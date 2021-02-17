from django.contrib import admin

# Register your models here.
from .models import Question
from .models import Choice

class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']
    #fields = ['question_text', 'pub_date']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
