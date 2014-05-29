from django.shortcuts import render, get_object_or_404, render_to_response
from django.template import RequestContext
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.utils import translation
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Region, Province, LGU, SealInfo, SealProperty
from .forms import CategoryCreationForm, EditSVGForm, SealCreationForm, SealInfoForm, SealPropertyForm


class MapView(ListView):
    queryset = LGU.objects.all().order_by('name')
    template_name = 'seals/map.html'

    def get_context_data(self, **kwargs):
        context = super(MapView, self).get_context_data(**kwargs)
        context['regions'] = Region.objects.all()
        context['provinces'] = Province.objects.all().order_by('name')
        return context


class RegionView(ListView):
    queryset = Region.objects.all().order_by('name')
    template_name = 'seals/region_list.html'

    def get_context_data(self, **kwargs):
        context = super(RegionView, self).get_context_data(**kwargs)
        return context


class CreateCategoryView(CreateView):
    template_name = 'seals/create_category.html'
    form_class = CategoryCreationForm
    success_url = '/'

    def form_valid(self, form):
        if '_save' in self.request.POST:
            self.success_url = '/'
        elif '_save_and_edit' in self.request.POST:
            self.success_url = '/category/' + form.instance.name + '/edit/'
        return super(CreateCategoryView, self).form_valid(form)


class UpdateCategoryView(UpdateView):
    model = Region
    form_class = CategoryCreationForm
    template_name = 'seals/update_category.html'

    def get_object(self):
        name = self.args[0].replace('-', ' ')
        return get_object_or_404(Region, name__iexact=name)

    def get_success_url(self):
        return '/category/' + self.args[0] + '/edit/'

    def form_valid(self, form):
        return super(UpdateCategoryView, self).form_valid(form)


class CategoryDelete(DeleteView):
    model = Region
    template_name = 'seals/delete_category.html'
    success_url = '/category/'

    def get_object(self):
        name = self.args[0].replace('-', ' ')
        return get_object_or_404(Region, name__iexact=name)


class UpdateSVG(UpdateView):
    model = Region
    form_class = EditSVGForm
    template_name = 'seals/edit_svg.html'

    def get_object(self):
        name = self.args[0].replace('-', ' ')
        return get_object_or_404(Region, name__iexact=name)

    def get_success_url(self):
        return '/category/' + self.args[0] + '/edit/'

    def form_valid(self, form):
        return super(UpdateSVG, self).form_valid(form)


class CreateSealView(CreateView):
    template_name = 'seals/create_seal.html'
    form_class = SealCreationForm
    success_url = '/'

    def form_valid(self, form):
        return super(CreateSealView, self).form_valid(form)


class SealView(DetailView):
    template_name = 'seals/seal.html'

    def get_object(self):
        name = self.args[0].replace('-', ' ')
        return get_object_or_404(LGU, name__iexact=name)

    def get_context_data(self, **kwargs):
        context = super(SealView, self).get_context_data(**kwargs)
        context['properties'] = SealProperty.objects.filter(seal=self.object)
        return context


class UpdateSealView(UpdateView):
    model = LGU
    form_class = SealCreationForm
    template_name = 'seals/update_seal.html'
    success_url = '/'

    def get_object(self):
        name = self.args[0].replace('-', ' ')
        return get_object_or_404(LGU, name__iexact=name)

    def get_success_url(self):
        return '/' + self.args[0] + '/'

    def form_valid(self, form):
        return super(UpdateSealView, self).form_valid(form)


class SealDelete(DeleteView):
    model = LGU
    template_name = 'seals/delete_seal.html'
    success_url = '/'

    def get_object(self):
        name = self.args[0].replace('-', ' ')
        return get_object_or_404(LGU, name__iexact=name)


class CreateSealInfoView(CreateView):
    template_name = 'seals/create_seal_info.html'
    form_class = SealInfoForm
    success_url = '/'

    def get_success_url(self):
        return '/' + self.args[0] + '/'

    def form_valid(self, form, **kwargs):
        name = self.args[0].replace('-', ' ')
        lgu = get_object_or_404(LGU, name__iexact=name)
        form.instance.seal = lgu
        return super(CreateSealInfoView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(CreateSealInfoView, self).get_context_data(**kwargs)
        name = self.args[0].replace('-', ' ')
        context['object'] = get_object_or_404(LGU, name__iexact=name)
        return context


class CreateSealProperty(CreateView):
    form_class = SealPropertyForm
    template_name = 'seals/create_seal_property.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(CreateSealProperty, self).get_context_data(**kwargs)
        name = self.args[0].replace('-', ' ')
        context['object'] = get_object_or_404(LGU, name__iexact=name)
        return context

    def get_success_url(self):
        return '/' + self.args[0] + '/'

    def form_valid(self, form):
        name = self.args[0].replace('-', ' ')
        form.instance.seal = get_object_or_404(LGU, name__iexact=name)
        return super(CreateSealProperty, self).form_valid(form)
