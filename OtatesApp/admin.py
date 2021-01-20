from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from OtatesApp.models import Proveedor, Ingreso, Egreso,Sucursal, Empleado



# Register your models here.
class ProveedorResource(resources.ModelResource):
    class Meta:
        model = Proveedor

class SucursalResource(resources.ModelResource):
    class Meta:
        model = Sucursal

class IngresoResource(resources.ModelResource):
    class Meta:
        model = Ingreso

class EgresoResource(resources.ModelResource):
    class Meta:
        model = Egreso

class EmpleadoResource(resources.ModelResource):
    class Meta:
        model = Empleado




class ProveedorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display=("razonsocial", "rfc")
    search_fields=("razonsocial","rfc")
    resource_class = ProveedorResource

class IngresoAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display=("fecha", "folio_in","folio_fin","importe","capturado_por")
    search_fields=("fecha", "folio_in","folio_fin","capturado_por")
    list_filter=("fecha",)
    resource_class = IngresoResource


class EgresoAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display=("fecha", "folio","capturado_por","importe","autorizado_por")
    search_fields=("fecha", "folio","capturado_por")
    list_filter=("fecha","autorizado_por",)
    resource_class = EgresoResource


class SucursalAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display=("nombre", "responsable")
    search_fields=("nombre", "responsable")
    resource_class = SucursalResource

class EmpleadoAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display=("user", "sucursal")
    search_fields=("user", "sucursal")
    resource_class = EmpleadoResource


admin.site.register(Proveedor, ProveedorAdmin)
admin.site.register(Ingreso, IngresoAdmin)
admin.site.register(Egreso, EgresoAdmin)
admin.site.register(Sucursal, SucursalAdmin)
admin.site.register(Empleado, EmpleadoAdmin)