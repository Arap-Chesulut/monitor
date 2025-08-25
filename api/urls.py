# api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CountyViewSet, AnalysisRequestViewSet, ExportRequestViewSet

router = DefaultRouter()
router.register(r'counties', CountyViewSet)
router.register(r'analysis', AnalysisRequestViewSet)
router.register(r'exports', ExportRequestViewSet)

urlpatterns = [
    path('', include(router.urls)),
]