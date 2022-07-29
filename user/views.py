from rest_framework.decorators import api_view, parser_classes
from django.http import JsonResponse, FileResponse
from common.middleware.jwt_middleware import JwtMiddleware
from common.lib.lib import  save_file_image
# Services
from user.services import UserService
from account.services import AccountService

# Create your views here.

@api_view(['GET', 'POST'])
def user_api(request):
    if request.method == 'GET':
        try:
            users = UserService().get_all_users()
            return JsonResponse({'users': users}, status=200)
        except Exception as e:
            return JsonResponse({'message': str(e)}, status=500)
    elif request.method == 'POST':
        try:
            # Multipart/form-data
            request_data= request.data.dict()
            user = UserService().add_user(request_data)
            if user is None:
                return JsonResponse({'success': False, 'message': 'Cannot Add User'}, status=400)
            save_file_image(request_data['user_id'],request.data.dict()['avatar'].file)
            if AccountService().add_account(user):
                return JsonResponse({'success': True},status=200)
            return JsonResponse({'success': False,'message': 'Cannot Add Account'},status=400)
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=500)

@api_view(['GET'])
def auth(request):
    if request.method == "GET":
        try:
            token = JwtMiddleware().encrypt_token(request.headers.get('Authorization'))
            if token is None:
                return JsonResponse({'message': 'Invalid Token'}, status=403)
            account = AccountService().get_account_by_id(token['id'])
            if account is None:
                return JsonResponse({'message': 'Not Found Account'}, status=404)
            user = UserService().get_user_by_id(account['user_id'])
            if user is None:
                return JsonResponse({'message': 'Not Found User'}, status=404)
            return JsonResponse({'user': user}, status=200)
        except Exception as e:
            return JsonResponse({'message': str(e)}, status=500)


@api_view(['GET'])
def show_image_user(request):
    if request.method == 'GET':
        try:
            params = request.query_params
            type = params['type']
            if type is None:
                return JsonResponse({'message': 'Invalid Image'}, status=400)
            if type == 'default':
                url = "./common/lib/images/default image.png"
            else:
                id = params['id']
                if id is None:
                    return JsonResponse({'message': "Invalid user"}, status=400)
                url = f"./common/users/{id}/{type}.jpg"
            return FileResponse(open(url, 'rb'))
        except Exception as e:
            return JsonResponse({'message': str(e)}, status=500)

@api_view(['GET'])
def user_handle(request):
    if request.method == 'GET':
        try:
            id = request.query_params['id']
            if id is None:
                return JsonResponse({'message': "Invalid User"}, status=400)
            user = UserService().get_user_by_id(id)
            return JsonResponse({'user': user}, status=200)
        except Exception as e:
            return JsonResponse({'message': str(e)}, status=500)

