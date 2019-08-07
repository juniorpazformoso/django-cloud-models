# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand

from django.conf import settings

from apps.elasticmodels.models import House
from apps.elasticmodels.documents import ESHouse

class Command(BaseCommand):
    help = 'Load data from Cleanoperation model'

    
    def handle(self, *args, **options):
        total_records = 0
        success_records = 0
        fail_records = 0
        count_cache = 1

        houses = House.objects.all()
        count_houses = houses.count()
        documents = list()

        for house in houses:
            total_records += 1
            try:
                documents.append(house)
                if count_cache == 2:
                    if(len(documents) > 0):
                        ESHouse.indexing_house(documents)
                        documents = list()
                        count_cache = 0

                count_cache += 1
                success_records += 1

            except Exception as e:
                print(e)
                self.stdout.write(e)
                fail_records += 1
                continue

        if(len(documents) > 0):
            ESHouse.indexing_house(documents)
        print("ALL GOOD")