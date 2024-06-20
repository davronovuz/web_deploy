from django.contrib import admin
from .models import New,Category,Contact


class NewsAdmin(admin.ModelAdmin):
    list_display = ["title","category","status"]
    list_filter = ["publish_time","status"]
    search_fields = ["title","body"]
    prepopulated_fields = {"slug":("title",)}



class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id","name"]


class ContactAdmin(admin.ModelAdmin):
    list_display = ["id","name","email"]


admin.site.register(New,NewsAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Contact,ContactAdmin)

