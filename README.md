# django-cloud-models

Explore Amazon Elasticsearch 7.x with Django Elasticsearch DSL<br>

# Requirements

Running an Elasticsearch instance and config ELASTICSEARCH_DSL in settings.py
by default the host configuration is on http://localhost:9200<br>

Open the Django admin and insert some Houses/(Example model). Automatic
all admin insertion are indexing in the running Elasticserch instance below
an index name house_document.<br>

If you delete for some reason the documents from your Elasticsearch instance
you can indexing all the database using **python manage.py loadhouses**

You can review the indexing documents in the home site http://localhost:8000
