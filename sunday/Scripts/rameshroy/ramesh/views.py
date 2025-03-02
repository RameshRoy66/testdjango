from django.shortcuts import render, redirect
from .forms import LoginForm
from .models import Login
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import LoginSerializer

def register(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect after successful insertion
    else:
        form = LoginForm()
    
    return render(request, 'register.html', {'form': form})

def success(request):
    return render(request, 'success.html')


# Get all login data
@api_view(['GET'])
def get_logins(request):
    logins = Login.objects.all()  # Fetch all rows from login table
    ramesh= "ramesh"
    serializer = LoginSerializer(logins, many=True)  # Convert to JSON
    # Add extra data to the response
    response_data = {
        "message": "Success",
        "developer": "ramesh",
        "data": serializer.data
    }
    return Response(response_data)

# Get a single login user by ID
@api_view(['GET'])
def get_login_by_id(request, id):
    try:
        login = Login.objects.get(id=id)
        serializer = LoginSerializer(login)
        return Response(serializer.data)
    except Login.DoesNotExist:
        return Response({"error": "User not found"}, status=404)

# Create a new login user
@api_view(['POST'])
def create_login(request):
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

# Update login details
@api_view(['PUT'])
def update_login(request, id):
    try:
        login = Login.objects.get(id=id)
        serializer = LoginSerializer(login, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    except Login.DoesNotExist:
        return Response({"error": "User not found"}, status=404)

# Delete login user
@api_view(['DELETE'])
def delete_login(request, id):
    try:
        login = Login.objects.get(id=id)
        login.delete()
        return Response({"message": "User deleted"}, status=204)
    except Login.DoesNotExist:
        return Response({"error": "User not found"}, status=404)
