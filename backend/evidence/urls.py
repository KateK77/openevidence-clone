from django.urls import path
from drf_spectacular.views import SpectacularAPIView

from . import views as v

urlpatterns = [
    path('api/health/', v.health),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/session/', v.session),
    path('api/register/', v.register),
    path('api/login/', v.sign_in),
    path('api/logout/', v.sign_out),
    path('api/profile/', v.profile),
    path('api/settings/', v.preferences),
    path('api/conversations/', v.conversations),
    path('api/conversations/<int:pk>/', v.conversation),
    path('api/ask/', v.ask),
    path('api/answers/<int:pk>/', v.answer),
    path('api/answers/<int:pk>/save/', v.save_answer),
    path('api/answers/<int:pk>/export/<str:kind>/', v.download),
    path('api/saved-answers/', v.saved_answers),
    path('api/articles/', v.articles),
    path('api/articles/<str:identifier>/', v.article),
    path('api/articles/<str:identifier>/save/', v.save_article),
    path('api/saved-articles/', v.saved_articles),
]
