from rest_framework.decorators import api_view
from .models import Task
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def retrieve_tasks(request):
    tasks = list(Task.objects.filter(user=request.user).values("id", "title", "description", "status"))
    return Response(data=tasks, status=200)

@api_view(['DELETE'])
def delete_task(request,pk):
    user = request.user
    try:
        task = Task.objects.get(id=pk)

    except Exception as e:
        return Response(data={
            "message": "object not found",
        }, status= 402)
    
    if task.user != user:
        return Response (
            data={
                "message":"Permession denied",
            },
            status=404
        )
    task.delete()

    return Response({"message":"successfully deleted"}, status=200)

@api_view(['POST'])
def create_task(request):
    user = request.user
    data = request.data
    STATUS_CHOICES = [
        "pending", "in_progress", "completed"
    ]
    mileko_data = {}
    if not isinstance(data["title"], str) or not data["title"].strip():
        return Response({"message":"title is invalid"}, status=400)
    else:
        mileko_data["title"]=data["title"]


    if not isinstance(data["description"], str):
        return Response({"message":"description is not a string"}, status=400)
    else:
        mileko_data["description"]=data["description"]


    if not data["status"] in STATUS_CHOICES:
        return Response({"message":"status does not exist in choices"}, status=400)
    else:
        mileko_data["status"]=data["status"]

    mileko_data["user"]=user


    task = Task.objects.create(**mileko_data)
    return Response({"message": "task created successfully"}, status=200)

@api_view(['GET'])
def retrieve_task(request,pk):
    tasks = Task.objects.filter(user=request.user,id=pk).values("id", "title", "description", "status").first()
    return Response(data=tasks or {}, status=200)

@api_view(['PATCH'])
def update_task(request, pk):
    data = request.data
    user=request.user
    STATUS_CHOICES = [
        "pending", "in_progress", "completed"
    ]
    try:
        task = Task.objects.get(id=pk)
    except Exception as e:
        return Response(
            {"message": "Task not found"},
            status=404
        )
    if task.user != user:
        return Response (
            data={
                "message":"Permession denied",
            },
            status=404
        )
    if "title" in data:
        if not isinstance(data["title"], str) or not data["title"].strip():
            return Response({"message":"title is invalid"}, status=400)
        task.title = data["title"]

    if "description" in data:
        if not isinstance(data["description"], str):
            return Response({"message":"description is not a string"}, status=400)
        task.description = data["description"]

    if "status" in data:
        if not data["status"] in STATUS_CHOICES:
            return Response({"message":"status does not exist in choices"}, status=400)
        task.status=data["status"]

    task.save()
    return Response({"message":"task updated"},status=200)

    

    
    
 
