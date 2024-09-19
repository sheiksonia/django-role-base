from django.shortcuts import render,redirect,get_object_or_404
from myApp.models import*
from  django.http import HttpResponse
from django.contrib.auth.decorators import login_required
#buid-in user
from django.contrib.auth import authenticate,login,logout

@login_required
def homepage(req):
    return render(req,'common/home.html')
def loginpage(req):
    if req.method=='POST':
        username=req.POST.get("username")
        password=req.POST.get("password")
        user=authenticate(username=username,password=password)
        if user:
            login(req,user)
            return redirect("homepage")
           
        else:
            return HttpResponse("user is  not valid")
    return render(req,'common/loginPage.html')

def signup_view(req):
    if req.method=='POST':
        username=req.POST.get("username")
        email=req.POST.get("email")
        usertype=req.POST.get("usertype")
        password=req.POST.get("password")
        confirm_password=req.POST.get("confirm_password")

        if password==confirm_password:
            
            user=customUser.objects.create_user(
                username=username,
                email=email,
                usertype=usertype,
                password=password

            )
            return redirect("loginpage")
    
    return render(req,'common/signupPage.html')
def logoutpage(req):
    logout(req)
    return  redirect("loginpage")

def addskillpage(req):
    if req.user.usertype =='admin':
        return render(req,"myAdmin/addskillpage.html")
    else:
        return HttpResponse("authorized is not access this page")  


def addeducation(req):
    if req.user.usertype =='admin':
        return render(req,"myAdmin/addeducation.html")
    else:
        return HttpResponse("authorized is not access this page")



def addinterest(req):
    if req.user.usertype =='admin':
        return render(req,"myAdmin/addinterert.html")
    else:
        return HttpResponse("authorized is not access this page") 

def addlanguage(req):
    if req.user.usertype =='admin':
        return render(req,"myAdmin/addlanguage.html")
    else:
        return HttpResponse("authorized is not access this page")

def createresume(req):
    if req.user.usertype =='viewer':
       current_user=req.user
       if req.method=='POST':
           resume, created=ResumeModel.objects.get_or_create(user=current_user)
               
           resume.Contact_Number=req.POST.get("contact_number"),
           resume.Designation=req.POST.get("designation"),
           resume.Carer_Summary=req.POST.get("career_summary"),
           resume.age=req.POST.get("age"),
           resume.gender=req.POST.get("gender"),
           resume.Profile_pic=req.FILES.get("profile_pic")
           
           resume.save()


            
           current_user.first_name=req.POST.get("first_name")
           current_user.last_name=req.POST.get("last_name")

           current_user.save()

       return render(req,'myAdmin/createresume.html')
    else:
        return HttpResponse("authorized is not access this page") 


def profilepage(req):
    current_user = req.user
    information = get_object_or_404(ResumeModel, user=current_user)
    context={
            'information':information
    }
        
     
    return render(req,'myAdmin/profilepage.html',context)               