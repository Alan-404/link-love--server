from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser


from like.services import LikeService

# Create your views here.


""" @api_view(['POST'])
def like_api(request):
    if request.method == 'POST': """