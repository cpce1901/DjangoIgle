from django.urls import path
from .views import Login, Logout, UserTokenRefresh


urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('refresh-token/', UserTokenRefresh.as_view(), name='refresh_token')
]