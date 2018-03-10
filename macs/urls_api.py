from rest_framework_nested import routers
from rest_framework.routers import DefaultRouter, SimpleRouter

from django.urls import re_path, include

from .views.api import MachinePermissionsView, MemberViewSet
from .views.api import LogViewSet, MachineViewSet, LocationViewSet

router = DefaultRouter()
# router.register(r'permissions', PermissionViewSet, base_name='permission')
router.register(r'members', MemberViewSet)

logRouter = SimpleRouter(router)
logRouter.register(r'logs', LogViewSet, base_name='log-entries')

machineRouter = SimpleRouter(router)
machineRouter.register('machine', MachineViewSet)

locationRouter = SimpleRouter(router)
locationRouter.register('location', LocationViewSet)

machine_permissions_router = routers.NestedSimpleRouter(router, r'members', lookup='member')
machine_permissions_router.register(r'machines', MachinePermissionsView, base_name='member-machines')

urlpatterns = [
    re_path(r'', include(router.urls)),
    re_path(r'', include(machine_permissions_router.urls)),
    re_path(r'', include(logRouter.urls)),
    re_path(r'', include(machineRouter.urls)),
    re_path(r'', include(locationRouter.urls)),
]
