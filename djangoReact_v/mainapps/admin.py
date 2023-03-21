from django.contrib import admin


from .models import Car, Maintenance, Complaints, Guide


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'number_car',
        'model_engine',
        'number_engine',
        'model_transmission',
        'number_transmission',
        'model_driving_bridge',
        'number_driving_bridge',
        'model_controlled_bridge',
        'number_controlled_bridge',
        'delivery_contract_number',
        'date_of_shipment_from_the_factory',
        'consignee',
        'delivery_address',
        'equipment',
        'client',
        'service_company',
        'guide'
    ]
    list_filter = ['number_car']
    readonly_fields = [
        'model_engine',
        'number_engine',
        'model_transmission',
        'number_transmission',
        'model_driving_bridge',
        'number_driving_bridge',
        'model_controlled_bridge',
        'number_controlled_bridge',
        'delivery_contract_number',
        'date_of_shipment_from_the_factory',
        'consignee',
        'delivery_address',
        'equipment',
        'client',
        'service_company',
        'guide'
    ]


admin.site.register(Car)


@admin.register(Maintenance)
class MaintenanceAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'type_of_maintenance',
        'date_of_maintenance',
        'operating_time',
        'order_number',
        'date_of_the_order_order',
        'the_organization_that_conducted',
        'car',
        'service_company',
        'guide',
    ]

    list_filter = ['type_of_maintenance']
    readonly_fields = [
        'date_of_maintenance',
        'operating_time',
        'order_number',
        'date_of_the_order_order',
        'the_organization_that_conducted',
        'car',
        'service_company',
        'guide',
    ]


admin.site.register(Maintenance)


@admin.register(Complaints)
class ComplaintsAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'date_of_refusal',
        'operating_time',
        'failure_node',
        'description_of_the_failure',
        'recovery_method',
        'spare_parts_used',
        'date_of_restoration',
        'equipment_downtime',
        'car',
        'service_company',
        'guide'
    ]

    list_filter = ['date_of_refusal']
    readonly_fields = [
        'operating_time',
        'failure_node',
        'description_of_the_failure',
        'recovery_method',
        'spare_parts_used',
        'date_of_restoration',
        'equipment_downtime',
        'car',
        'service_company',
        'guide'
    ]


admin.site.register(Complaints)


@admin.register(Guide)
class GuideAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'entity_name',
        'title',
        'description'
    ]

    list_filter = ['entity_name']
    readonly_fields = [
        'title',
        'description'
    ]


admin.site.register(Guide)
