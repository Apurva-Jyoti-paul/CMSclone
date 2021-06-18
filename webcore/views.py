from django.shortcuts import redirect,render
from django.contrib.auth.decorators import login_required
from .models import contents, media, text_block,webpage,website,testtext
from django.contrib.auth.models import User
from .forms import pageForm, websiteForm,txtForm,picForm,save_mediaform,save_contents,testform
import cloudinary
from django.http import HttpResponseForbidden,HttpResponseNotFound
from django.views.decorators.cache import never_cache



def base(request):
    return render(request,'index.html',{})


@never_cache
@login_required
def index(request):
    #a=
    a= website.objects.filter(admin=request.user)
    b= testtext.objects.filter(site__admin=request.user).order_by('-id')
  #  midia=media.objects.filter(webp__web__admin=request.user).order_by('-id')[0:5]
    webno=a.count()
    pagno=b.count()
    midia2=media.objects.filter(webp__web__admin=request.user)
    b=b[0:3]
    for i in a:
        print(i.hname,i.id)
    midno=midia2.count()
    print(webno,pagno,midno)

    return render(request,'Maindashboard.html',{'a':a,'b':b,'webno':webno,'pagno':pagno,'midno':midno})
# Create your views here.

def view(request,key):
    if request.method == 'GET':
        #key parser
        a=[]
        k=key
        m=''
        for i in k:
            if i!=' ':
                m=m+i
            else:
                a.append(m)
                m=''
        a.append(m)
        print(a)
        c1=a.count(1)       
#if c1 < 2:
 #           return redirect('invalidurl.html')

        t= webpage.objects.filter(web__hname=a[-2],identifier=a[-1])
        print(t)
        print("a")
        tlist = list(t)
        print(tlist)
        c2 = t.count()
        if c2 ==1:
            block=text_block.objects.filter(page=tlist[0])
            print(block)
            return render(request,'vuw.html',{'block':block,'t':t})
        else:
            return redirect('error404.html')


@never_cache
@login_required
def create_website(request):
    if request.method=='POST':
        form= websiteForm(request.POST)
        #form.admin= request.user
        if form.is_valid():
            f=form.save(commit=False)
            f.admin= request.user
            f.save()
            return redirect('../activity/')
    else:
        form = websiteForm()
        return render(request,'Createwebsite.html',{'form':form})

@never_cache        
@login_required
def edit_pagetxt(request,key):
    if request.method=='POST':
        c= text_block.objects.filter(page__identifier=key).order_by('seq')
        a= webpage.objects.get(identifier=key)
        p = c.count()
        form= txtForm(request.POST,request.FILES)
        print(form)
        if 1:
            print('a')                                    ###buggy view
            f=form.save(commit=False)
            print(request.FILES)
            obj = cloudinary.uploader.upload(request.FILES)
            f.link = obj['url']
            p=p+1
            f.seq=p
            f.web = a
            f.save()
            return redirect("../home.html")
    else:
        form=txtForm()
        return render(request,'editbeta.html',{'form':form})
@never_cache
@login_required
def betaformview(request,key,k):

    page = webpage.objects.get(web__hname=key,identifier=k)
    arr="&quot;"
    print(page)
    midia=media.objects.filter(webp=page).order_by('-id')
    g=contents.objects.filter(pag__identifier=k,pag__web__hname=key).order_by('-id')

    if g:
        f=g[0]
        print(g,f)
        print(f.text)
    else:
        f=''
    if(midia.count()):
        print(midia[0].med)
    
  
    return render(request,'editbeta.html',{'page':page,'key':key,'midia':midia,'k':k,'arr':arr,'f':f})

@never_cache
@login_required
def save_media(request,key,k):
    if request.method=='POST':
        f= save_mediaform(request.POST)
        l=webpage.objects.get(identifier=key)
        print(l)
        print(f)
        if f.is_valid():
            print("success")
            sv=f.save(commit=False)
            sv.webp=l
            print('a')
            sv.save()
            return redirect("/betaedit")
    else:
        f=save_mediaform()
        return render(request,'editbeta.html',{'f':f})

@never_cache
@login_required
def save_content(request,k,key):
    o=webpage.objects.get(identifier=k,web__hname=key)
    print('a',o)
    
    
    if request.method=='POST':
        cf=save_contents(request.POST)
        
        print(cf)
        if cf.is_valid():
            print(cf)
            t=cf.cleaned_data.get('text')
            print(t)
            j=cf.save(commit=False)
            j.pag=o
            
            j.save()
            print(j)
            g=contents.objects.filter(pag__identifier=k,pag__web__hname=key).order_by('-id')

            print(g.count())
            for i in g:
                fof=i
             

            print(fof)
        
            return render(request,'editwebpage.html',{'t':t})
        else:
            return redirect('/home')
    else:
        cf=save_contents()
        return render(request,'editbeta.html',{'cf':cf})

@never_cache
def watch(request,key,k):
    g=contents.objects.filter(pag__identifier=k,pag__web__hname=key).order_by('-id')

    print(g)
    f=g[0]
    print(g,f)
    print(f.text)
    print(f.align)
    return render(request,'watch.html',{'f':f})

@never_cache
@login_required  
def crt_page(request,key):
    if request.method=='POST':
        try:
            q=website.objects.get(hname=key)
            if (request.user==q.admin):
                if(q):
                    form=pageForm(request.POST)
                    if form.is_valid():
                        k=form.save(commit=False)
                        k.web=q
                        k.save()
                        return redirect('/home')
            else:
                return render(request,'nwebsite.html',{})
        except:
            return HttpResponseForbidden()
    else:
        form=pageForm()
        q=website.objects.get(hname=key)
        return render(request,'createpage.html',{'form':form,'websi':q})

@never_cache
@login_required
def show_all(request):
    site=website.objects.filter(admin=request.user)
    pages= webpage.objects.filter(web__admin=request.user)
    return render(request,'table.html',{'site':site,'pages':pages})
@never_cache
@login_required
def delete_website(request,key):
    g=website.objects.filter(admin=request.user,hname=key)
    
    if(g.count()==1):
        g.delete()

    return redirect('/home')    


def action_panel(request,key):

    c=webpage.objects.filter(web__hname=key,web__admin=request.user)
    
    if(c):
        t=c.count()
        print(t)
        return render(request,'objects.html',{'no':t,'pages':c,'key':key})
    else:
        return HttpResponseNotFound('<h1 style="text-align:center;">No Such Page Exists</h1>')

def show_testt(request,key,key2):
    sso=testtext.objects.filter(site__hname=key,title=key2)
    for s in sso:
        pass

    return render(request,'testtemp.html',{'s':s})

def take_test(request,key):
    if request.method=='POST':
        websiteobject=website.objects.get(hname=key)
        f=testform(request.POST,request.FILES)
        if f.is_valid():
            g=f.save(commit=False)
            g.site=websiteobject
            g.save()
            return redirect('../')
    else:
        f=testform()
        return render(request,'testform.html',{'f':f,'key':key})