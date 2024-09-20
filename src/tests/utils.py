from django.test import Client

"""
django.test 의 Client는 기본값이 content_type=MULTIPART_CONTENT
content_type="application/json"를 주로 사용하기 때문에 오버랩해서 사용
"""
class APIClient(Client):
    def post(
        self,
        path,
        data=None,
        content_type="application/json",
        follow=False,
        secure=False,
        *,
        headers=None,
        **extra,
    ):
        return super().post(
            path=path,
            data=data,
            content_type=content_type,
            follow=follow,
            secure=secure,
            headers=headers,
            **extra,
        )