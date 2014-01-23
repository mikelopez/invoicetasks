"""
Set the static class views for admin functionality.
"""
import logging
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings
from models import Client, TaskToInvoice, Invoice
from forms import ClientForm, TaskToInvoiceForm, InvoiceForm
from braces.views import LoginRequiredMixin, StaffuserRequiredMixin

LOG_ON = getattr(settings, "LOG_ON", False)
MODULES = getattr(settings, "MODULES", ())

class UpdateInstanceView(UpdateView):
    """Todo:
    update providers and banners classes
    to update views to use base UpdateInstanceView
    """
    def get_context_data(self, **kwargs):
        context = super(UpdateInstanceView, self).get_context_data(**kwargs)
        context['extmodules'] = MODULES
        return context
        
    def form_valid(self, form):
        self.object = form.save(commit=False)
        clean = form.cleaned_data
        for k, v in clean.items():
            setattr(self.object, k, v)
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())



"""
class AdminIndexView(StaffuserRequiredMixin, TemplateView):
    # the admin index base view
    template_name = "www/admin-index.html"

"""

class BaseListView(ListView):
    def get_context_data(self, **kwargs):
        context = super(BaseListView, self).get_context_data(**kwargs)
        return context

class BaseCreateView(CreateView):
    def get_context_data(self, **kwargs):
        context = super(BaseCreateView, self).get_context_data(**kwargs)
        return context

class BaseDetailView(DetailView):
    """
    Base Detail Page View.
    """
    #queryset = Client.objects.all()

    def get_context_data(self, **kwargs):
        context = super(BaseDetailView, self).get_context_data(**kwargs)
        return context


# Clients
class ClientView(StaffuserRequiredMixin, BaseListView):
    """
    Shows the list of websites.
    """
    model = Client

class CreateClient(StaffuserRequiredMixin, BaseCreateView):
    """
    Create a new Client.
    """
    model = Client

class UpdateClient(StaffuserRequiredMixin, UpdateInstanceView):
    """
    Updates a website.
    """
    model = Client
    form_class = ClientForm
    template_name = 'invoicetasks/client_update.html'
    def get_object(self, queryset=None):
        obj = Client.objects.get(id=self.kwargs['pk'])
        return obj
    
class ClientDetailView(StaffuserRequiredMixin, BaseDetailView):
    """
    Client Detail Page View.
    """
    queryset = Client.objects.all()
    def get_object(self, **kwargs):
        obj = super(ClientDetailView, self).get_object(**kwargs)
        return obj



# TaskToInvoices
class TaskToInvoiceView(StaffuserRequiredMixin, BaseListView):
    """
    Shows the list of websites.
    """
    model = TaskToInvoice

class CreateTaskToInvoice(StaffuserRequiredMixin, BaseCreateView):
    """
    Create a new TaskToInvoice.
    """
    model = TaskToInvoice

class UpdateTaskToInvoice(StaffuserRequiredMixin, UpdateInstanceView):
    """
    Updates a website.
    """
    model = TaskToInvoice
    form_class = TaskToInvoiceForm
    template_name = 'invoicetasks/tasktoinvoice_update.html'
    def get_object(self, queryset=None):
        obj = TaskToInvoice.objects.get(id=self.kwargs['pk'])
        return obj
    
class TaskToInvoiceDetailView(StaffuserRequiredMixin, BaseDetailView):
    """
    TaskToInvoice Detail Page View.
    """
    queryset = TaskToInvoice.objects.all()
    def get_object(self, **kwargs):
        obj = super(TaskToInvoiceDetailView, self).get_object(**kwargs)
        return obj




# Invoices
class InvoiceView(StaffuserRequiredMixin, BaseListView):
    """
    Shows the list of websites.
    """
    model = Invoice

class CreateInvoice(StaffuserRequiredMixin, BaseCreateView):
    """
    Create a new Invoice.
    """
    model = Invoice

class UpdateInvoice(StaffuserRequiredMixin, UpdateInstanceView):
    """
    Updates a website.
    """
    model = Invoice
    form_class = InvoiceForm
    template_name = 'invoicetasks/invoice_update.html'
    def get_object(self, queryset=None):
        obj = Invoice.objects.get(id=self.kwargs['pk'])
        return obj
    
class InvoiceDetailView(StaffuserRequiredMixin, BaseDetailView):
    """
    Invoice Detail Page View.
    """
    queryset = Invoice.objects.all()
    def get_object(self, **kwargs):
        obj = super(InvoiceDetailView, self).get_object(**kwargs)
        return obj

