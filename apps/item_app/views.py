from django.shortcuts import render, redirect
from django.contrib import messages
from models import Item
from ..login_app.models import User

# Create your views here.
def session_check(request):
    try: 
        return request.session['user_id']
    except:
        return False

def index(request):
    if session_check(request) == False:
        return redirect('/')
    context = {
        'items': Item.objects.all(),
        'users': User.objects.all(),
        'wishlist': User.objects.get(id = request.session['user_id']).wish_item.all()
    }
    
    return render(request,'item_app/index.html',context)

def add_item(request):
    if session_check(request) == False:
        return redirect('/')
    return render(request,'item_app/add_item.html')

def add_proccess(request):
    user = User.objects.filter(id = request.session['user_id']).first()
    #when adding a item the user id is stored in sessions and that is referred to when i show an item and all the users who put it in their list 
    print"~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print user
    results = Item.objects.itemVal(request.POST,user)
    print'!!!!!!!!!!!!!!!!!!!!!!'
    if results['status'] == True:
        for error in results['errors']:
            messages.error(request, error)
        return redirect('/item/add_item')
    print results
    return redirect('/item')

def logout(request):
    request.session.flush()
    return redirect('/')

def remove(request, item, user):
    print '*******************'
    user = User.objects.get(id = user)
    item = Item.objects.get(id = item)
    wish = user.wish_item.remove(item)
    # abit sloppy but gets the job done.. could be like the add function.. just needed to print to see how it was storing things in the data base 
    print user
    print wish
    print '*******'
    return redirect('/item')

def add(request, item, user):
    User.objects.get(id = user).wish_item.add(Item.objects.get(id = item))
    return redirect('/item')

def delete(request, item, user):
    print"$$$$$$$$$$$$$$$$$$$$$$$$$$$"
    x =User.objects.get(id = user).wish_item.delete(Item.objects.get(id = item))
    print x
    #still need to work on this ... the query is right just need to figure out the syntax for the html 
    return redirect('/item')

def showall(request,item):
    if session_check(request) == False:
        return redirect('/')
  
    context={
        'show': User.objects.all(),
        'item': Item.objects.get(id = item)
    }
    #to show all the users that want that item , need to beable to grab that id and user the many to many key linking the models together
  

    return render(request,'item_app/showall.html',context)

def show(request,item):
    x =Item.objects.get(id = item)
    #get(id = item ) sets the word 'item' to the id of the item
    print x
    return redirect('/item/showall')

