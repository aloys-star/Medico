
from django.contrib import admin
from django.urls import path
from Medicoapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('innerpage/', views.innerpage, name='inner-page'),
    path('doctors/', views.doctors, name='doctors'),
    path('about/', views.about, name='about'),
    path('departments/', views.departments, name='departments'),
    path('contact/', views.Contact, name='contact'),
    path('appointment/', views.Appointment, name='appointment'),
    path('branch/', views.Branch, name='branch'),
    path('show/', views.show, name='show'),
    path('registration/', views.registartion, name='registration'),
    path('login/', views.login, name='login'),
    path('delete/<int:id>', views.delete),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('uploadimage/', views.upload_image, name='upload'),
    path('showimage/', views.show_image, name='image'),
    path('imagedelete/<int:id>', views.imagedelete),

    path('pay/', views.pay, name='pay'),
    path('stk/', views.stk, name='stk'),
    path('token/', views.token, name='token'),


]
