# coding=UTF-8

from django.conf.urls import url
from apps.elasticmodels.views import ElasticView

urlpatterns = [
    url(r'^', ElasticView.as_view(), name="elastic_view")
]
