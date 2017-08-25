from django.shortcuts import render, redirect
from django.contrib import messages
from models import User
# Create your views here.
def index(request):
    return render(request,'login_app/index.html')

def register(request):
    results = User.objects.regVal(request.POST)
    if results['status'] == False:
        for error in results['errors']:
            messages.error(request, error)
        return redirect('/')    
    user = User.objects.creator(request.POST)
    messages.success(request,'user has been created')
    return redirect('/')

def login(request):
    results = User.objects.loginVal(request.POST)
    if results['status'] == False:
        for error in results['errors']:
            messages.error(request, error)
        return redirect('/')

    request.session['user_id'] = results['user'].id 
    request.session['username'] = results['user'].username
    print results
    return redirect('/item')