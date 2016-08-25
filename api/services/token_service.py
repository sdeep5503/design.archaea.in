import jwt
import json
from datetime import datetime, timedelta, date


class TokenService:

    def __init__(self):
        pass

    @staticmethod
    def create_jwt_token(user_guid=None):
        date_handler = lambda obj: (obj.isoformat()
                                    if isinstance(obj, datetime)
                                       or isinstance(obj, date)
                                    else None
                                    )
        payload = {
            # idp name
            '_idp': 'design.archaea.in',
            # subject
            '_identity': user_guid,
            # issued at
            '_iat': json.dumps(datetime.now(), default=date_handler),
            # expiry
            '_exp': json.dumps(datetime.utcnow() + timedelta(seconds=1), default=date_handler),
        }
        token = jwt.encode(payload, 'Secret Key', algorithm='HS256')
        return token.decode('unicode_escape')

    @staticmethod
    def decode_jwt_token(token):
        return jwt.decode(token, 'Secret Key', algorithms='HS256')

print TokenService.decode_jwt_token('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWRlbnRpdHkiOiJ2aXNocCIsIl9leHAiOiJcIjIwMTYtMDgtMjRUMjA6MDk6MjIuMDQ5NjMxXCIiLCJfaWRwIjoiZGVzaWduLmFyY2hhZWEuaW4iLCJfaWF0IjoiXCIyMDE2LTA4LTI1VDAxOjM5OjIxLjA0OTYwNFwiIn0.3VsotJH_Lv5b11MQLq3z6KDHUOdFHTmMHrOurT_NnqM')
