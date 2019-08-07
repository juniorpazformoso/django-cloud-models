# -*- coding: utf-8 -*-

from django_elasticsearch_dsl import Index, fields
from django_elasticsearch_dsl.documents import DocType
from elasticsearch_dsl.field import Double
from apps.elasticmodels.models import House
from django.conf import settings

from elasticsearch_dsl.connections import connections
from elasticsearch.helpers import bulk
from django.conf import settings
import sys
import traceback

from django.conf import settings


es_Index = Index(settings.HOUSE_INDEX)

@es_Index.doc_type
class HouseDocument(DocType):
    # address = fields.ObjectField(properties={
    #          'pk': fields.IntegerField(),
    #          'address': fields.StringField(),
    #      })

    class Django:
        model = House


class ESHouse():
    @staticmethod
    def indexing_house(documents):
        try:
            bulk(connections.get_connection(), actions=(ESHouse.indexing(d) for d in documents))
        except Exception as e:
            print(traceback.format_exc())
            sys.stdout.write(traceback.format_exc())


    @staticmethod
    def indexing(house):
        house_doc = HouseDocument(meta={'id': house.pk})
        house_doc.address = house.address
        house_doc.color = house.color
        house_doc.price = house.price
        #house_doc.address = {'pk': house.address.pk,
        #                     'address': house.address.address}

        house_doc.save(index="house_document")
        dict_to_bulk = house_doc.to_dict(include_meta=True)
        # If you send _version to Elasticsearch 7.x the rocket explode :(
        del dict_to_bulk['_version'] # Delete _version to successfully launch rocket :)
        return dict_to_bulk

