from django.urls import path
from . import views
urlpatterns = [

    path('',views.index,name='index'),
    path('Register/', views.Register, name='Register'),
    path('EmpRegister/', views.EmpRegister, name='EmpRegister'),
    path('JobRegister/', views.JobRegister, name='JobRegister'),
    path('JobSearch/', views.JobSearch, name='JobSearch'),

    path('EmpLogin/', views.EmpLogin, name='EmpLogin'),
    path('JobserkerLogin/', views.JobserkerLogin, name='JobserkerLogin'),
    path('Jobapply/<int:id>', views.Jobapply, name='Jobapply'),
    path('applicantview/<int:id>', views.applicantview, name='applicantview'),
    path('logout/',views.logout,name='logout'),

    path('JobList/', views.JobList, name='JobList'),
    path('JobEdit/<int:id>', views.JobEdit, name='JobEdit'),
    path('JobDelete/<int:id>', views.JobDelete, name='JobDelete'),


]