from django.contrib import admin


from .models import Location, Machine, MemberPermission, Member
from .models.log import InvalidRequest, MachineLock, MachineUnlock, Log
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
    (None, {'fields': ['member_name', 'member_id']})]
    inlines = [MachinePermissionInline]

class MachineLockAdmin(admin.ModelAdmin):
 	list_display = ('machine.description', 'member.name', 'timestamp')

class MachineUnlockAdmin(admin.ModelAdmin):
 	list_display = ('machine', 'member', 'timestamp')

admin.site.register(Location)
admin.site.register(Machine)
admin.site.register(MemberPermission)
admin.site.register(Member, MemberAdmin)
admin.site.register(InvalidRequest)
admin.site.register(MachineLock, MachineLockAdmin)
admin.site.register(MachineUnlock, MachineUnlockAdmin)
