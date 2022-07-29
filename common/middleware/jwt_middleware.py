import jwt
from datetime import datetime
from common.lib.secret import key_token

class JwtMiddleware:
    def create_token(self, account_id):
        payload = {
            'id': account_id,
            'time': str(datetime.now())
        }

        return jwt.encode(payload=payload, key=key_token,algorithm='HS256')

    def encrypt_token(self, authorization_token):
        token = str(authorization_token).split(' ')[1]
        if token is None:
            return False
        decoded = jwt.decode(token, key=key_token, algorithms='HS256')
        return decoded