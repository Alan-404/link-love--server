from rest_framework.decorators import api_view
from post.services import PostService
from django.http import JsonResponse, FileResponse

from common.middleware.jwt_middleware import JwtMiddleware
from account.services import AccountService
from common.lib.lib import save_list_files_post, save_file_image
# Create your views here.


@api_view(['POST'])
def post_api(request):
    if request.method == 'POST':
        try:
            # multipart/form-data
            request_data = request.data.dict()
            account_id = JwtMiddleware().encrypt_token(authorization_token=request.headers.get('Authorization'))['id']
            if account_id is None:
                return JsonResponse({'success': False, 'message': "invalid user"}, status=403)
            account = AccountService().get_account_by_id(account_id)
            if account is None:
                return JsonResponse({'success': False, 'message': "invalid user"}, status=403)
            request_data['user_id'] = account['user_id']
            post = PostService().add_post(request_data)
            if post is None:
                return JsonResponse({'message': "Can't add Post"}, status=400)
            save_list_files_post(post['_id'], request.data, len(request.FILES))
            return JsonResponse({'success': True}, status=200)
        except Exception as e:
            return JsonResponse({'message': str(e)})


@api_view(['GET'])
def media_view(request):
    if request.method == 'GET':
        try:
            params = request.query_params
            post_id = params['id']
            index = params['index']
            return FileResponse(open(f"./common/posts/{post_id}/{index}.mp4", 'rb'))
        except Exception as e:
            return JsonResponse({'message': str(e)})