from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Todo
from .serilaizers import TodoSerializer

@api_view(['GET'])
def home (request) : 

    todo = Todo.objects.order_by('-date')

    serializer = TodoSerializer(todo, many=True)

    return Response(serializer.data)


# @api_view(['POST'])
# def create_todo (request) :
