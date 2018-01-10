from django.conf.urls import url, include
from . import views

app_name = 'shortener'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<short_id>\w+)$', views.redirect_original, name='redirect')
]