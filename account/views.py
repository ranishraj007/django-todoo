from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.


User = get_user_model()
@api_view(['POST'])
def login(request):
    data= request.data
    username = data.get('username')
    password = data.get('password')
    try:
        user= User.objects.get(username=username)
        if user.check_password(password):
            return Response({"message": "Login successful"}, status=200)
        else:
            return Response({"message":"Login Failed"}, status=401)
    except Exception as e:
        return Response({"message": "Something went wrong", "error":str(e)}, status=401)
