from django.db import models

class Supplier(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class PurchaseOrder(models.Model):
    supplier = models.ForeignKey('Supplier', on_delete=models.CASCADE)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description

class Docket(models.Model):
    name = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    num_hours_worked = models.DecimalField(max_digits=10, decimal_places=2)
    rate_per_hour = models.DecimalField(max_digits=10, decimal_places=2)
    supplier = models.ForeignKey('Supplier', on_delete=models.CASCADE)
    purchase_order = models.ForeignKey('PurchaseOrder', on_delete=models.CASCADE)

    def __str__(self):
        return self.name