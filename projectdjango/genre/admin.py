from django.contrib import admin
# Register your models here.

from . models import Collection, Piece

admin.site.register(Collection)
admin.site.register(Piece)