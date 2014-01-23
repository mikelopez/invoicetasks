from django.db import models
from datetime import datetime

# Create your models here.
class Client(models.Model):
    """Client to bill."""
    CLIENT_STAT = (
            ('pending','pending'),
            ('followup','followup'),
            ('active','active'),)
    name = models.CharField(max_length=100)
    email = models.TextField(max_length=100)
    status = models.CharField(max_length=10, choices=CLIENT_STAT)
    @property
    def has_invoices(self):
        """Has an invoice or not..."""
        return self.invoice_set.select_related()
    def __str__(self):
        return str(self.name)
    def __unicode__(self):
        return unicode(self.name)


class TaskToInvoice(models.Model):
    """A task that will be invoiced"""
    TASK_STAT = (
            ('pending','pending'),
            ('started','started'),
            ('finished','finished'),)
    brief = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    hours = models.IntegerField(blank=True, null=True, default=0)
    status = models.CharField(max_length=12, blank=True, null=True, choices=TASK_STAT)
    rate = models.IntegerField(default=0, blank=True, null=True)


class Invoice(models.Model):
    """Invoices"""
    client = models.ForeignKey('Client')
    date_created = models.DateTimeField(blank=True, null=True)
    paid = models.NullBooleanField(blank=True, null=True, default=False)
    total = models.CharField(blank=True, null=True, default="0.00", max_length=10)
    def save(self):
        if not getattr(self, 'date_created'):
            setattr(self, 'date_created', datetime.now())
        super(self, Invoice).save()


