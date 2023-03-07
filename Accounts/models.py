from django.db import models
from dbview.models import DbView
# Create your models here.
class Employer(models.Model):
    EmpName=models.CharField(max_length=50)
    EmpEmailID=models.CharField(max_length=50)
    EmpPhoneNo=models.IntegerField()
    EmpAddress=models.TextField()
    EmpUsername=models.TextField(max_length=20,unique=True)
    EmpPassword = models.TextField(max_length=20)
class Jobseeker(models.Model):
    JobseekerFirstName = models.CharField(max_length=50)
    JobseekerLastName = models.CharField(max_length=50)
    JobseekerGender=models.CharField(max_length=20)
    JobseekerDob=models.CharField(max_length=20)
    JobseekerUsername = models.TextField(max_length=20, unique=True)
    JobseekerPassword = models.TextField(max_length=20)
    JobseekerEmailID = models.CharField(max_length=50)
    JobseekerPhoneNo = models.IntegerField()
    JobseekerSkill=models.TextField()
    JobseekerExperience=models.IntegerField()
    JobseekerTitle=models.TextField(max_length=20)
class JobListing(models.Model):
    EmployerID= models.ForeignKey(Employer,on_delete=models.CASCADE)
    JobTitle=models.TextField()
    JobDesc=models.TextField()
    JobLocation = models.TextField(null=True)
    JobCategory=models.TextField()
    JobSalary=models.IntegerField()
    Jobskill=models.TextField()
    JobStatus=models.BooleanField(default=True)
class JobApplication(models.Model):
    EmployerID = models.ForeignKey(Employer,on_delete=models.CASCADE)
    JobseekerID = models.ForeignKey(Jobseeker,on_delete=models.CASCADE)
    JobseekerCover=models.TextField()
    JobStatus=models.CharField(max_length=50)
    JobListingID=models.ForeignKey(JobListing,on_delete=models.CASCADE)
    JobseekerResume= models.FileField(upload_to='Resume')