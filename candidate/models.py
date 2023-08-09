from django.db import models
from hr.models import JobPost , CandidateApplications
from django.contrib.auth.models import User
# Create your models here.


class MyApplyJobList(models.Model):
    user = models.OneToOneField(to=User,on_delete=models.CASCADE)
    job = models.ForeignKey(to=CandidateApplications,on_delete=models.CASCADE)
    dateYouApply = models.DateTimeField(auto_now_add=True)


class IsSortList(models.Model):
    user = models.ForeignKey(to=User,on_delete=models.CASCADE)
    job = models.OneToOneField(to=JobPost,on_delete=models.CASCADE)
    dateYouApply = models.DateTimeField(auto_now_add=True)
