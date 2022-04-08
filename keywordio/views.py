
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from keywordio.models import *
from keywordio.forms import bookenter
import datetime
from datetime import timedelta
# Create your views here.
def home(request):
        form=bookenter()
        return render(request,'home.html',{'form':form})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            print('invalid data')
            return redirect('login')
    else:
        return render(request,'adminlogin.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                print('username taken')
            elif User.objects.filter(email=email).exists():
                print('mail id used')
            else:
                user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save();
                return redirect('login')
                print('user created')
        else:
            print('password does not match')
        return redirect('/')
    else:
        return render(request,'adminreg.html')

def addbook(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method =='POST':
        bookname = request.POST['bookname']
        auther = request.POST['auther']
        ISBN = request.POST['ISBN']
        category = request.POST['category']
        quantity = request.POST['quantity']

        ins = book(bookname=bookname,auther=auther,ISBN=ISBN,category=category,quantity=quantity)
        ins.save()
        return render(request,'add_book.html')
    else:
        return render(request,'add_book.html')

def studentregister(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method =='POST':
        studentfirstname = request.POST['studentfirstname']
        studentlastname = request.POST['studentlastname']
        branch = request.POST['branch']
        enrollnumber = request.POST['enrollnumber']
        username = request.POST['username']
        password = request.POST['password']
        ins1 = student(studentfirstname=studentfirstname, studentlastname= studentlastname,branch=branch,enrollnumber=enrollnumber,username=username,password=password)
        ins1.save()
        return render(request,'register_student.html')
    else:
        return render(request,'register_student.html')
   
def studentdata(request):
    students = student.objects.all()
    return render(request,'student_data.html',{'students':students})

def bookdata(request):
    books = book.objects.all()
    return render(request,'book_data.html',{'books':books})

def issuebook(request):
    if not request.user.is_authenticated:
        return redirect('login')
   # data = student.objects.get(all)
    #data1 = book.objects.get(all)

    if request.method=='POST':     
        stu0 = request.POST['studentenroll']
        bookname = request.POST['bookname']
        tday = datetime.date.today()
        tdelta = datetime.timedelta(days=30)
        ex = tday+tdelta
        studata = student.objects.filter(enrollnumber=stu0).first()
        book1=book.objects.filter(bookname=bookname).first()
        if book1.quantity>0:
           book1.quantity-=1
           book1.save()
           ins1=issuedbooks(studentname=studata.studentfirstname,enrollnumber=studata.enrollnumber,branch=studata.branch,bookname=book1.bookname,auther=book1.auther,issueddate=tday,expiryddate=ex)
           ins1.save()
           return redirect('/')
        else:
           return redirect('/')
    else:
        return redirect('/')

def returnbook(request,id):
    if not request.user.is_authenticated:
        return redirect('login')
    data1=issuedbooks.objects.get(pk=id)
    bookname1=data1.bookname
    auther1=data1.auther
    d0=book.objects.filter(bookname=bookname1,auther=auther1).first()
    data1.delete()
    print(d0.quantity)
    d0.quantity+=1
    d0.save()
    return redirect('issuedlist')


def issuenewbook(request):
    if not request.user.is_authenticated:
        return redirect('login')
    booklist=book.objects.all()
    studentlist=student.objects.all()
    return render(request,'issuebook.html',{'booklist':booklist,'studentlist':studentlist})

def issuedlist(request):
    issuelist = issuedbooks.objects.all()
    return render(request,'issuedlist.html',{'issuelist':issuelist})

def delet_book_data(request,id):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method=="POST":
        delbook = book.objects.get(pk=id)
        d0=book.objects.filter(pk=id).first()
        b0=d0.bookname
        d1=issuedbooks.objects.filter(bookname=b0).first()
        d1.delete()
        delbook.delete()
        return redirect('/')

def delet_student_data(request,id):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method=="POST":
        delstudent = student.objects.get(pk=id)
        delstudent.delete()
        return redirect('/')




