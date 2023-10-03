from django.shortcuts import render,HttpResponse
from django.contrib.auth.models import User

# Create your views here.

def signup(request):
    return render(request,'signup1.html')
    #if request.method == 'POST':
        #uname = request.POST.get('username')
        #email = request.POST.get('email')
        #pass1=request.POST.get('password')
        ##my_user = User.objects.create_user(uname,email,pass1)
        #my_user.save()
        #return HttpResponse("User account has created ")

        #print(uname,email,pass1,pass2)'''
    

def login(request):
    return render(request,'index.html')

def logout(request):
    return render(request,'index.html')
