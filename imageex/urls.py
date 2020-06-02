from django.urls import path
from .views import MyModelView
from django.conf.urls import url

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'imagepath', MyModelView, basename='imagepath')
urlpatterns = router.urls