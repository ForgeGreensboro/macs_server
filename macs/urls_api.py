from rest_framework_nested import routers
from rest_framework.routers import DefaultRouter, SimpleRouter

from django.urls import re_path, include

from .views.api import MachineView, MemberViewSet, LogViewSet

router = DefaultRouter()
# router.register(r'permissions', PermissionViewSet, base_name='permission')
router.register(r'members', MemberViewSet)

logRouter = SimpleRouter(router)
logRouter.register(r'logs', LogViewSet, base_name='log-entries')

machines_router = routers.NestedSimpleRouter(router, r'members', lookup='member')
machines_router.register(r'machines', MachineView, base_name='member-machines')

urlpatterns = [
    re_path(r'', include(router.urls)),
    re_path(r'', include(machines_router.urls)),
    re_path(r'', include(logRouter.urls))
]
