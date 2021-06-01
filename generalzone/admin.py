from django.contrib import admin
from . models import Enquiry,Complaint,Career,loginInfo

# Register your models here.
admin.site.register(Enquiry)
admin.site.register(Complaint)
admin.site.register(Career)
admin.site.register(loginInfo)
