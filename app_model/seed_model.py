###############################################################################
#   Script: seed_model.py
#   Author: Dennis Barger
#   Purpose:
#   - Load URL configurations into app_model.  Configurations represent the
#     metadata describing each API site identified for data ingestion.
#
#   class ingest_configs(models.Model):
#       data_source_name = models.CharField(max_length=60)
#       data_source_descr = models.CharField(max_length=254)
#       ingest_url = models.URLField()
#       ingest_type = models.IntegerField()
#       access_key_label = models.CharField(max_length=30)
#       access_key_value = models.CharField(max_length=254)
#       ingest_format = models.IntegerField()
###############################################################################

from app_model.models import ingest_configs

#   FDA Food Enforcement

r = ingest_configs(
    data_source_name = 'FDA Food Enforcement' ,
    data_source_descr = 'All food product recalls monitored by the FDA',
    ingest_url = 'http://download.open.fda.gov/food/enforcement/food-enforcement-0001-of-0001.json.zip',
    ingest_type = '3',
    access_key_label = 'api_key',
    access_key_value = '1osNHy9Jk90oZ3h7yXFlNBeiez0TPcicnIOvhpjF',
    ingest_format = '2'
)
r.save()

#   SDWIS Water System

r = ingest_configs(
    data_source_name = 'SDWIS Water System' ,
    data_source_descr = 'Inventory information on public water systems',
    ingest_url = 'https://iaspub.epa.gov/enviro/efservice/water_system',
    ingest_type = '2',
    access_key_label = 'NA',
    access_key_value = 'NA',
    ingest_format = '1'
)
r.save()

#   SDWIS Water System Facility

r = ingest_configs(
    data_source_name = 'SDWIS Water System Facility' ,
    data_source_descr = 'Inventory information on public water systems facilities',
    ingest_url = 'https://iaspub.epa.gov/enviro/efservice/water_system_facility/',
    ingest_type = '2',
    access_key_label = 'NA',
    access_key_value = 'NA',
    ingest_format = '1'
)
r.save()

#   SDWI Enforcement Action

r = ingest_configs(
    data_source_name = 'SDWIS Enforcement Action' ,
    data_source_descr = 'Enforcement actions taken against water systems, laboratories or operators',
    ingest_url = 'https://iaspub.epa.gov/enviro/efservice/enforcement_action/',
    ingest_type = '2',
    access_key_label = 'NA',
    access_key_value = 'NA',
    ingest_format = '1'
)
r.save()

#   SDWIS Violation

r = ingest_configs(
    data_source_name = 'SDWIS Violation' ,
    data_source_descr = 'Documents a breach of a SDWIS requirements',
    ingest_url = 'https://iaspub.epa.gov/enviro/efservice/violation',
    ingest_type = '2',
    access_key_label = 'NA',
    access_key_value = 'NA',
    ingest_format = '1'
)
r.save()

#   SDWIS Violation Event

r = ingest_configs(
    data_source_name = 'OSHA Violation Event' ,
    data_source_descr = 'Information about OSHA violation events and penalties',
    ingest_url = 'https://data.dol.gov/get/violation_event/',
    ingest_type = '1',
    access_key_label = 'X-API-KEY',
    access_key_value = '540161ce-f20a-45ec-b147-2fd27ae365ad',
    ingest_format = '2'
)
r.save()

#   OSHA Violation

r = ingest_configs(
    data_source_name = 'OSHA Violation' ,
    data_source_descr = 'OSHA violations that are in violation of the Act, Executive Order 12196, or 29 CFR Part 1960.',
    ingest_url = 'https://data.dol.gov/get/violation',
    ingest_type = '1',
    access_key_label = 'X-API-KEY',
    access_key_value = '540161ce-f20a-45ec-b147-2fd27ae365ad',
    ingest_format = '2'
)
r.save()

#   OSHA Inspection

r = ingest_configs(
    data_source_name = 'OSHA Inspection' ,
    data_source_descr = 'OSHA inspections conducted by OSHA compliance safety and health officers.',
    ingest_url = 'https://data.dol.gov/get/inspection/',
    ingest_type = '1',
    access_key_label = 'X-API-KEY',
    access_key_value = '540161ce-f20a-45ec-b147-2fd27ae365ad',
    ingest_format = '2'
)
r.save()

#   OSHA Fatalities

r = ingest_configs(
    data_source_name = 'OSHA Fatalities' ,
    data_source_descr = 'Fatalities related to OSHA violation events.',
    ingest_url = 'http://api.dol.gov/V1/Safety/Fatalities',
    ingest_type = '1',
    access_key_label = 'X-API-KEY',
    access_key_value = '540161ce-f20a-45ec-b147-2fd27ae365ad',
    ingest_format = '2'
)
r.save()




