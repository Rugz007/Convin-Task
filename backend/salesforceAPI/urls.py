from django.urls import path
from .views import *

urlpatterns = [
    path('authorize',MatchesViewSet.as_view({'get':'authorize'}),name='authorize'),
    path('callback',MatchesViewSet.as_view({'get':'authenticate'}),name='authenticate')
]
