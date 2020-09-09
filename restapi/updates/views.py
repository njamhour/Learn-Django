import json # Como era feito de forma anterior

from django.core.serializers import serialize

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.generic import View

from restapi.mixins import JsonResponseMixin
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
    # return HttpResponse(json_data, content_type='application/json')

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

class SerializedView(View):
    def get(self, request, *args, **kwargs):
        obj = Update.objects.get(id=1)
        data = serialize("json", [obj,], fields=('user', 'content'))
        # print(data)
        # data = {
        #     "user": obj.user.username,
        #     "content": obj.content,
        # }
        json_data = data
        return HttpResponse(json_data, content_type='application/json')

class SerializedListView(View):
    def get(self, request, *args, **kwargs):
        qs = Update.objects.all()
        data = serialize("json", qs, fields=('user', 'content'))
        print(data)
        # data = {
        #    "user": qs.user.username,
        #    "content": qs.content,
        # }
        # json_data = json.dumps(data)
        json_data = data
        return HttpResponse(json_data, content_type='application/json')