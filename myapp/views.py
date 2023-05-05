from django.shortcuts import render,HttpResponse
from .models import upload

# Create your views here.
def welcome(request):
    return HttpResponse('<h1>welcome to my world!!!<h1>')

def submit(request):
    return render(request, 'submit.html')

def insert(request):
    if request.method=='POST':
        vfirstname = request.POST.get('firstname')
        vlastname = request.POST.get('lastname')
        vemail = request.POST.get('email')
        vfile = request.FILES.get('file')
        # print(vfirstname,vlastname,vemail,vfile)
        up = upload(fname=vfirstname, lname=vlastname, email=vemail, file=vfile)
        up.save()
        return render(request, 'submit.html')



    return render(request, 'home.html')