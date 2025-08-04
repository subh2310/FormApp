from django.urls import path
from formapi.views import home, candidate_detail
urlpatterns = [
    path('', home, name='home'),
    path('candidate/<int:pk>', candidate_detail, name='candidate_detail'),
]
