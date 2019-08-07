# coding=UTF-8

from django.shortcuts import render
from django.views.generic import TemplateView
from apps.elasticmodels.documents import HouseDocument

class ElasticView(TemplateView):
    """
    View to review data from web
    """
    template_name="elasticmodels/elastic.html"

    def get_context_data(self, **kwargs):
        request = self.request
        context = super(ElasticView, self).get_context_data(**kwargs)

        # Search using wildcard
        # HouseDocument.search().query('wildcard', address__keyword="*Luyano*").execute()
        context.update({'all_houses': HouseDocument.search().execute(),
                         'all_red_houses': HouseDocument.search().query('term', color="red").execute()})

        return context


