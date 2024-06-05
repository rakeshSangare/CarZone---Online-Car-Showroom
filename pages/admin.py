from django.contrib import admin
from pages.models import Team
from django.utils.html import format_html

# Register your models here.
class TeamAdmin(admin.ModelAdmin):

    def thumbnail(self,object):
        return format_html('<img src="{}" width="40" style="border-radius:50px" />'.format(object.photo.url))

    thumbnail.short_description = 'photo'

    list_display = ('id','thumbnail' ,'firstName','lastName','designation')
    list_display_links =('id','thumbnail','firstName')
    search_fields = ('firstName','lastName')
    list_filter =('designation',)

admin.site.register(Team,TeamAdmin)