from django.shortcuts import render,redirect
import datetime
from . models import Notification,Consignment,City
from generalzone.models import Enquiry,Complaint,Career
from django.contrib import auth


# Create your views here.
def adminhome(request):
    if request.session['userid']:
        nf=Notification.objects.all()
        return render(request,'adminhome.html',{'nf':nf})
    else:
        return render(request,'login.html')
def enquiries(request):
    if request.session['userid']:
        if request.session['userid']:
            enq=Enquiry.objects.all()
        return render(request,'enquiries.html',{'enq':enq})
    else:
        return render(request,'login.html')
def complains(request):
    if request.session['userid']:
        comp=Complaint.objects.all()
        return render(request,'complains.html',{'comp':comp})
    else:
        return render(request,'login.html')
def consignment(request):
    if request.session['userid']:
        city=City.objects.all()
        return render(request,'consignment.html',{'city':city})
    else:
        return render(request,'login.html')
def jobseekers(request):
    if request.session['userid']:
        car=Career.objects.all()
        return render(request,'jobseekers.html',{'car':car})
    else:
        return render(request,'login.html')
def addnotification(request):
    if request.session['userid']:
        notificationtext=request.POST['notificationtext']
        posteddate=datetime.datetime.now().strftime('%Y/%m/%d')
        nf=Notification(notificationtext=notificationtext,posteddate=posteddate)
        nf.save()
        return redirect('adminzone:adminhome')
    else:
        return render(request,'login.html')
def deletenotification(request,id):
    if request.session['userid']:
        nf=Notification.objects.get(id=id)
        nf.delete()
        return redirect('adminzone:adminhome')
    else:
        return render(request,'index.html')
def deleteenquiries(request,id):
    if request.session['userid']:
        en=Enquiry.objects.get(id=id)
        en.delete()
        return redirect('adminzone:enquiries')
    else:
        return render(request,'login.html')
def deletecomplains(request,id):
    if request.session['userid']:
        co=Complaint.objects.get(id=id)
        co.delete()
        return redirect('adminzone:complains')
    else:
        return render(request,'login.html')
def saveconsignment(request):
    if request.session['userid']:
        refno=request.POST['refno']
        sendername=request.POST['sendername']
        senderaddress=request.POST['senderaddress']
        sendercontactno=request.POST['sendercontactno']
        receivername=request.POST['receivername']
        receiveraddress=request.POST['receiveraddress']
        source=request.POST['source']
        currentcity=request.POST['currentcity']
        destination=request.POST['destination']
        status=request.POST['status']
        posteddate=datetime.datetime.now().strftime('%Y/%m/%d')
        if Consignment.objects.filter(refno=refno).exists():
            msg='This entry already exists.'
        else:
            con=Consignment(refno=refno,sendername=sendername,senderaddress=senderaddress,sendercontactno=sendercontactno,receivername=receivername,receiveraddress=receiveraddress,source=source,currentcity=currentcity,destination=destination,status=status,posteddate=posteddate)
            con.save()
            msg='The entry is done.'
        return render(request,'consignment.html',{'msg':msg})
    else:
        return render(request,'login.html')
def deletejobseekers(request,emailaddress):
    if request.session['userid']:
        c = Career.objects.get(emailaddress=emailaddress)
        c.delete()
        return redirect('adminzone:jobseekers')
    else:
        return render(request,'login.html')
def logout(request):
    auth.logout(request)
    return redirect('index')


