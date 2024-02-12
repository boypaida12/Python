from django.contrib import admin
from .models import Course, ClassSchedule, ClassAttendance, Query, QueryComment
# Register your models here.

admin.site.register(Course)
admin.site.register(ClassSchedule)
admin.site.register(ClassAttendance)
admin.site.register(Query)
admin.site.register(QueryComment)

