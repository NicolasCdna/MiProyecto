from django.contrib import admin

from .models import Vehiculo
from .models import Version
from .models import Proxy
# Register your models here.

admin.site.register(Vehiculo)


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('version_codif', 'version_extend', 'mercado')
    search_fields = ('version_codif', 'version_extend')
    list_filter = ('mercado',)

@admin.register(Proxy)
class ProxyAdmin(admin.ModelAdmin):
    list_display = ('central', 'version', 'sw_version')
    list_filter = ('central',)
    search_fields = ('version__version_codif', 'sw_version')
