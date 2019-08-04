from django.apps import AppConfig

from django.conf import settings

from elasticsearch_dsl.connections import connections

class ElasticmodelsConfig(AppConfig):
    name = 'apps.elasticmodels'

    def ready(self):
        connections.configure(**settings.ELASTICSEARCH_DSL)
