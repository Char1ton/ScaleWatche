from django.contrib import admin
from .models import ScaleWatcher

# Register your models here.
class ScaleWatcherAdmin(admin.ModelAdmin):
    list_display=('title','description','line')

admin.site.register(ScaleWatcher,ScaleWatcherAdmin)
