import pandas as pd
from .models import MobileShop
from django.utils.dateparse import parse_datetime

def import_csv(csv_file):
    data = pd.read_csv(csv_file)
    for _, row in data.iterrows():
        MobileShop.objects.update_or_create(
            osm_id=row['osm_id'],
            defaults={
                'shop': row['shop'],
                'name': row['name'],
                'addr_housenumber': row['addr-housenumber'],
                'addr_street': row['addr-street'],
                'addr_city': row['addr-city'],
                'addr_postcode': row['addr-postcode'],
                'the_geom': row['the_geom'],
                'osm_original_geom': row['osm_original_geom'],
                'osm_type': row['osm_type']
            }
        )

import_csv('C:/Users/Meryem/Documents/Projet_Django_PriceHub_M1/Projet_Django_PriceHub_M1/Price-Hub-master/PHUb/data8_filtre.csv')
