from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from joseph.models import Joseph
from joseph.serializers import JosephSerializer
@csrf_exempt
def joseph_list(request):
    """
    List all code joseph, or create a new joseph.
    """
    if request.method == 'GET':
        joseph = Joseph.objects.all()
        serializer = JosephSerializer(joseph, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = JosephSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
        @csrf_exempt
        def joseph_detail(request, pk):
            """
            Retrieve, update or delete a code joseph.
            """
            try:
                joseph = Joseph.objects.get(pk=pk)
            except Snippet.DoesNotExist:
                return HttpResponse(status=404)
        
            if request.method == 'GET':
                serializer = JosephSerializer(joseph)
                return JsonResponse(serializer.data)
        
            elif request.method == 'PUT':
                data = JSONParser().parse(request)
                serializer = JosephSerializer(joseph, data=data)
                if serializer.is_valid():
                    serializer.save()
                    return JsonResponse(serializer.data)
                return JsonResponse(serializer.errors, status=400)
        
            elif request.method == 'DELETE':
                joseph.delete()
                return HttpResponse(status=204)