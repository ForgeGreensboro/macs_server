from rest_framework_nested import routers
from rest_framework.routers import DefaultRouter

from django.urls import re_path, include

from .views import MachineView, MemberViewSet

router = DefaultRouter()
# router.register(r'permissions', PermissionViewSet, base_name='permission')
router.register(r'members', MemberViewSet)

machines_router = routers.NestedSimpleRouter(router, r'members', lookup='member')
machines_router.register(r'machines', MachineView, base_name='member-machines')

urlpatterns = [
    re_path(r'^', include(router.urls)),
    re_path(r'^', include(machines_router.urls))
]
