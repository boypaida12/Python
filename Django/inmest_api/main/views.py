from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views import View

# Create your views here.

def json_response(request):
    return JsonResponse({"name": "Lucky"})

def say_hello(req):
    return HttpResponse("<h1>Hello Amigo</h1>")

def user_profile(req):
    return JsonResponse({
        "firstName": "Kwame",
        "lastName": "Johnson",
        "age": 40,
        "email": "johnson@gmail.com",
        "location": "Accra",
        "occupation": "JoAT",
        "company": "TBD",
    })
    
def filter_queries(req, id):
    data = {
        "id": id,
        "title": "the gods",
        "description": "the stories untold",
        "status": "published",
        "submitted_by": "kabutey"
    }
    return JsonResponse(data)

class QueryView(View):
    queries = [
            {"id": 1, "title": "Adama"},
            {"id": 2, "title": "Samson"}
        ]
    def get(self, request):
        
        return JsonResponse({"result": self.queries})