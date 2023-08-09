from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Todo
from .serilaizers import TodoSerializer
from rest_framework import status


@api_view(['GET',"POST"])
def home (request) : 

    if request.method == "POST" :
        serialiser = TodoSerializer(data = request.data )
        
        if serialiser.is_valid() :
            serialiser.save()
            return Response(serialiser.data, status=status.HTTP_201_CREATED)
        else :
            return Response(serialiser.data,status=status.HTTP_400_BAD_REQUEST)
        

    todo = Todo.objects.order_by('-date')

    serializer = TodoSerializer(todo, many=True)

    return Response(serializer.data)



