from django.urls import path
from contact import views
urlpatterns = [
    path('',views.contact,name='contact'),
    path('addmessage/',views.addmessage,name='addmessage'),
    path('register/',views.register,name='register'),
    path('registered_students/',views.registered_students,name='registered_students'),]