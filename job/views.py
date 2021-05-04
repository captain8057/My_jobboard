from django.shortcuts import render,redirect
from django.urls import reverse
from .models import *
from django.core.paginator import Paginator
from .form import applyform ,JobForm
from django.contrib.auth.decorators import login_required
from .filters import JobFilters
from accounts.decorators import allowedUsers,notLoggedUsers



# Create your views here.

def job_list(request):
    job_list = Job.objects.all()


    myfilter = JobFilters(request.GET,queryset=job_list)
    job_list = myfilter.qs

    paginator = Paginator(job_list, 5) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={'jobs': page_obj ,'myfilter':myfilter}
    return render(request,'job/job_list.html',context)


def home_page(request):
    job_list = Job.objects.all()
    cate= Category.objects.all()
    cate_num= Job.objects.filter(category__in=cate)
    # for cat in cate:
    #     cate_num= Job.objects.filter(category__exact=cat).count()

    print(cate_num)
    context={'job_list': job_list,'cate':cate , 'cate_num':cate_num }
    return render(request,'job/index.html',context)
    


def job_detail(request , id):
    job_detail = Job.objects.get(id=id)

    if request.method=='POST':
      form = applyform(request.POST ,request.FILES)
      if form.is_valid():
          myform =form.save(commit=False)
          myform.job= job_detail
          myform.save()


    else:
        form = applyform()
    context={'job': job_detail ,'form':form}
    return render(request,'job/job_detail.html',context)


@allowedUsers(allowedGroups=['Admin','Organisations'])
def add_job(request):
   if request.method=='POST':
       form = JobForm(request.POST ,request.FILES)
       if form.is_valid():
          myform =form.save(commit=False)
          myform.onwer= request.user
          myform.save()
          return redirect(reverse('joburl:job_list'))
   else:
       form =JobForm()


   return render(request,'job/add_job.html',{'form':form})



def like_or_unlike(request,id):
    job = Job.objects.get(id=id)

    if request.user in job.like.all():
        job.like.remove(request.user)
    
    else:
        job.like.add(request.user)
    
    return redirect(reverse('joburl:job_detailurl',kwargs={'id':job.id}))



def user_favourites(request):
    user_favourites = Job.objects.filter(like=request.user)
    return render(request,'accounts:profile',{'user_favourites':user_favourites})

