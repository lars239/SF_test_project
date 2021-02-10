from django.contrib import admin
from .models import Question, Test, Choice, Answer

admin.site.register(Question)
admin.site.register(Test)
admin.site.register(Choice)
admin.site.register(Answer)