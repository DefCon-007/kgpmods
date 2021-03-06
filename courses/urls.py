from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.search, name='course_home'),
    url(r'^([A-Z0-9]+)/edit$', views.edit, name='course_edit'),
    url(r'^([A-Z0-9]+)/json$', views.json, name='course_json'),
    url(r'^([A-Z0-9]+)$', views.index, name='course_index'),
    url(r'^compare$', views.compare, name='grade_compare'),
]
