from django.contrib import admin

from .models import Cat, Dog
# Register your models here.


class DogAdmin(admin.ModelAdmin):
    class Meta:
        model = Dog


class CatAdmin(admin.ModelAdmin):
    class Meta:
        model = Cat


admin.site.register(Dog, DogAdmin)
admin.site.register(Cat, CatAdmin)