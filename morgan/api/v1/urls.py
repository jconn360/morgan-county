from django.conf.urls import patterns, url, include
from rest_framework.routers import DefaultRouter
from morgan.api.v1.resources.identity import Identity


router = DefaultRouter(trailing_slash=False)

router.register(r'identities', Identity)

urlpatterns = router.urls

