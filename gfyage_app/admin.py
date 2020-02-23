from django.contrib import admin

# Register your models here.
from gfyage_app.models import Audio


class PostAdmin(admin.ModelAdmin):
    list_display = ['Title', 'Date']


admin.site.register(Audio, PostAdmin)
