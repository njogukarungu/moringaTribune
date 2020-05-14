from django.contrib import admin
from .models import Editor,Article, tags

class AdminArticle(admin.ModelAdmin):
    filter_horizontal = ('tags',)

admin.site.register(Editor)
admin.site.register(tags)
admin.site.register(Article, AdminArticle)
