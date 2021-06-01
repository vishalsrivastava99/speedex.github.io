from django.db import models

# Create your models here.
class Enquiry(models.Model):
    name=models.CharField(max_length=50)
    gender=models.CharField(max_length=6)
    address=models.TextField()
    contactno=models.CharField(max_length=15)
    emailaddress=models.EmailField()
    enquirytext=models.TextField()
    enquirydate=models.CharField(max_length=20)
class Complaint(models.Model):
    name=models.CharField(max_length=50)
    gender=models.CharField(max_length=6)
    address=models.TextField()
    contactno=models.CharField(max_length=15)
    emailaddress=models.EmailField()
    subject=models.CharField(max_length=200)
    complainttext=models.TextField()
    complaintdate=models.CharField(max_length=20)
class Career(models.Model):
    name=models.CharField(max_length=50)
    gender=models.CharField(max_length=6)
    address=models.TextField()
    contactno=models.CharField(max_length=15)
    emailaddress=models.CharField(max_length=50,primary_key=True)
    qualification=models.CharField(max_length=50)
    experience=models.CharField(max_length=10)
    keyskills=models.TextField()
    cv=models.CharField(max_length=100)
    connectdate=models.CharField(max_length=20)
class loginInfo(models.Model):
    userid=models.CharField(max_length=50)
    password=models.CharField(max_length=20)
    usertype=models.CharField(max_length=20)




