from django.contrib import admin


from .models import Location, Machine, MemberPermission, Member
from .models.forms import MachineForm


class MachineInline(admin.StackedInline):
    model = Machine
    extra = 1
    form = MachineForm

class MachinePermissionInline(admin.TabularInline):
    model = MemberPermission
    extra = 1

class MemberAdmin(admin.ModelAdmin):
    fieldsets = [
    (None, {'fields': ['member_name']})]
    inlines = [MachinePermissionInline]

admin.site.register(Location)
admin.site.register(Machine)
admin.site.register(MemberPermission)
admin.site.register(Member, MemberAdmin)
