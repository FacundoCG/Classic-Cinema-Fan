from django.contrib import admin
from django.db import models
from django.utils.html import format_html
from ckeditor.fields import RichTextField

# Create your models here.

class Gender(models.Model):
    name = models.CharField(max_length=100, verbose_name="Género")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "género"
        verbose_name_plural = "géneros"
        ordering = ["name"]
    def __str__(self):
        return self.name

class Company(models.Model):
    name = models.CharField(max_length=100, verbose_name="Compañía")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = "compañía"
        verbose_name_plural = "compañías"
        ordering = ["name"]
    def __str__(self):
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=100, verbose_name="Película")
    description = RichTextField(verbose_name="Resumen")
    RATING = [
        (1, "Vey bad"),
        (2, "Bad"),
        (3, "Mediocre"),
        (4, "Good"),
        (5, "Excellent"),
    ]    
    rating = models.PositiveSmallIntegerField(choices=RATING, verbose_name="Rating")
    genders = models.ManyToManyField(Gender, verbose_name="Géneros")
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name="Compañia")
    premiere = models.SmallIntegerField(verbose_name="Año de Estreno")
    image = models.ImageField(upload_to="movies", null=True, blank=True, verbose_name="Cover")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)    
    class Meta:
        verbose_name = "película"
        verbose_name_plural = "películas"
        ordering = ["-created"]
        
    def __str__(self):
        return self.name
    
    @admin.display(ordering='name')
    def pelicula(self):
        return format_html(
            '<span style="color: red;">{}</span>',
            self.name,
        )
    @admin.display(ordering='description')
    def resumen(self):
        return format_html(
            self.description
        )         