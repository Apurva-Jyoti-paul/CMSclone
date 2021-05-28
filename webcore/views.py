from django.shortcuts import redirect,render
from django.contrib.auth.decorators import login_required
from .models import media, text_block,webpage,website
from django.contrib.auth.models import User
from .forms import websiteForm,txtForm,picForm,save_mediaform
import cloudinary

@login_required
def index(request):
    #a=
    a= website.objects.filter(admin=request.user)
    b= webpage.objects.filter(web__admin=request.user)
    return render(request,'home.html',{'a':a,'b':b})
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

@login_required
def create_website(request):
    if request.method=='POST':
        form= websiteForm(request.POST)
        #form.admin= request.user
        if form.is_valid():
            f=form.save(commit=False)
            f.admin= request.user
            f.save()
            return redirect('home.html')
    else:
        form = websiteForm()
        return render(request,'Createwebsite.html',{'form':form})
        
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


def betaformview(request,key,k):

    page = webpage.objects.get(web__hname=key,identifier=k)
    print(page)
    midia=media.objects.filter(webp=page).order_by('-id')
    print(midia[0].med)
    return render(request,'editbeta.html',{'page':page,'key':key,'midia':midia})


def save_media(request,key):
    if request.method=='POST':
        f= save_mediaform(request.POST)
        l=webpage.objects.get(identifier=key)
        print(l)
        if f.is_valid():
            sv=f.save(commit=False)
            sv.webp=l
            print('a')
            sv.save()
            return redirect("../")
    else:
        f=save_mediaform()
        return render(request,'editbeta.html',{'f':f})
