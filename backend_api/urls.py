from django.urls import path, include
from rest_framework.routers import DefaultRouter

from backend_api import views


class OptionalSlashRouter(DefaultRouter):
    def __init__(self, *args, **kwargs):
        super(DefaultRouter, self).__init__(*args, **kwargs)
        self.trailing_slash = '/?'


router = OptionalSlashRouter()
router.register('foi', views.FieldOfInterestViewSet, basename='field_of_interest')
router.register('teacher', views.TeacherViewSet, basename='teacher')
router.register('presenter', views.PresenterViewSet, basename='presenter')
router.register('workshop', views.WorkshopViewSet, basename='workshop')
router.register('presentation', views.PresentationViewSet, basename='presentation')
router.register('misc', views.MiscViewSet, basename='misc')

urlpatterns = [
    path('', include(router.urls)),
    path('user/', views.UserAPIView.as_view()),
    path(r'user/<pk>/', views.UserAPIView.as_view()),
    path('payment/', views.PaymentAPIView.as_view()),
]
