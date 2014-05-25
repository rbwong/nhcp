from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import AuthenticationForm

@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')