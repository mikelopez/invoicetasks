from django.conf.urls import patterns, include, url
from django.conf import settings
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from invoicetasks.views import \
        CreateInvoice, UpdateInvoice, InvoiceView, InvoiceDetailView, \
        CreateTaskToInvoice, UpdateTaskToInvoice, TaskToInvoiceView, TaskToInvoiceDetailView, \
        CreateClient, UpdateClient, ClientView, ClientDetailView
        

PROJECT_ROOTDIR = getattr(settings, 'PROJECT_ROOTDIR', '')

urlpatterns = patterns('',

    #url(r'^$', InvoiceView.as_view(), name="adminview"),
    
    url(r'^invoice/add', CreateInvoice.as_view(), name="invoice_add"),
    url(r'^invoice/update/(?P<pk>\d+)', UpdateInvoice.as_view(), name="update_invoice"),
    url(r'^invoice/(?P<pk>\d+)', InvoiceDetailView.as_view(), name="invoice_detail"),
    url(r'^invoice/', InvoiceView.as_view(), name="invoice_view"),

    url(r'^tasktoinvoice/add', CreateTaskToInvoice.as_view(), name="tasktoinvoice_add"),
    url(r'^tasktoinvoice/update/(?P<pk>\d+)', UpdateTaskToInvoice.as_view(), name="update_tasktoinvoice"),
    url(r'^tasktoinvoice/(?P<pk>\d+)', TaskToInvoiceDetailView.as_view(), name="tasktoinvoice_detail"),
    url(r'^tasktoinvoice/', TaskToInvoiceView.as_view(), name="tasktoinvoice_view"),

    url(r'^client/add', CreateClient.as_view(), name="client_add"),
    url(r'^client/update/(?P<pk>\d+)', UpdateClient.as_view(), name="update_client"),
    url(r'^client/(?P<pk>\d+)', ClientDetailView.as_view(), name="client_detail"),
    url(r'^client/', ClientView.as_view(), name="client_view"),


    #(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root':'%s/static/' % (PROJECT_ROOTDIR), 'show_indexes': True}),


)
