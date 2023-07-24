from django.contrib import admin
from .models import Gender, Company, Movie

# Register your models here.
class GenderAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    
class CompanyAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class MovieAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')   
    list_display = ('pelicula', 'resumen', 'rating', 'premiere')     
    list_filter = ('genders', 'company')
    ordering = ('name', 'premiere')
    
admin.site.register(Gender, GenderAdmin)    
admin.site.register(Company, CompanyAdmin)    
admin.site.register(Movie, MovieAdmin)    