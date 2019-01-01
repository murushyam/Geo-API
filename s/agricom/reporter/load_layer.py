import os
from django.contrib.gis.utils import LayerMapping
from .models import Counties



# Auto-generated `LayerMapping` dictionary for Counties model
counties_mapping = {
    'scalerank': 'SCALERANK',
    'natscale': 'NATSCALE',
    'labelrank': 'LABELRANK',
    'featurecla': 'FEATURECLA',
    'name': 'NAME',
    'namepar': 'NAMEPAR',
    'namealt': 'NAMEALT',
    'diffascii': 'DIFFASCII',
    'nameascii': 'NAMEASCII',
    'adm0cap': 'ADM0CAP',
    'capin': 'CAPIN',
    'worldcity': 'WORLDCITY',
    'megacity': 'MEGACITY',
    'sov0name': 'SOV0NAME',
    'sov_a3': 'SOV_A3',
    'adm0name': 'ADM0NAME',
    'adm0_a3': 'ADM0_A3',
    'adm1name': 'ADM1NAME',
    'iso_a2': 'ISO_A2',
    'note': 'NOTE',
    'latitude': 'LATITUDE',
    'longitude': 'LONGITUDE',
    'changed': 'CHANGED',
    'namediff': 'NAMEDIFF',
    'diffnote': 'DIFFNOTE',
    'pop_max': 'POP_MAX',
    'pop_min': 'POP_MIN',
    'pop_other': 'POP_OTHER',
    'rank_max': 'RANK_MAX',
    'rank_min': 'RANK_MIN',
    'geonameid': 'GEONAMEID',
    'meganame': 'MEGANAME',
    'ls_name': 'LS_NAME',
    'ls_match': 'LS_MATCH',
    'checkme': 'CHECKME',
    'max_pop10': 'MAX_POP10',
    'max_pop20': 'MAX_POP20',
    'max_pop50': 'MAX_POP50',
    'max_pop300': 'MAX_POP300',
    'max_pop310': 'MAX_POP310',
    'max_natsca': 'MAX_NATSCA',
    'min_areakm': 'MIN_AREAKM',
    'max_areakm': 'MAX_AREAKM',
    'min_areami': 'MIN_AREAMI',
    'max_areami': 'MAX_AREAMI',
    'min_perkm': 'MIN_PERKM',
    'max_perkm': 'MAX_PERKM',
    'min_permi': 'MIN_PERMI',
    'max_permi': 'MAX_PERMI',
    'min_bbxmin': 'MIN_BBXMIN',
    'max_bbxmin': 'MAX_BBXMIN',
    'min_bbxmax': 'MIN_BBXMAX',
    'max_bbxmax': 'MAX_BBXMAX',
    'min_bbymin': 'MIN_BBYMIN',
    'max_bbymin': 'MAX_BBYMIN',
    'min_bbymax': 'MIN_BBYMAX',
    'max_bbymax': 'MAX_BBYMAX',
    'mean_bbxc': 'MEAN_BBXC',
    'mean_bbyc': 'MEAN_BBYC',
    'compare': 'COMPARE',
    'gn_ascii': 'GN_ASCII',
    'feature_cl': 'FEATURE_CL',
    'feature_co': 'FEATURE_CO',
    'admin1_cod': 'ADMIN1_COD',
    'gn_pop': 'GN_POP',
    'elevation': 'ELEVATION',
    'gtopo30': 'GTOPO30',
    'timezone': 'TIMEZONE',
    'geonamesno': 'GEONAMESNO',
    'un_fid': 'UN_FID',
    'un_adm0': 'UN_ADM0',
    'un_lat': 'UN_LAT',
    'un_long': 'UN_LONG',
    'pop1950': 'POP1950',
    'pop1955': 'POP1955',
    'pop1960': 'POP1960',
    'pop1965': 'POP1965',
    'pop1970': 'POP1970',
    'pop1975': 'POP1975',
    'pop1980': 'POP1980',
    'pop1985': 'POP1985',
    'pop1990': 'POP1990',
    'pop1995': 'POP1995',
    'pop2000': 'POP2000',
    'pop2005': 'POP2005',
    'pop2010': 'POP2010',
    'pop2015': 'POP2015',
    'pop2020': 'POP2020',
    'pop2025': 'POP2025',
    'pop2050': 'POP2050',
    'cityalt': 'CITYALT',
    'min_zoom': 'min_zoom',
    'wikidataid': 'wikidataid',
    'wof_id': 'wof_id',
    'capalt': 'CAPALT',
    'name_en': 'NAME_EN',
    'name_de': 'NAME_DE',
    'name_es': 'NAME_ES',
    'name_fr': 'NAME_FR',
    'name_pt': 'NAME_PT',
    'name_ru': 'NAME_RU',
    'name_zh': 'NAME_ZH',
    'geom': 'MULTIPOINT',
}


county_shp = os.path .abspath(os.path.join(os.path.dirname(__file__),'data/ne_10m_populated_places.shp'))

def run(verbose=True):
    lm = LayerMapping(Counties, county_shp, counties_mapping, transform=False,encoding='iso-8859-1')
    lm.save(strict=True,verbose=verbose)
