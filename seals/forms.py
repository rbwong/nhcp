from django import forms
from django.contrib.auth.models import User
from seals.models import Region, Province, LGU, SealInfo, SealProperty
from django.utils import timezone

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions

class CategoryCreationForm(forms.ModelForm):
    name = forms.CharField(required=True)

    class Meta:
        model = Region
        fields = ('name',)

    # Uni-form
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.form_class = 'form-horizontal'
        self.helper.layout = Layout(
            Field('name', css_class='input-xlarge'),
        )
        self.request = kwargs.pop('request', None)
        return super(CategoryCreationForm, self).__init__(*args, **kwargs)

class EditSVGForm(forms.ModelForm):
    name_fil = forms.CharField(required=False, label='Name in Filipino')
    svg = forms.CharField(widget=forms.HiddenInput())

    class Meta:
        model = Region
        fields = ('name_fil', 'svg')

    # Uni-form
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.form_class = 'form-horizontal'
        self.helper.layout = Layout(
            Field('name_fil', css_class='input-xlarge'),
        )
        self.request = kwargs.pop('request', None)
        return super(EditSVGForm, self).__init__(*args, **kwargs)


class SealCreationForm(forms.ModelForm):
    image = forms.ImageField()
    name = forms.CharField(required=True)
    name_fil = forms.CharField(required=False, label='Name in Filipino')
    description = forms.CharField(widget=forms.Textarea, required=False)
    description_fil = forms.CharField(widget=forms.Textarea, label='Description in Filipino', required=False)
    province = forms.ModelChoiceField(Province.objects.all(), label='Official Seal of(Subcategory)')

    class Meta:
        model = LGU
        fields = ('image', 'name', 'name_fil', 'description', 'description_fil', 'province', 'location')

    # Uni-form
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.form_class = 'form-horizontal'
        self.helper.layout = Layout(
            Field('name', css_class='input-xlarge'),
            Field('name_fil', css_class='input-xlarge'),
            Field('description', css_class='input-xlarge'),
            Field('description_fil', css_class='input-xlarge'),
        )
        self.request = kwargs.pop('request', None)
        return super(SealCreationForm, self).__init__(*args, **kwargs)


class SealInfoForm(forms.ModelForm):
    name = forms.CharField(required=True)
    name_fil = forms.CharField(required=False, label='Name in Filipino')
    description = forms.CharField(widget=forms.Textarea, required=False)
    description_fil = forms.CharField(widget=forms.Textarea, label='Description in Filipino', required=False)

    class Meta:
        model = SealInfo
        fields = ('name', 'name_fil', 'description', 'description_fil')

    # Uni-form
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.form_class = 'form-horizontal'
        self.helper.layout = Layout(
            Field('name', css_class='input-xlarge'),
            Field('name_fil', css_class='input-xlarge'),
            Field('description', css_class='input-xlarge'),
            Field('description_fil', css_class='input-xlarge'),
        )
        self.request = kwargs.pop('request', None)
        return super(SealInfoForm, self).__init__(*args, **kwargs)


class SealPropertyForm(forms.ModelForm):
    name = forms.CharField(required=True)
    name_fil = forms.CharField(required=False, label='Name in Filipino')
    description = forms.CharField(widget=forms.Textarea, required=False)
    description_fil = forms.CharField(widget=forms.Textarea, label='Description in Filipino', required=False)
    svg = forms.CharField(widget=forms.HiddenInput())

    class Meta:
        model = SealProperty
        fields = ('name', 'name_fil', 'description', 'description_fil', 'svg')

    # Uni-form
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.form_class = 'form-horizontal'
        self.helper.layout = Layout(
            Field('name', css_class='input-xlarge'),
            Field('name_fil', css_class='input-xlarge'),
            Field('description', css_class='input-xlarge'),
            Field('description_fil', css_class='input-xlarge'),
        )
        self.request = kwargs.pop('request', None)
        return super(SealPropertyForm, self).__init__(*args, **kwargs)