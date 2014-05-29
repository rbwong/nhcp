from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required, permission_required
from seals.views import *
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^$', MapView.as_view()),
    url(r'^new/$', login_required(CreateSealView.as_view())),
    url(r'^category/$', RegionView.as_view()),
    url(r'^category/new/$', login_required(CreateCategoryView.as_view())),
    url(r'^category/([\w-]+)/edit/$', login_required(UpdateCategoryView.as_view())),
    url(r'^category/([\w-]+)/delete/$', login_required(CategoryDelete.as_view())),
    url(r'^category/([\w-]+)/svg/$', login_required(UpdateSVG.as_view())),
    url(r'^([\w-]+)/$', SealView.as_view()),
    url(r'^([\w-]+)/edit/$', login_required(UpdateSealView.as_view())),
    url(r'^([\w-]+)/delete/$', login_required(SealDelete.as_view())),
    url(r'^([\w-]+)/seal-info/$', login_required(CreateSealInfoView.as_view())),
    url(r'^([\w-]+)/create-property/$', login_required(CreateSealProperty.as_view())),

    url(r'^sample$', TemplateView.as_view(template_name="sample.html")),
)
