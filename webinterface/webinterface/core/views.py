from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

# Create your views here.
from django.contrib.auth.decorators import login_required

from .forms import BugCreateForm, ProductForm
from .models import Bug, BugProductStatus

import pdb

def bug(request, bug_id):
    #return HttpResponse('This is bug {}'.format(bug_id))
    if request.method == 'POST':
        # handle form data and insert it into db
        pass
    else:
        # show form to add a bug
        return render(request, "core/bug.html", {"bug_id": bug_id})

def bug_list(request):
    if request.method == 'GET':
        #bugs = Bug.objects.all().values()
        #bugs = Bug.objects.prefetch_related('product__product_type').all().values()
        bugs = Bug.objects.prefetch_related('product__product_type').all()
        return JsonResponse([bug.get_json() for bug in bugs], safe=False)
        #return JsonResponse(list(bugs), safe=False)
    elif request.method == 'POST':
        data = request.POST
        
"""
@login_required
def bug_create(request):
    if request.method == 'POST':
        
        form_bug = BugCreateForm(data=request.POST)
        form_product = ProductForm(data.request.POST)

        pdb.set_trace()
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            
            
            bug_product_status = BugProductStatus()
            print("form.id = {}".format(form.id))
            return redirect("core/bug_create_ok.html", form=form)
    else:
        form_bug = BugCreateForm()
        form_product = ProductForm()
        context = {
            "form_bug": form_bug,
            "form_product": form_product
        }
        return render(request, "core/bug_create.html", context=context)
"""

