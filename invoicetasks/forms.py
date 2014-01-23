from django import forms
from django.forms import ModelForm
from models import TaskToInvoice, Client, Invoice


class BaseForm(ModelForm):
    """Providers Custom form"""
    def __init__(self, *args, **kwargs):
        super(BaseForm, self).__init__(*args, **kwargs)


class TaskToInvoiceForm(BaseForm):
    """TaskToInvoice Custom form"""
    class Meta:
        model = TaskToInvoice

class ClientForm(BaseForm):
    """Client Custom form"""
    class Meta:
        model = Client

class InvoiceForm(BaseForm):
    """Invoice Custom form"""
    class Meta:
        model = Invoice
