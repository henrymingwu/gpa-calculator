from django.contrib import admin
from gpa_calculator.models import User, Schedule, Course

# class UserAdmin(admin.ModelAdmin):
#     list_display = ('name',)

# class CourseAdmin(admin.ModelAdmin):
#     list_display = ('course_name', 'schedule', 'units', 'grade')

# class ScheduleAdmin(admin.ModelAdmin):
#     list_display = ('user',)

admin.site.register(User)
admin.site.register(Course)
admin.site.register(Schedule)
