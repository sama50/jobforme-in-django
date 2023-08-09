from django.contrib import admin
from hr import models
# Register your models here.


@admin.register(models.Hr)
class HrAdmin(admin.ModelAdmin):
    list_display = ('id','user')

@admin.register(models.JobPost)
class JobPostAdmin(admin.ModelAdmin):
    list_display = ('id','user','title','address','compnayName','salaryLow','salaryHigh','lastDateToApply','applyCount')

@admin.register(models.CandidateApplications)
class CandidateApplicationsAdmin(admin.ModelAdmin):
    list_display = ('id','user','job')

@admin.register(models.SelectCandidateJob)
class SelectCandidateJobAdmin(admin.ModelAdmin):
    list_display = ('id','job','candidate')