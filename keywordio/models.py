from django.db import models
# Create your models here.
class book(models.Model):
    bookname=models.CharField(max_length=60)
    auther=models.CharField(max_length=60)
    ISBN=models.IntegerField()
    category=models.CharField(max_length=60)
    quantity=models.IntegerField()
    

    def __str__(self):
        return self.bookname
    

class student(models.Model):
    studentfirstname=models.CharField(max_length=60)
    studentlastname=models.CharField(max_length=60)
    branch=models.CharField(max_length=60)
    enrollnumber=models.IntegerField(default=1)
    username=models.CharField(max_length=60)
    password=models.CharField(max_length=60)

    def __str__(self):
        return self.studentfirstname

class issuedbooks(models.Model):
    studentname = models.CharField(max_length=60)
    enrollnumber = models.IntegerField(default='')
    branch = models.CharField(max_length=60)
    bookname=models.CharField(max_length=60)
    auther = models.CharField(max_length=60,default='N/A')
    issueddate = models.DateField(auto_now_add=True,null=True,blank=True)
    expiryddate = models.DateField(auto_now_add=False,null=True,blank=True)


    def __str__(self):
        return self.bookname
   
class studentissue(models.Model):
    stdinfo = models.CharField(max_length=60,default='0000000')
    book = models.CharField(max_length=60,default='0000000')
    issue_date = models.DateField(auto_now_add=True,null=True,blank=True)
    expiry_date = models.DateField(auto_now_add=True,null=True,blank=True)


    def __str__(self):
        return self.bookname
