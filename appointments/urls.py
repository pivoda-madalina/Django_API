from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('appointments', views.AppointmentView)
router.register('clients', views.ClientView)

urlpatterns = [
    path('', include(router.urls)),
]
