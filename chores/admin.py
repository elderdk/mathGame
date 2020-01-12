from django.contrib import admin
from .models import Chore, ChoreLog

# Register your models here.
admin.site.register(Chore)

@admin.register(ChoreLog)
class ChoreLogAdmin(admin.ModelAdmin):
    list_display = (
    'user_did',
    'chore_name',
    'done_time'
    )