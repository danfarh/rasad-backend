from django.contrib import admin
from .models import (
	Job,
    Resume
)


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    pass

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    pass


