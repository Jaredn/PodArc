from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404, render_to_response, HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.template import RequestContext

#Import Models
from models import Datacenters, Cages, CageRows, Racks

#Import System Modules
import re
import sys
import json


# Locations.Views #

def home(request, template_name='locations_home.html'):
    """ Home page for Locations app """
    return render(request, template_name)
