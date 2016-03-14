from django.db import models
from django.utils.translation import ugettext_lazy as _

class Store(models.Model):
    store_name = models.CharField(_('Stores'),max_length=128,help_text ='Store name')

    def __unicode__(self):
        return self.store_name

class Product(models.Model):
    
    name = models.CharField(_("Products"),max_length=512)
    price = models.FloatField(_("Price"),)
    availabilty = models.BooleanField(default=False)
    stock = models.IntegerField(_("Stock"),default=0)
    
    def __unicode__(self):
        return self.name

class StoreMapping(models.Model):
    store = models.ForeignKey(Store)
    merchant_id = models.CharField(_("Merchant ID"),max_length=16)
    
    def __unicode__(self):
        return self.merchant_id

class ArticleMapping(models.Model):
    product = models.ForeignKey(Product)
    article_id = models.CharField(_("Article ID"),max_length=16)            