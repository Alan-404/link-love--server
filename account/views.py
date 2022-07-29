from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from django.http import JsonResponse, FileResponse

from account.services import AccountService
from user.services import UserService

from common.middleware.jwt_middleware import JwtMiddleware
# Create your views here.

@api_view(['POST', "PUT"])
def auth_account(request):
    if request.method == 'POST':
        try:
            request_data = JSONParser().parse(request)
            user = UserService().get_user_by_email(request_data['email'])
            if user is None:
                return JsonResponse({'success': False, 'message': "Invalid Email or Password"}, status=400)
            account = AccountService().get_account_by_user_id(user['_id'])
            if account is None:
                return JsonResponse({'success': False, 'message': "Account Not Found"}, status=404)
            if AccountService().check_password_account(request_data['password'], account['password']):
                token = JwtMiddleware().create_token(account['_id'])
                return JsonResponse({'success': True, 'access_token': token}, status=200)
            return JsonResponse({'success': False, 'message': "Invalid Email or Password"}, status=400)
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=500)
    elif request.method == 'PUT':
        try:
            decoded_token = JwtMiddleware().encrypt_token(request.headers.get('Authorization'))
            if decoded_token == False:
                return JsonResponse({'success': False, 'message': "Invalid Token"}, status=400)
            request_data = JSONParser().parse(request)
            
            if AccountService().change_password(decoded_token['id'], request_data['old_password'], request_data['new_password']):
                return JsonResponse({'success': True}, status=200)
            return JsonResponse({'success': False, 'message': "Cannot Found Account"}, status=404)
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=500)