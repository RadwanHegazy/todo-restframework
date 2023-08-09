from django.shortcuts import get_object_or_404
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




@api_view(['GET','PUT','DELETE'])
def edit_todo (request, todoid) : 

    todo = get_object_or_404(Todo, id = todoid)

    if request.method == "GET" :
        serilaizer = TodoSerializer(todo)
        sts = status.HTTP_200_OK

    elif request.method == "PUT" :

        serilaizer = TodoSerializer(todo,data = request.data)
        
        if serilaizer.is_valid():
            serilaizer.save()
            sts = status.HTTP_200_OK
        else :
            sts = status.HTTP_400_BAD_REQUEST
        
            return Response (serilaizer.errors,status=sts)

    elif request.method == "DELETE" :
        todo.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    

    return Response(serilaizer.data,status=sts)