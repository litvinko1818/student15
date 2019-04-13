from django.contrib import admin
from .models import Video, Comment


class InlineComment(admin.StackedInline):
    model = Comment
    extra = 2
    readonly_fields = ['like']


class VideoAdmin(admin.ModelAdmin):
    readonly_fields = ['like', 'dislike']
    inlines = [InlineComment]

admin.site.register(Video, VideoAdmin)
# Register your models here.
