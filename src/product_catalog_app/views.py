from django.shortcuts import render,redirect,get_object_or_404
from management.models import Pin
from .models import Product,Category
from .forms import PasswordForm


# Create your views here.


def index(request):
    """The home page for product_catalog_app"""
    return render(request, 'product_catalog_app/index.html')



def login_form(request):

    if request.method != 'POST' :
        form = PasswordForm()
    
    else:
        form = PasswordForm(data = request.POST)

        # Initiate your session variable
        request.session['password'] = 'invalid'

        if (request.method == 'POST') : 
            if form.is_valid():
                form_password = form['passcode'].value()

                # get the actual password info form the database
                password_object = Pin.objects.get(id=1).passcode

                if (password_object == form_password):
                    request.session['password'] = 'valid'
                    form.save()
                    return redirect('product_catalog_app:products')


    context = {'form' : form}
    return render(request, 'product_catalog_app/loginform.html',context)

            


def products(request,category_slug=None):
    if (request.session['password'] != 'valid'):
        return redirect('product_catalog_app/index.html')
    
    category = None
    categories = Category.objects.all()
    data = Product.objects.all()
    if category_slug:
        category = get_object_or_404(Category,slug=category_slug)
        data = Product.objects.filter(category=category)
    if 'q' in request.GET:
        q = request.GET['q']
        if category != None :
            data = Product.objects.filter(name__icontains=q,category=category)
        else:
            data = Product.objects.filter(name__icontains=q)
 

    return render(request, 'product_catalog_app/products.html', {'categories':categories,
                                              'category':category,
                                              'products':data,
                                              })




                    
# def login_form(request):
#     """ supposed to check password now adds a password"""
#     if request.method !=  'POST':
#         # No data submitted; create a blank form.
#         form = PasswordForm()
#     else:
#         # POST data submitted; process data.
#         form = PasswordForm(data = request.POST)
#         if form.is_valid():
#             sample_instance = Pin.objects.get(id=1)
#             value_of_field = sample_instance.passcode
#             passcode = form['passcode'].value()
    
        

#             if value_of_field == passcode:
#                 # form.save()
#                 print("*******************\nIt's the same")
#                 return redirect('product_catalog_app:products')
#             else:
#                 print("*******************\nMission failed , we will get them next time")
         

#     context = {'form' : form}
#     return render(request, 'product_catalog_app/loginform.html',context)


