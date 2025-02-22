from django.contrib import admin

from .models import Question, Choice

admin.site.site_header = "Votes Administrator"
admin.site.site_title = "Votes Administrator Area"
admin.site.index_title = "Welcome to the Votes Administrator Area"

class ChoiceInLine(admin.TabularInline):
  model = Choice
  extra = 3

class QuestionAdmin(admin.ModelAdmin):
  fieldsets = [
    (None, {'fields' : ['question_text']}),
    ('Date Information', {'fields' : ['pub_date'], 'classes' : ['collapse']}),
  ]
  inlines = [ChoiceInLine]

'''admin.site.register(Question)
admin.site.register(Choice)'''

admin.site.register(Question, QuestionAdmin)