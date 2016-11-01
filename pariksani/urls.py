from django.conf.urls import url

from pariksani.views import views

urlpatterns = [
    url(r'', views.HomeView.as_view()),
    url(r'^about/', views.AboutView.as_view()),
]