from django.shortcuts import render,redirect,reverse
from . models import Enquiry,Complaint,Career,loginInfo
import datetime
from django.core.exceptions import ObjectDoesNotExist
from django.core.files.storage import FileSystemStorage
from . import smssender
from adminzone.models import Notification,Consignment


# Create your views here.
def index(request):
    nf=Notification.objects.all()
    return render(request,'index.html',{'nf':nf})
def about(request):
    nf=Notification.objects.all()
    return render(request,'about.html',{'nf':nf})
def login(request):
    nf=Notification.objects.all()
    return render(request,'login.html',{'nf':nf})
def tracking(request):
    nf=Notification.objects.all()
    return render(request,'tracking.html',{'nf':nf})
def complaint(request):
    nf=Notification.objects.all()
    return render(request,'complaint.html',{'nf':nf})
def enquiry(request):
    nf=Notification.objects.all()
    return render(request,'enquiry.html',{'nf':nf})
def career(request):
    nf=Notification.objects.all()
    if request.method=='POST' and request.FILES['myfile']:
        name=request.POST['name']
        gender=request.POST['gender']
        address=request.POST['address']
        contactno=request.POST['contactno']
        emailaddress=request.POST['emailaddress']
        qualification=request.POST['qualification']
        experience=request.POST['experience']
        keyskills=request.POST['keyskills']
        myfile=request.FILES['myfile']
        cv=myfile.name
        connectdate=datetime.datetime.now().strftime('%Y/%m/%d')
        if Career.objects.filter(emailaddress=emailaddress).exists():
            msg='The User is registered'
        else:
            c=Career(name=name,gender=gender,address=address,contactno=contactno,emailaddress=emailaddress,qualification=qualification,experience=experience,keyskills=keyskills,cv=cv,connectdate=connectdate)
            c.save()
            fs=FileSystemStorage()
            fs.save(cv,myfile)
            msg='Your registration is done.'
        return render(request,'Career.html',{'msg':msg,'nf':nf})
    return render(request,'career.html',{'nf':nf})
def saveenquiry(request):
    name=request.POST['name']
    gender=request.POST['gender']
    address=request.POST['address']
    contactno=request.POST['contactno']
    emailaddress=request.POST['emailaddress']
    enquirytext=request.POST['enquirytext']
    enquirydate=datetime.datetime.now().strftime("%Y/%m/%d")
    en=Enquiry(name=name,gender=gender,address=address,contactno=contactno,emailaddress=emailaddress,enquirytext=enquirytext,enquirydate=enquirydate)
    en.save()
    smssender.sendsms(contactno, 'Thanks for enquiry. We will contact you soon. -Team HR')
    return redirect('index')
def savecomplaint(request):
    name=request.POST['name']
    gender=request.POST['gender']
    address=request.POST['address']
    contactno=request.POST['contactno']
    emailaddress=request.POST['emailaddress']
    subject=request.POST['subject']
    complainttext=request.POST['complainttext']
    complaintdate=datetime.datetime.now().strftime('%Y/%m/%d')
    cp=Complaint(name=name,gender=gender,address=address,contactno=contactno,emailaddress=emailaddress,subject=subject,complainttext=complainttext,complaintdate=complaintdate)
    cp.save()
    return redirect('index')
def validateuser(request):
    userid=request.POST['userid']
    password=request.POST['password']
    try:
        v=loginInfo.objects.get(userid=userid,password=password)
        if v is not None:
            request.session['userid']=userid
            return redirect(reverse('adminzone:adminhome'))
    except ObjectDoesNotExist:
        return redirect('login')
def search(request):
    refno=request.POST['refno']
    con=Consignment.objects.get(refno=refno)
    return render(request,'tracking.html',{'con':con})


