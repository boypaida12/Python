from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views import View
from rest_framework import status
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from main.models import *
from main.serializers import *
import datetime
from rest_framework import viewsets
from inmest_api.utils import *

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
    
    def post(self, request):
        return JsonResponse({"status": "ok"})

@api_view(["GET"])
def fetch_class_schedules(request):

    print("User making", request.user)
    # 1. Retrieve from db all class schedules
    queryset = ClassSchedule.objects.all()

    # 2. Return queryset result as response
    # 2b. Transform/serialize the queryset result to json and send as response

    serializer = ClassScheduleSerializer(queryset, many=True)

    # 3. Respond to the request
    return Response({"data": serializer.data}, status.HTTP_200_OK)

@api_view(["POST"])
def create_class_schedule(request):
    # Receiving data from frontend
    title = request.data.get("title")
    description = request.data.get("description")
    start_date_and_time = request.data.get("start_date_and_time")
    end_date_and_time = request.data.get("end_date_and_time")
    cohort_id = request.data.get("cohort_id")
    venue = request.data.get("venue")
    facilitator_id = request.data.get("facilitator_id")
    is_repeated = request.data.get("is_repeated", False)
    repeat_frequency = request.data.get("repeat_frequency", None)
    course_id = request.data.get("course_id")
    meeting_type = request.data.get("meeting_type")

    #Performing validations
    if not title:
        return Response({"message":"My friend, send me title"}, status.HTTP_400_BAD_REQUEST)
    
    cohort = None
    facilitator = None
    course = None

    #Validating the existence of records

    try:
        cohort = Cohort.objects.get(id=cohort_id)
    except Cohort.DoesNotExist:
        return Response({"message": "Massaa, this cohort does not exist"}, status.HTTP_400_BAD_REQUEST)
    
    try:
        facilitator = IMUser.objects.get(id=facilitator_id)
    except IMUser.DoesNotExist:
        return Response({"message": "Massaa, this facilitator does not exist"}, status.HTTP_400_BAD_REQUEST)
    
    try:
        course = Course.objects.get(id=course_id)
    except Course.DoesNotExist:
        return Response({"message": "Massaa, this course does not exist"}, status.HTTP_400_BAD_REQUEST)
    
    #creating class schedule
    class_schedule = ClassSchedule.objects.create(
        title=title,
        description=description,
        venue=venue,
        is_repeated=is_repeated,
        repeat_frequency=repeat_frequency,
        facilitator=facilitator,
        start_date_and_time=datetime.datetime.now(),
        end_date_and_time=datetime.datetime.now(),
        cohort=cohort,
        course=course,
        organizer=facilitator
    )
    class_schedule.save()

    serializer = ClassScheduleSerializer(class_schedule, many=False)
    return Response({"message": "Schedule successfully created", "data": serializer.data}, status.HTTP_201_CREATED)




class QueryModelViewSet(viewsets.ModelViewSet):
    @action(detail=False, methods=["post"])
    def raise_query(self, request):
        title = request.data.get("title")
        description = request.data.get("description", None)
        query_type = request.data.get("query_type", None)
        assignee = None
        # if query_type == 'FACILITY':
        #     assignee = IMUser.objects.get(email="lucky@")
        query = Query.objects.create(
            title=title,
            description=description,
            query_type=query_type,
            submitted_by=request.user,
            author=request.user
        )
        query.save()
        #send email to the assignee
        return Response({"message": "Query successfully submitted"})
    

    @action(detail=False, methods=["post"])
    def filter_queries(self, request):
        search_text = request.data.get("search_text")
        status = request.data.get("status")

        queryset = Query.objects.all()
        serializer = QuerySerializer(queryset, many=True)
        
        return generate_200_response(serializer.data)
    
class ClassModelViewset(viewsets.ModelViewSet):
    pass