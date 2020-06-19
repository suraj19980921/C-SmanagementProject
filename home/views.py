from django.shortcuts import render, redirect
from django.contrib.auth.models import auth, User
from .models import College
from django.core.paginator import Paginator , PageNotAnInteger ,EmptyPage
from django.http import JsonResponse
from django.core.serializers import serialize
from django.contrib.postgres.search import SearchVector



# Create your views here.

def login(request):
   
    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]

       

        user = auth.authenticate(username=username,password=password)
        
        if user is not None:
            auth.login(request,user)
            return redirect('home')
            
        else:
            message = "Invalid Username or password"
            return render(request,'login.html',{"messages":message})
        
    return render (request,'login.html')
         

def logout(request):

    auth.logout(request)
    return redirect('/')




    

def register(request):

    return render(request,'register.html')


def createAccount(request):

    if request.method == "POST":

        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]

        user = User.objects.create_user(first_name=first_name,
                                        last_name= last_name,
                                        username=username,
                                        password=password,email=email)
        
        user.save()
        return redirect('login')

    return redirect('register')

def home(request):
       
    all_colleges =  Paginator(College.objects.filter(user_id = request.user),3)
    
    page = request.GET.get('page')

    total_pages = all_colleges.num_pages

    
    try:
        colleges = all_colleges.page(page)

    except PageNotAnInteger:

        colleges = all_colleges.page(1) 

    except EmptyPage:
        colleges = all_colleges.page(total_pages)

    return render(request,'homepage.html',{"colleges":colleges,"total_pages":total_pages})


def collegeDetails(request):

    if request.method == "POST":

        colleges = Paginator(College.objects.filter(user_id = request.user),3)

        college_name = request.POST["college_name"]
        college_address = request.POST["college_address"]
        college_phone = request.POST["college_phone"]
        college_description = request.POST["college_description"]
        user = request.user

        college = College.objects.create(college_name=college_name,
                                         college_address=college_address,
                                         college_phone = college_phone,
                                         college_description= college_description,
                                         user= user)

        
        college.save()
    
    return redirect('/home?page='+str(colleges.num_pages))

    
def delete(request):    
  
    all_colleges =  Paginator(College.objects.filter(user_id = request.user),3)


    current_page = request.POST['currentPage']

    if int(current_page) > all_colleges.num_pages:

        current_page = current_page-1

    id = request.POST['deleteid']
    
    College.objects.get(id = id).delete()

    return redirect('/home?page='+str(current_page))


def fetch(request):

    college = College.objects.filter(id = request.GET['id'])

    colleges = serialize('json', college)

    return JsonResponse({"colleges":colleges})

def update(request):
 

    if request.method == "POST":
        
        college_id =  request.POST["collegeId"]
        college_name = request.POST["college_name"]
        college_address = request.POST["college_address"]
        college_phone = request.POST["college_phone"]
        college_description = request.POST["college_description"]
        
        current_page = request.POST['current_page']
 
    College.objects.filter(pk=college_id).update(college_name=college_name,
                                                      college_address=college_address,
                                                      college_phone = college_phone,
                                                      college_description= college_description)


    return redirect('/home?page='+str(current_page))
   
    
def search(request):

    #colleges = College.objects.filter(user_id = request.user.id)

    colleges = College.objects.annotate(search=SearchVector('college_name', 'college_address','college_phone','college_description')).filter(search='9873745976')

    colleges = serialize('json', colleges)

    return JsonResponse({"colleges":colleges})


