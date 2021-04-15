from django.contrib import admin

# Register your models here.
from .models import Question, Choice

class QuestionAdmin_0(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']

class QuestionAdmin_1(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 2

class ChoiceInline_1(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

    list_display = ('question_text', 'pub_date')

    list_filter = ['pub_date']

    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
