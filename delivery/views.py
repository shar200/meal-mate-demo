from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'delivery/index.html')

def signin(request):
    return render(request, 'delivery/signin.html')

def signup(request):
    return render(request, 'delivery/signup.html')

def handle_login(request):

    user= 'latha'
    pw='123456'
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        if username== user and password==pw:
            return render(request, 'delivery/success.html')
        else:
            return render(request, 'delivery/fail.html')
        #return HttpResponse(f"Username: {username} password: {password}")
    else:
        return HttpResponse("Invalid request")
    

def handle_signup(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        email=request.POST.get('email')
        mobile=request.POST.get('mobile')
        address=request.POST.get('address')
        data={
            "username": username, 
            "password": password,
            "email": email,
            "mobile": mobile,
            "address": address
        }
        return render(request, 'delivery/userdata.html', data)
        #return HttpResponse(f"Username: {username}, password: {password}, Email: {email}, Mobile: {mobile}, Address: {address} ")
    else:
        return HttpResponse("Invalid request")
