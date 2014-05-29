from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required, permission_required
from seals.views import *
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^$', MapView.as_view(), name='map-view'),
    url(r'^new/$', login_required(CreateSealView.as_view()), name='new-seal-view'),
    url(r'^category/$', RegionView.as_view(), name='category-view'),
    url(r'^category/new/$', login_required(CreateCategoryView.as_view())),
    url(r'^category/(?P<pk>[\w-]+)/edit/$', login_required(UpdateCategoryView.as_view()), name='category-edit-view'),
    url(r'^category/(?P<pk>[\w-]+)/delete/$', login_required(CategoryDelete.as_view())),
    url(r'^category/(?P<pk>[\w-]+)/svg/$', login_required(UpdateSVG.as_view()), name='category-svg-view'),
    url(r'^(?P<pk>[\w-]+)/$', SealView.as_view(), name='seal-view'),
    url(r'^(?P<pk>[\w-]+)/edit/$', login_required(UpdateSealView.as_view()), name='seal-edit-view'),
    url(r'^(?P<pk>[\w-]+)/delete/$', login_required(SealDelete.as_view()), name='seal-delete-view'),
    url(r'^(?P<pk>[\w-]+)/seal-info/$', login_required(CreateSealInfoView.as_view()), name='seal-info-view'),
    url(r'^(?P<pk>[\w-]+)/create-property/$', login_required(CreateSealProperty.as_view()), name='seal-prpty-view'),

    url(r'^sample$', TemplateView.as_view(template_name="sample.html")),
)
