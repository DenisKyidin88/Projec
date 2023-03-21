from django.db import models


class Car(models.Model):
    objects = True
    number_car = models.CharField(max_length=255)
    model_technique = models.CharField(max_length=255)
    model_engine = models.CharField(max_length=255)
    number_engine = models.CharField(max_length=255)
    model_transmission = models.CharField(max_length=255)
    number_transmission = models.CharField(max_length=255)
    model_driving_bridge = models.CharField(max_length=255)
    number_driving_bridge = models.CharField(max_length=255)
    model_controlled_bridge = models.CharField(max_length=255)
    number_controlled_bridge = models.CharField(max_length=255)
    delivery_contract_number = models.CharField(max_length=255)
    date_of_shipment_from_the_factory = models.DateField(auto_now=True)
    consignee = models.CharField(max_length=255)
    delivery_address = models.CharField(max_length=255)
    equipment = models.CharField(max_length=255)
    client = models.CharField(max_length=255)
    service_company = models.CharField(max_length=255)
    guide = models.ManyToManyField("Guide", through='GuideCar')


class Maintenance(models.Model):
    objects = True
    type_of_maintenance = models.CharField(max_length=255)
    date_of_maintenance = models.DateField(auto_now_add=True)
    operating_time = models.DateField(auto_now=True)
    order_number = models.CharField(max_length=255)
    date_of_the_order_order = models.DateField(auto_now=True)
    the_organization_that_conducted = models.CharField(max_length=255)
    car = models.CharField(max_length=255)
    service_company = models.CharField(max_length=255)
    guide = models.ForeignKey("Guide", on_delete=models.CASCADE)


class Complaints(models.Model):
    objects = True
    date_of_refusal = models.DateField(auto_now_add=True)
    operating_time = models.DateField(auto_now_add=True)
    failure_node = models.CharField(max_length=255)
    description_of_the_failure = models.CharField(max_length=255)
    recovery_method = models.CharField(max_length=255)
    spare_parts_used = models.CharField(max_length=255)
    date_of_restoration = models.DateField(auto_now_add=True)
    equipment_downtime = models.FloatField(default=0.00)
    car = models.CharField(max_length=255)
    service_company = models.CharField(max_length=255)
    guide = models.ForeignKey("Guide", on_delete=models.CASCADE)


class Guide(models.Model):
    objects = True
    entity_name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()


class GuideCar(models.Model):
    guide = models.ForeignKey(Guide, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    amount = models.IntegerField(default=1)
