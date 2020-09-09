import json # Como era feito de forma anterior

from restapi.mixins import JsonResponseMixin
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.generic import View

from .models import Update
# def detail_view(request):
    # return render() # return JSON -> JS Object Notation
    # return HttpResponse(get_template().render({}))

def json_example_view(request):
    '''
    URI - REST API
    GET - Retrieve
    '''
    data = {
        "count": 1000,
        "content": "Some new content"
    }
    return JsonResponse(data)
    # json_data = json.dumps(data) # Como era feito da forma anterior
    # return HttpResponse(json_data, content_type='application/json') # Como era feito da forma anterior

class JsonCBV(View):
   def get(self, request, *args, **kwargs):
    '''
    URI - REST API
    GET - Retrieve
    '''
    data = {
        "count": 1000,
        "content": "Some new content"
    }
    return JsonResponse(data)



class JsonCBV2(JsonResponseMixin, View):
   def get(self, request, *args, **kwargs):
    data = {
        "count": 1000,
        "content": "Some new content"
    }
    return self.render_to_json_response(data)