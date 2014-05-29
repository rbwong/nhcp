from django import forms
from seals.models import Region, Province, LGU, SealInfo, SealProperty

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field


class CategoryCreationForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.label_class = 'col-lg-1'
    helper.field_class = 'col-lg-11'
    helper.form_tag = False
    helper.layout = Layout(
        Field('name', wrapper_class='row'),
    )

    name = forms.CharField(required=True)

    class Meta:
        model = Region
        fields = ('name',)


class EditSVGForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.label_class = 'col-lg-2'
    helper.field_class = 'col-lg-10'
    helper.form_tag = False
    helper.layout = Layout(
        Field('name_fil', wrapper_class='row'),
    )

    name_fil = forms.CharField(required=False, label='Name in Filipino')
    svg = forms.CharField(widget=forms.HiddenInput())

    class Meta:
        model = Region
        fields = ('name_fil', 'svg')


class SealCreationForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.label_class = 'col-lg-2'
    helper.field_class = 'col-lg-10'
    helper.form_tag = False
    helper.layout = Layout(
        Field('image', wrapper_class='row'),
        Field('name', wrapper_class='row'),
        Field('name_fil', wrapper_class='row'),
        Field('description', wrapper_class='row'),
        Field('description_fil', wrapper_class='row'),
        Field('province', wrapper_class='row'),
    )

    image = forms.ImageField()
    name = forms.CharField(required=True)
    name_fil = forms.CharField(required=False, label='Name in Filipino')
    description = forms.CharField(widget=forms.Textarea, required=False)
    description_fil = forms.CharField(
        widget=forms.Textarea, label='Description in Filipino', required=False)
    province = forms.ModelChoiceField(
        Province.objects.all(), label='Official Seal of(Subcategory)')

    class Meta:
        model = LGU
        fields = ('image', 'name', 'name_fil', 'description',
                  'description_fil', 'province', 'location')


class SealInfoForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.label_class = 'col-lg-2'
    helper.field_class = 'col-lg-10'
    helper.form_tag = False
    helper.layout = Layout(
        Field('name', wrapper_class='row'),
        Field('name_fil', wrapper_class='row'),
        Field('description', wrapper_class='row'),
        Field('description_fil', wrapper_class='row'),
    )

    name = forms.CharField(required=True)
    name_fil = forms.CharField(required=False, label='Name in Filipino')
    description = forms.CharField(widget=forms.Textarea, required=False)
    description_fil = forms.CharField(
        widget=forms.Textarea, label='Description in Filipino', required=False)

    class Meta:
        model = SealInfo
        fields = ('name', 'name_fil', 'description', 'description_fil')


class SealPropertyForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.label_class = 'col-lg-2'
    helper.field_class = 'col-lg-10'
    helper.form_tag = False
    helper.layout = Layout(
        Field('name', wrapper_class='row'),
        Field('name_fil', wrapper_class='row'),
        Field('description', wrapper_class='row'),
        Field('description_fil', wrapper_class='row'),
    )

    name = forms.CharField(required=True)
    name_fil = forms.CharField(required=False, label='Name in Filipino')
    description = forms.CharField(widget=forms.Textarea, required=False)
    description_fil = forms.CharField(
        widget=forms.Textarea, label='Description in Filipino', required=False)
    svg = forms.CharField(widget=forms.HiddenInput())

    class Meta:
        model = SealProperty
        fields = ('name', 'name_fil', 'description', 'description_fil', 'svg')
