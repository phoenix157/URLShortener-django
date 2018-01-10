from django.contrib import admin
from .models import ShortURL

# Register your models here.
class ShortUrlAdmin(admin.ModelAdmin):
    list_display = ('url', 'code', 'timestamp')

admin.site.register(ShortURL, ShortUrlAdmin)