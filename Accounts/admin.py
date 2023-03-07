from django.contrib import admin
from .models import  *

# Register your models here.
admin.site.register(Employer)
admin.site.register(Jobseeker)
admin.site.register(JobApplication)
admin.site.register(JobListing)
