"""Models registration for Admin"""
from django.contrib import admin
from .models import Material, Quiz, Answer, Question, Result

# Register your models here.
class AnswerInline(admin.TabularInline):
    model = Answer

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
admin.site.register(Quiz)
admin.site.register(Result)
admin.site.register(Material)
