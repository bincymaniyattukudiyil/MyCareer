from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.db.models import Q

from django.shortcuts import render, redirect
from .models import *
from . forms import FileForm

# Create your views here.
def GetEmployerId(request):

    current_user = request.user
    name = current_user.username
    objs = Employer.objects.filter(EmpUsername=name)
    if len(objs) == 1:
        obj = objs[0]
    else:
        pass
    EmployerID = obj.id
    return EmployerID
def GetJobseekerId(request):

    current_user = request.user
    name = current_user.username
    Userobjs = Jobseeker.objects.filter(JobseekerUsername=name)
    if len(Userobjs) == 1:

        jobseekerobj = Userobjs[0]
        JobseekerID = jobseekerobj.id
        print('id is,', JobseekerID)
        return JobseekerID
    else:
        pass

def index(request):
    return render(request, "Index.html")

def Register(request):
    print(request.method)
    if request.method == 'POST':
        print('hi')
        JobseekerFirstName = request.POST['JobseekerFirstName']
        JobseekerLastName = request.POST['JobseekerLastName']
        JobseekerGender = request.POST['JobseekerGender']
        JobseekerDob = request.POST['JobseekerDob']
        JobseekerUsername = request.POST['JobseekerUsername']
        JobseekerPassword = request.POST['JobseekerPassword']
        JobseekerEmailID = request.POST['JobseekerEmailID']
        JobseekerPhoneNo = request.POST['JobseekerPhoneNo']
        JobseekerSkill = request.POST['JobseekerSkill']
        JobseekerExperience = request.POST['JobseekerExperience']
        JobseekerTitle=request.POST['JobseekerTitle']
        if Jobseeker.objects.filter(JobseekerUsername=JobseekerUsername).exists():

            # messages.info(request, "username exist")
            return redirect('JobseekerRegister')
        else:
            JobseekerProfile = Jobseeker(JobseekerFirstName=JobseekerFirstName,JobseekerLastName=JobseekerLastName,
                                         JobseekerGender=JobseekerGender, JobseekerDob=JobseekerDob, JobseekerPassword=JobseekerPassword,
                                         JobseekerEmailID = JobseekerEmailID, JobseekerPhoneNo=JobseekerPhoneNo,
                                         JobseekerSkill=JobseekerSkill,JobseekerExperience=JobseekerExperience,
                                         JobseekerTitle =JobseekerTitle,JobseekerUsername=JobseekerUsername)
            JobseekerProfile.save()
            user = User.objects.create_user(password=JobseekerPassword,
                                            username=JobseekerUsername)
            user.save();
        return render(request, 'index.html')

    else:
        return render(request, 'JobseekerRegister.html')
    return render(request, "Index.html")
def EmpRegister(request):
    print(request.method)
    if request.method == 'POST':
        print("hi")
        EmpName = request.POST['EmpName']
        EmpEmailID = request.POST['EmpEmailID']
        EmpPhoneNo = request.POST['EmpPhoneNo']
        EmpAddress = request.POST['EmpAddress']
        EmpUsername = request.POST['EmpUsername']
        EmpPassword = request.POST['EmpPassword']
        if Employer.objects.filter(EmpUsername=EmpUsername).exists():

            # messages.info(request, "username exist")
            return redirect('index')
        else:
            EmployerRegister = Employer(EmpName=EmpName,EmpEmailID=EmpEmailID,EmpPhoneNo=EmpPhoneNo,EmpAddress=EmpAddress,
                                        EmpUsername=EmpUsername,EmpPassword=EmpPassword)
            EmployerRegister.save()
            user = User.objects.create_user(password=EmpPassword,
                                            username=EmpUsername)
            user.save();
        return render(request, 'index.html')

    else:
        return render(request, 'EmployerRegister.html')

    return render(request, "Index.html")
def JobRegister(request):

    if request.method == 'POST':
        EmployerID=GetEmployerId(request)
        JobTitle = request.POST['JobTitle']
        JobDesc = request.POST['JobDesc']
        JobLocation = request.POST['JobLocation']
        JobCategory = request.POST['JobCategory']
        JobSalary = request.POST['JobSalary']
        Jobskill = request.POST['Jobskill']
        JobStatus = True
        print(JobCategory,JobStatus)
        Job = JobListing.objects.create(EmployerID_id=EmployerID, JobTitle=JobTitle, JobDesc=JobDesc,JobLocation=JobLocation,Jobskill=Jobskill,JobSalary=JobSalary,JobCategory=JobCategory,JobStatus=JobStatus)
        Job.save()
    else:
        return render(request, "JobListing.html")

    return render(request,"JobListing.html")
def JobSearch(request):
    if request.method == 'POST':
        Title=request.GET.get('Title')
        Location = request.GET.get('Location')
        Category = request.GET.get('Category')

        item=JobListing.objects.all().filter((Q(JobTitle__contains=Title) | Q(JobDesc__contains=Title)
                                             | Q(JobLocation__contains=Location) | Q(JobCategory__contains=Category) |
                                             Q(Jobskill__contains=Title)) & Q(JobStatus__contains='Active'))

        return render(request, "JobSerch.html",{'item':item,'Title':Title,'Location':Location,'Category':Category})
    return render(request, 'index.html')
def EmpLogin(request):
    if request.method =='POST':
        print("here1")
        username = request.POST['EmpUsername']
        password = request.POST['EmpPassword']
        user = auth.authenticate(username=username, password=password)
        print(username)
        print(password)
        if user is not None:
            auth.login(request, user)
            EmployerID=GetEmployerId(request)
            ApplicantID=JobApplication.objects.all().filter(EmployerID=EmployerID)
            # print((ApplicantID.JobseekerID).id)
            # print(ApplicantID)
            # # item = Jobseeker.objects.filter(id__in=[(ApplicantID.JobseekerID).id])
            # # print(ApplicantID)
            # if len(ApplicantID)>=1:
            #     ids=[]
            #
            #
            #     for i in ApplicantID:
            #
            #         print(i.JobseekerCover)
            #         print((i.JobseekerID).id)
            #         ids.append((i.JobseekerID).id)
            #
            #         # a[i]=Jobseeker.objects.all().filter(id=[i.JobseekerID.id])
            #         # item=Jobseeker.objects.all().filter(id__in=[i.JobseekerID.id])
            # print(ids)
            #
            # item=Jobseeker.objects.filter(id__in=ids)
            # print(item)
            return render(request, 'EmployerHome.html',{'item':ApplicantID,'username':username})
                # return render(request, 'JobseekerRegister.html')
        else:

            return render(request, 'Index.html')

    else:
        # messages.info(request,"user doesnot exist")
     return render(request, 'EmployerLogin.html')
def JobserkerLogin(request):
        print("here")
        print(request.method)
        if request.method == 'POST':
            print("here1")
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                jid = GetJobseekerId(request)

                items = JobApplication.objects.filter(JobseekerID=jid)
                print(items)
                return render(request, "Home.html", {'items': items,'username': username})

            else:
                return render(request, 'Index.html')
        else:

            return render(request, 'JobseekerLogin.html')

def logout(request):
   # return HttpResponse("hi")
    auth.logout(request)
    return render(request, 'Index.html')
def Jobapply(request,id):
    if request.method=='POST':
        JobStatus='submitted'
        JobseekerCover=request.POST['JobseekerCover']
        JobseekerResume = request.FILES['JobseekerResume']
        JobseekerID = GetJobseekerId(request)
        Empobj = JobListing.objects.filter(id=id)
        if len(Empobj) == 1:
            employerobj = Empobj[0]
        else:
            pass
        EmployerID = employerobj.id
        # if JobseekerResume.is_valid():
        Jobsubmit=JobApplication(EmployerID_id=EmployerID,JobseekerID_id=JobseekerID,JobListingID_id=id,JobseekerResume=JobseekerResume,JobStatus=JobStatus,JobseekerCover=JobseekerCover)
        Jobsubmit.save()
        return render(request, "Index.html")
    return render(request,"Jobapply.html",{'jobid':id})
def applicantview(request,id):
    if request.method == 'POST':
        print('here')
        items = JobApplication.objects.get(id=id)
        Status= request.POST['JobStatus']
        items.JobStatus=Status
        items.save()

    print(id)
    items = JobApplication.objects.filter(id=id)

    return render(request, "JobseekerDetails.html", {'items': items})
def logout(request):
   # return HttpResponse("hi")
    auth.logout(request)
    return render(request, 'index.html')
def JobList(request):

    # if request.method == 'POST':
    #     items = JobListing.objects.filter(id=id)
    #     return render(request, "JobDetails.html", {'items': items})
    EmployerID = GetEmployerId(request)
    items = JobListing.objects.all().filter(EmployerID=EmployerID)


    return render(request, "EmployerJobList.html", {'items': items})
def JobEdit(request,id):


    if request.method == 'POST':
        items = JobListing.objects.get(id=id)

        JobTitle = request.POST['JobTitle']
        JobDesc = request.POST['JobDesc']
        JobLocation = request.POST['JobLocation']
        JobCategory = request.POST['JobCategory']
        JobSalary = request.POST['JobSalary']
        Jobskill = request.POST['Jobskill']
        JobStatus = True
        items.JobTitle = JobTitle
        items.JobDesc = JobDesc
        items.JobLocation = JobLocation
        items.JobCategory = JobCategory
        items.JobSalary = JobSalary
        items.Jobskill = Jobskill
        items.JobStatus = JobStatus
        print(items.JobSalary)
        items.save()
        return render(request, "EmployerJobList.html")
    print(request.method)
    print(id)
    item = JobListing.objects.all().filter(id=id)
    print(item)
    return render(request, "JobDetails.html", {"items": item})

def JobDelete(request,id):
    items = JobApplication.objects.get(id=id)
    items.delete()
    return render(request, "EmployerJobList.html")







