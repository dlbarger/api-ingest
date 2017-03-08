from django.contrib import admin
from app_model.models import ingest_configs

# Customize change list for ingest_configs
class AppModelAdmin(admin.ModelAdmin):
    list_display = ('data_source_name','data_source_descr')


# Register your models here.
admin.site.register(ingest_configs, AppModelAdmin)