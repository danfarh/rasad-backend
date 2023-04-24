from django.contrib import admin
from .models import (Question,Answer)

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_filter = ('title','text','confirm')
    search_fields = ('title','text','confirm')
    list_display = (
        'user',
        'title',
        'text',
        'confirm'
    )

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_filter = ('question__title','text','confirm')
    search_fields = ('text','confirm')
    list_display = (
        'question',
        'text',
        'confirm'
    ) 
