from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings

# class Address(models.Model):
#     number = models.IntegerField()
#     address = models.CharField(max_length=200)


class House(models.Model):
    """
    Models House
    """
    color = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=12, decimal_places=4)
    address = models.CharField(max_length=200)
    # address = models.ForeignKey(Address, on_delete=True)

    def __str__(self):
        return self.address


@receiver(post_save, sender=House, dispatch_uid="index_house")
def house_document(sender, instance, created, **kwargs):
    """
    Used signal to index documents. This signal perform created and update action
    You can extends this to support delete actions
    """
    from apps.elasticmodels.documents import ESHouse
    ESHouse.indexing(instance)
    
    