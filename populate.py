import os
from datetime import datetime, timedelta

def populate():
    region1 = add_region(name='Region 1')
    region2 = add_region(name='Region 2')
    region3 = add_region(name='Region 3')
    region4A = add_region(name='Region 4A')
    region4B = add_region(name='Region 4B')
    region5 = add_region(name='Region 5')
    region6 = add_region(name='Region 6')
    region7 = add_region(name='Region 7')
    region8 = add_region(name='Region 8')
    region9 = add_region(name='Region 9')
    region10 = add_region(name='Region 10')
    region11 = add_region(name='Region 11')
    region12 = add_region(name='Region 12')
    region13 = add_region(name='Region 13')
    NCR = add_region(name='NCR')
    CAR = add_region(name='CAR')
    ARMM = add_region(name='ARMM')

    add_province(name='Basilan', region=ARMM)
    add_province(name='Lanao del Sur', region=ARMM)
    add_province(name='Maguindanao', region=ARMM)
    add_province(name='Sulu', region=ARMM)
    add_province(name='Tawi Tawi', region=ARMM)

    add_province(name='Abra', region=CAR)
    add_province(name='Apayao', region=CAR)
    add_province(name='Benguet', region=CAR)
    add_province(name='Ifugao', region=CAR)
    add_province(name='Kalinga', region=CAR)
    add_province(name='Mountain Province', region=CAR)

    add_province(name='Makati', region=NCR)

    add_province(name='Ilocos Sur', region=region1)
    province = add_province(name='Ilocos Norte', region=region1)
    add_province(name='Pangasinan', region=region1)
    add_province(name='La Union', region=region1)


    add_LGU(name='Bangui', province=province)
    add_LGU(name='Currimao', province=province)
    add_LGU(name='Dingras', province=province)
    add_LGU(name='Paoay', province=province)
    add_LGU(name='Pasuquin', province=province)
    add_LGU(name='Piddig', province=province)
    add_LGU(name='Pinli', province=province)

    print 'Generated Initial contents'

def add_region(name):
    region = Region.objects.get_or_create(name=name)[0]
    return region

def add_province(name, region):
    province = Province.objects.get_or_create(name=name, region=region)[0]
    return province

def add_LGU(name, province):
    lgu = LGU.objects.get_or_create(name=name, province=province)[0]
    return lgu

# Start execution here!
if __name__ == '__main__':
    print "Starting User population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nhcp.settings')
    from django.contrib.auth.models import User
    from seals.models import Region, Province, LGU
    populate()