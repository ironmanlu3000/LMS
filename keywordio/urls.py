from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('addbook',views.addbook,name='addbook'),
    path('studentregister',views.studentregister,name='studentregister'),
    path('studentdata',views.studentdata,name='studentdata'),
    path('bookdata',views.bookdata,name='bookdata'),
    path('issuebook',views.issuebook,name='issuebook'),
    path('issuenewbook',views.issuenewbook,name='issuenewbook'),
    path('issuedlist',views.issuedlist,name='issuedlist'),
    path('returnbook/<int:id>/',views.returnbook,name='returnbook'),
    path('delete/<int:id>/',views.delet_book_data,name='delete_book'),
    path('deletestudent/<int:id>/',views.delet_student_data,name='delete_student')
]
