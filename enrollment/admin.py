from django.contrib import admin

from . import models


class SubjectInline(admin.TabularInline):
    model = models.Student.subjects.through


class StudentInline(admin.TabularInline):
    model = models.Subject.students.through


class StudentAdmin(admin.ModelAdmin):
    search_fields = ['name']
    inlines = [
        SubjectInline
    ]


class SubjectAdmin(admin.ModelAdmin):
    search_fields = ['code', 'title']
    inlines = [
        StudentInline
    ]


class StudentSubjectAdmin(admin.ModelAdmin):
    list_select_related = True
    search_fields = ['student__name', 'subject__code', 'subject__title']


admin.site.register(models.Student, StudentAdmin)
admin.site.register(models.Subject, SubjectAdmin)
admin.site.register(models.StudentSubject, StudentSubjectAdmin)
