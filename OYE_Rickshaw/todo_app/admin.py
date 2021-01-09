from django.contrib import admin

from . import models


@admin.register(models.TODO)
class TODOAdmin(admin.ModelAdmin):
	list_display = ('title', 'description', 'state', 'priority', 'date', 'id')
	search_fields = ('title', 'state', 'priority', 'date')
	list_filter = ('state', 'priority')
