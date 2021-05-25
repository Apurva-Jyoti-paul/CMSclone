from django.shortcuts import redirect,render
from django.contrib.auth.decorators import login_required
from .models import text_block,webpage,website
from django.contrib.auth.models import User
from .forms import websiteForm

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
        