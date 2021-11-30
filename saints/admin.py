from django.contrib import admin
from .models import AccountabilityGroup, Activity, Case, Department, Fellowship, FellowshipImage, GateOneImage, HomeAltar, Leader, Saint, Attendance, Sunday_Service, Visitor, Report, AccountabilityLeader


class SaintAdmin(admin.ModelAdmin):

    list_display = ('name', 'phone', 'residence', "year", 'saint_level')
    search_fields = ['name', 'residence', 'year', 'stability', "saint_level"]
    list_filter = ['name', 'residence', 'year', 'stability', "saint_level"]


class ServiceAdmin(admin.ModelAdmin):

    list_display = ('report', 'date', "duration", )
    search_fields = ['report', 'date', "duration", "visitors"]
    list_filter = ['report', 'date', "duration", "visitors"]


class LeaderAdmin(admin.ModelAdmin):
    list_display = ('name', "department")
    search_fields = ['name', 'department']
    list_filter = ['name', 'department']


class ActivityAdmin(admin.ModelAdmin):

    list_display = ('name', 'date', 'duration', 'type')
    search_fields = ['name', 'date', 'type']


class FellowshipAdmin(admin.ModelAdmin):

    list_display = ('name', 'date', 'duration')
    search_fields = ['name', 'date']
    list_filter = ['name', 'date']


class AttendanceAdmin(admin.ModelAdmin):

    list_display = ('saint', 'fellowship')
    search_fields = ['saint', 'fellowship']
    list_filter = ['saint', 'fellowship']


class AccountabilityLeaderAdmin(admin.ModelAdmin):

    list_display = ('name', 'accountability_group', "contact")
    search_fields = ['name', "accountability_group"]
    list_filter = ['name', "accountability_group"]


class HomealtarAdmin(admin.ModelAdmin):
    list_display = ('name', 'Senior_Pastor', 'contact', 'region')
    search_fields = ['name', '', 'Senior_Pastor', 'contact']


class CaseAdmin(admin.ModelAdmin):
    list_display = ('name', 'ailment', 'age', 'residence', "gender")
    search_fields = ['name', 'ailment', 'age', 'residence', "gender"]


class VisitorAdmin(admin.ModelAdmin):

    list_display = ('name', 'date', 'fellowship',
                    'contact', 'interestedDepartment')
    search_fields = ['name', 'date', 'fellowship',
                     'contact', 'interestedDepartment']
    list_filter = ('name', 'date', 'fellowship',
                   'contact', 'interestedDepartment')


class CaseAdmin(admin.ModelAdmin):
    list_display = ('name', 'condition',
                    'contact', "residence", "age")
    search_fields = ['name', 'condition',
                     'contact', "residence", "age"]
    list_filter = ('name', 'condition',
                   'contact', "residence")


admin.site.register(Saint, SaintAdmin)
admin.site.register(Activity, ActivityAdmin)
admin.site.register(Attendance, AttendanceAdmin)
admin.site.register(Fellowship, FellowshipAdmin)
admin.site.register(Visitor, VisitorAdmin)
admin.site.register(Report)
admin.site.register(AccountabilityGroup)
admin.site.register(Department)
admin.site.register(HomeAltar, HomealtarAdmin)
admin.site.register(Leader, LeaderAdmin)
admin.site.register(Sunday_Service, ServiceAdmin)
admin.site.register(AccountabilityLeader, AccountabilityLeaderAdmin)
admin.site.register(GateOneImage)
admin.site.register(Case, CaseAdmin)
admin.site.register(FellowshipImage)
