from django.urls import include, path
from rest_framework import routers
from api import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'data', views.UserDataView)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('auth/', views.CustomObtainAuthToken.as_view()),
    path('register/', views.RegisterAPI.as_view()),
    path('logout/', views.userLogout),
]