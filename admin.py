from django.contrib import admin
from AdminApp.models import Category,Flight

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display=("cat_name",)
    
class FlightAdmin(admin.ModelAdmin):
    list_display=("name","description","price","way","ImageUrl","category")
     
    

admin.site.register(Category,CategoryAdmin)
admin.site.register(Flight,FlightAdmin)
