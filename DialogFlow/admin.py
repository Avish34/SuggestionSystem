from django.contrib import admin
from .models import Suggestion,accuracy_db
# Register your models here.
admin.site.register(Suggestion)
admin.site.register(accuracy_db)
