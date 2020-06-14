from django.shortcuts import render, redirect
from django.contrib.auth.models import auth, User
from .models import Staff
from django.core.paginator import Paginator , PageNotAnInteger ,EmptyPage
from django.http import JsonResponse
from django.core.serializers import serialize
from django.contrib.postgres.search import SearchVector



# Create your views here



def staff(request):
       
    college_id = request.GET['staff']
    
    all_staff =  Paginator(Staff.objects.filter(college_id = college_id),3)
    
    page = request.GET.get('page')

    total_pages = all_staff.num_pages

    
    try:
        staff = all_staff.page(page)

    except PageNotAnInteger:

        staff = all_staff.page(1) 

    except EmptyPage:
        staff = all_staff.page(total_pages)
        

    return render(request,'staff.html',{"staff":staff,"total_pages":total_pages,"college_id":college_id})


def staffDetails(request):

    if request.method == "POST":

        college_id = request.POST['college_id']

        all_staff = Paginator(Staff.objects.filter(college_id = college_id),3)

        staff_name = request.POST["staff_name"]
        staff_address = request.POST["staff_address"]
        staff_phone = request.POST["staff_phone"]
        staff_description = request.POST["staff_description"]
        

        staff = Staff.objects.create(staff_name=staff_name,
                                         staff_address=staff_address,
                                         staff_phone = staff_phone,
                                         staff_description= staff_description,
                                         college_id = college_id)

        
        staff.save()
    
    return redirect('/college/staff/staffinfo?page='+str(all_staff.num_pages)+'&staff='+str(college_id))

    
def delete(request):    
  
    all_staffs =  Paginator(staff.objects.filter(user_id = request.user),3)


    current_page = request.POST['currentPage']

    if int(current_page) > all_staffs.num_pages:

        current_page = current_page-1

    id = request.POST['deleteid']
    
    staff.objects.get(id = id).delete()

    return redirect('/home?page='+str(current_page))


def fetch(request):

    staff = staff.objects.filter(id = request.GET['id'])

    staffs = serialize('json', staff)

    return JsonResponse({"staffs":staffs})

def update(request):
 

    if request.method == "POST":
        
        staff_id =  request.POST["staffId"]
        staff_name = request.POST["staff_name"]
        staff_address = request.POST["staff_address"]
        staff_phone = request.POST["staff_phone"]
        staff_description = request.POST["staff_description"]
        
        current_page = request.POST['current_page']
 
    staff.objects.filter(pk=staff_id).update(staff_name=staff_name,
                                                      staff_address=staff_address,
                                                      staff_phone = staff_phone,
                                                      staff_description= staff_description)


    return redirect('/home?page='+str(current_page))
   
    
def search(request):

    #staffs = staff.objects.filter(user_id = request.user.id)

    staffs = staff.objects.annotate(search=SearchVector('staff_name', 'staff_address','staff_phone','staff_description')).filter(search='9873745976')

    staffs = serialize('json', staffs)

    return JsonResponse({"staffs":staffs})



