from django.contrib import admin
from school.models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'Name', 'Surname')
    list_display_links = ('id', 'Name')
    search_fields = ('Name',)


admin.site.register(Student, StudentAdmin)
