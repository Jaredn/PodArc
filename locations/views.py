from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404, render_to_response, HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.template import RequestContext

#Import Models
from models import Datacenters, Cages, CageRows, Racks

#Import Forms from forms.py
from forms import FormNewDatacenter, FormNewCage, FormNewCageRow, FormNewRack

#Import System Modules
import re
import sys
import json




# Locations.Views #

def home(request, template_name='locations_home.html'):
    """ Home page for Locations app """
    return render(request, template_name)

def datacenter_create(request, template_name='locations_datacenter_create.html'):
    """ View and Create Datacenters """


    if request.method == 'POST' and 'CreateDatacenter' in request.POST:
        form = FormNewDatacenter(request.POST) #create form object
        if form.is_valid():
            # Get POST Data from form.cleaned_Data
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            f = Datacenters(name=name, description=description) # create model object
            f.save() #insert new value into database
            return redirect('locations_datacenter_create') #Must match a urls.py "name"

    if request.method == 'POST' and 'input_delete_id' in request.POST:
        #Deactivate / Delete datacenter
        try:
            deleteId = int(request.POST['input_delete_id'])
        except:
            pass
        if deleteId >= 1:
            Datacenters.objects.filter(id=deleteId).update(active=0)
            return redirect('locations_datacenter_create') #Must match a urls.py "name"

    #Default action for GET, or POST's that fail validation.
    data = {}
    data['datacenters'] = Datacenters.objects.filter(active=1)
    data['form'] = FormNewDatacenter(request.POST or None) #Not POST or post failed, so make form object either way.
    return render(request, template_name, data)

def cage_create(request, template_name='locations_cage_create.html'):
    """ View and Create Cages"""
    if request.method == 'POST' and 'CreateCage' in request.POST:
        form = FormNewCage(request.POST) #create form object

        if form.is_valid():
            # Get POST Data from form.cleaned_Data
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            datacenter = form.cleaned_data['datacenter'].id #since datacenter is a foreignkey it returns the entire object.  You must reference 'id'.
            f = Cages(name=name, description=description, datacenter_id=datacenter) # create model object
            f.save() #insert new value into database
            return redirect('locations_cage_create') #Must match a urls.py "name"

    if request.method == 'POST' and 'input_delete_id' in request.POST:
        #Deactivate / Delete datacenter
        try:
            deleteId = int(request.POST['input_delete_id'])
        except:
            pass
        if deleteId >= 1:
            Cages.objects.filter(id=deleteId).update(active=0)
            return redirect('locations_cage_create') #Must match a urls.py "name"

    #Default action for GET, or POST's that fail validation.
    data = {}
    data['cages'] = Cages.objects.filter(active=1)
    data['form'] = FormNewCage(request.POST or None) #Not POST or post failed, so make form object either way.
    return render(request, template_name, data)

def cagerow_create(request, template_name='locations_cagerow_create.html'):
    """ View and Create Cage Rows"""

    if request.method == 'POST' and 'CreateCageRow' in request.POST:
        form = FormNewCageRow(request.POST) #create form object
        if form.is_valid():
            # Get POST Data from form.cleaned_Data
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            cage = form.cleaned_data['cage'].id
            f = CageRows(name=name, description=description, cage_id=cage) # create model object
            f.save() #insert new value into database
            return redirect('locations_cagerow_create') #Must match a urls.py "name"

    if request.method == 'POST' and 'input_delete_id' in request.POST:
        #Deactivate / Delete datacenter
        try:
            deleteId = int(request.POST['input_delete_id'])
        except:
            pass
        if deleteId >= 1:
            CageRows.objects.filter(id=deleteId).update(active=0)
            return redirect('locations_cageRow_create') #Must match a urls.py "name"

    #Default action for GET, or POST's that fail validation.
    data = {}
    data['cageRows'] = CageRows.objects.filter(active=1)
    data['form'] = FormNewCageRow(request.POST or None) #Not POST or post failed, so make form object either way.
    return render(request, template_name, data)

def rack_create(request, template_name='locations_rack_create.html'):
    """ View and Create Racks"""

    if request.method == 'POST' and 'CreateRack' in request.POST:
        form = FormNewRack(request.POST) #create form object
        if form.is_valid():
            # Get POST Data from form.cleaned_Data
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            cagerow = form.cleaned_data['cagerow'].id
            f = Racks(name=name, description=description, cagerow_id=cagerow) # create model object
            f.save() #insert new value into database
            return redirect('locations_rack_create') #Must match a urls.py "name"

    if request.method == 'POST' and 'input_delete_id' in request.POST:
        #Deactivate / Delete datacenter
        try:
            deleteId = int(request.POST['input_delete_id'])
        except:
            pass
        if deleteId >= 1:
            Racks.objects.filter(id=deleteId).update(active=0)
            return redirect('locations_rack_create') #Must match a urls.py "name"

    #Default action for GET, or POST's that fail validation.
    data = {}
    data['racks'] = Racks.objects.filter(active=1)
    data['form'] = FormNewRack(request.POST or None) #Not POST or post failed, so make form object either way.
    return render(request, template_name, data)




#### View Locations (Datacenter/Cage/Rack/Row) by ID

def datacenter_by_id(request, pk, template_name='locations_datacenter_by_id.html'):
    """ View a datacenter by ID """


    # if request.method == 'POST' and 'CreateDatacenter' in request.POST:
    #     form = FormNewDatacenter(request.POST) #create form object
    #     if form.is_valid():
    #         # Get POST Data from form.cleaned_Data
    #         name = form.cleaned_data['name']
    #         description = form.cleaned_data['description']
    #         f = Datacenters(name=name, description=description) # create model object
    #         f.save() #insert new value into database
    #         return redirect('locations_datacenter_create') #Must match a urls.py "name"
    #
    # if request.method == 'POST' and 'input_delete_id' in request.POST:
    #     #Deactivate / Delete datacenter
    #     try:
    #         deleteId = int(request.POST['input_delete_id'])
    #     except:
    #         pass
    #     if deleteId >= 1:
    #         Datacenters.objects.filter(id=deleteId).update(active=0)
    #         return redirect('locations_datacenter_create') #Must match a urls.py "name"

    #Default action for GET, or POST's that fail validation.
    data = {}
    data['this_datacenter'] = Datacenters.objects.filter(id=pk)
    return render(request, template_name, data)