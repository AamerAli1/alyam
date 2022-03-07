from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'product_catalog_app'

urlpatterns = [
    path('login/', views.login_form, name='login_form'),
    path('',views.index,name = 'index'),
    path('products/', views.products, name='products'),
   
  
    path('<slug:category_slug>', views.products, name='product_by_category'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)