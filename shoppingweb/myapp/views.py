from django.shortcuts import render

# Create your views here.
def home(request):
 return render(request, 'home.html')

def product_detail(request):
 return render(request, 'productdetail.html')

def add_to_cart(request):
 return render(request, 'addtocart.html')

def buy_now(request):
 return render(request, 'buynow.html')

def profile(request):
 return render(request, 'profile.html')

def addaddress(request):
 return render(request, 'addaddress.html')

def address(request):
 return render(request, 'address.html')

def orders(request):
 return render(request, 'orders.html')

def change_password(request):
 return render(request, 'changepassword.html')

def mobile(request):
 return render(request, 'mobile.html')

def login(request):
 return render(request, 'login.html')

def logout(request):
 return render(request, '/')

def customerregistration(request):
 return render(request, 'customerregistration.html')

def checkout(request):
 return render(request, 'checkout.html')

# error handling when a user or resource is not found
def error_404(request, exception):
    return render(request,'404.html')