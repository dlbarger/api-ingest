from django.db import models

# Create your models here.
class ingest_configs(models.Model):
    data_source_name = models.CharField(max_length=60)
    data_source_descr = models.CharField(max_length=254)
    ingest_url = models.URLField()
    ingest_type = models.IntegerField()
    access_key_label = models.CharField(max_length=30)
    access_key_value = models.CharField(max_length=254)
    ingest_format = models.IntegerField()

#   def __str__(self):
# 		return self.data_source_name