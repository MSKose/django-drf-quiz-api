'''
For the Inline TabularInline admin model used here see the ref here: https://docs.djangoproject.com/en/4.1/ref/contrib/admin/#inlinemodeladmin-objects

The admin interface has the ability to edit models on the same page as a parent model with the use of TabularInline. These are called inlines. So for 
our case down below, we linked answer to question so whenever we go to amdin page of question we'll be able add the answers there as well.
'''



from django.contrib import admin
from .models import Category, Quizzes, Answer, Question

@admin.register(Category) #! @admin.register(<Modelname>) does exactly thr same thing as admin.site.register(<Modelname>)

class CatAdmin(admin.ModelAdmin):
	list_display = [      #! list_display controls which fields are to be displayed 
        'name',
        ]

@admin.register(Quizzes)

class QuizAdmin(admin.ModelAdmin):
	list_display = [
        'id', 
        'title',
        ]

class AnswerInlineModel(admin.TabularInline):
    model = Answer
    fields = [
        'answer_text', 
        'is_right'
        ]

@admin.register(Question)

class QuestionAdmin(admin.ModelAdmin):
    fields = [
        'title',
        'quiz',
        ]
    list_display = [
        'title', 
        'quiz',
        'date_updated'
        ]
    inlines = [
        AnswerInlineModel, 
        ] 

@admin.register(Answer)

class AnswerAdmin(admin.ModelAdmin):
    list_display = [
        'answer_text', 
        'is_right', 
        'question'
        ]