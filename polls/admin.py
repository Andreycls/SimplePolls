from django.contrib import admin
from .models import Question, Choice

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 6
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
]
list_display = ('question_text', 'pub_date', 'was_published_recently')
inlines = [ChoiceInline]
admin.site.register(Question)
admin.site.register(Choice)


