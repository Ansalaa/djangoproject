from django.shortcuts import render,redirect
from books.models import Book
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request,'home.html')

@login_required

def add(request):
    if(request.method=="POST"):
        t=request.POST['t']
        a=request.POST['a']
        p=request.POST['p']
        g=request.POST['g']
        l=request.POST['l']
        c=request.FILES['c']
        d=request.FILES['d']
        b=Book.objects.create(title=t,author=a,price=p,pages=g,language=l,cover=c,pdf=d)
        b.save()
        return view(request)

    return render(request, 'add.html')

@login_required
def view(request):

    k=Book.objects.all()      #Read all record from table book
    context={'books':k}        #passes data from views to html file. Context is dictionary type
    return render(request,'view.html',context)


def details(request,p):
    b=Book.objects.get(id=p)   #read a perticular record from table Book
    context={'books':b}
    return render(request,'details.html',context)

def edit(request,p):
    b=Book.objects.get(id=p)
    if (request.method == "POST"):  # After submitting form
        b.title = request.POST['t']
        b.author = request.POST['a']
        b.price = request.POST['p']
        b.pages = request.POST['g']
        b.language = request.POST['l']
        if (request.FILES.get('c') == None):
            b.save()
        else:
            b.cover = request.FILES.get('c')
        if (request.FILES.get('d') == None):
            b.save()
        else:
            b.pdf = request.FILES.get('d')

        b.save()
        return redirect('books:view')

    context={'books':b}
    return render(request,'edit.html',context)



def delete(request,p):
    b=Book.objects.get(id=p)
    b.delete()
    return redirect('books:view')

from django.db.models import Q
def search(request):
    b=None   #Initialized to none
    query=""

    if(request.method=='POST'):  #After form submission
        query=request.POST['q']
        if query:
            b=Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query))  #django lookups

    return render(request,'search.html', {'books':b,'query':query})
