from django.contrib import admin
from .models import Score, DefaultSetting

# Register your models here.
admin.site.register(Score)

@admin.register(DefaultSetting)
class DefaultSettingAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'eqArr',
        'allowedOperators',
        'negativeAnswerAllowed',
        'canExceedTen'
    )