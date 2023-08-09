from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from hr.models import JobPost , CandidateApplications
from candidate.models import MyApplyJobList
# Create your views here.

@login_required
def candidateHome(request):
    jobpost = JobPost.objects.all()
    return render(request,'candidate/dashboradh.html',{'jobpost':jobpost})

@login_required
def applyJob(request,id):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        college = request.POST.get('college')
        passing_year = request.POST.get('passing_year')
        yearOfExperience = request.POST.get('yearOfExperience')
        resume = request.FILES.get('resume')
        job = JobPost.objects.get(id=id)
        if CandidateApplications.objects.filter(user=request.user,job=job).exists():
            return redirect('dash')
        CandidateApplications(user=request.user,job=job,passingYear=passing_year,yearOfExperience=yearOfExperience,resume=resume).save()
        return redirect('dash')
    return render(request,'candidate/apply.html')

@login_required
def myjoblist(request):
    joblist = MyApplyJobList.objects.filter(user=request.user)
    return render(request,'candidate/myjoblist.html',{'joblist':joblist})

