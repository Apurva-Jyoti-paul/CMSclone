from django.shortcuts import redirect,render
from django.contrib.auth.decorators import login_required
from .models import text_block,webpage,website


def index(request):
    return render(request,'home.html')
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
        
        