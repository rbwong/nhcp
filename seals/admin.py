from django.contrib import admin
from seals.models import Region, Province, LGU, SealInfo, SealProperty

class RegionAdmin(admin.ModelAdmin):
    list_display = ('name', 'name_fil', 'svg','date_created')


class ProvinceAdmin(admin.ModelAdmin):
    list_display = ('name', 'name_fil', 'date_created')


class LGUAdmin(admin.ModelAdmin):
    list_display = ('name', 'name_fil', 'description', 'description_fil', 'date_created')

class SealInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'name_fil', 'description', 'description_fil', 'date_created')

class SealPropertyAdmin(admin.ModelAdmin):
    list_display = ('name', 'name_fil', 'description', 'description_fil', 'date_created')


admin.site.register(Region, RegionAdmin)
admin.site.register(Province, ProvinceAdmin)
admin.site.register(LGU, LGUAdmin)
admin.site.register(SealProperty, SealPropertyAdmin)
admin.site.register(SealInfo, SealInfoAdmin)