from django.shortcuts import render, redirect
from movies.models import Movie



def home(request):
    k = Movie.objects.all()
    context = {'movies':k}
    return render(request,"home.html",context)

def add(request):
    if (request.method == "POST"):
        t = request.POST['t']
        d = request.POST['d']
        l = request.POST['l']
        y = request.POST['y']
        i = request.FILES['i']
        m = Movie.objects.create(title=t, description=d, language=l, year=y, cover=i)
        m.save()
        return redirect('home')

    return render(request,"add.html")

def details(request,p):
    m=Movie.objects.get(id=p)
    context={'movies':m}
    return render(request,'details.html',context)

def delete(request,p):
    m=Movie.objects.get(id=p)
    m.delete()
    return redirect('home')

def update(request,p):
    m=Movie.objects.get(id=p)
    if (request.method == "POST"):  # After submitting form
        m.title = request.POST['t']
        m.description = request.POST['d']
        m.language = request.POST['l']
        m.year = request.POST['y']
        if (request.FILES.get('i') == None):
            m.save()
        else:
            m.cover = request.FILES.get('i')
        m.save()
        return redirect('home')

    context={'movies':m}
    return render(request,'update.html',context)
