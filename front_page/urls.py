from django.conf.urls import url
from . import views

app_name = 'front_page'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^excel_index/$', views.excel_index, name='excel_index'),
    url(r'^ml_index/$', views.ml_index, name='ml_index'),
]