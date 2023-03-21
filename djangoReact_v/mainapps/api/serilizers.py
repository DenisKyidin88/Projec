from rest_framework import serializers

from ..models import Car, Maintenance, Complaints, Guide


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = [
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


class MaintenanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maintenance
        fields = [
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


class ComplaintsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complaints
        fields = [
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


class GuideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guide
        fields = [
            'id',
            'entity_name',
            'title',
            'description'
        ]
