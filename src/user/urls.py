from django.http import HttpRequest
from ninja import Router

from config.response import ErrorResponse, ObjectResponse, error_response, response
from user.authentication import authentication_service
from user.exceptions import UserNotFoundException
from user.request import UserLoginRequestBody
from user.response import UserTokenResponse
from user.models import ServiceUser

router = Router(tags=["Users"])


@router.post(
    "/login",
    response={
        200: ObjectResponse[UserTokenResponse],
        404: ObjectResponse[ErrorResponse],
    },
)
def user_login_handler(request: HttpRequest, body: UserLoginRequestBody):
    try:
        user = ServiceUser.objects.get(email=body.email)
    except ServiceUser.DoesNotExist:
        return 404, error_response(msg=UserNotFoundException.message)
    return 200, response(
        {"token": authentication_service.encode_token(user_id=user.id)}
    )
