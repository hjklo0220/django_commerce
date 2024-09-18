from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI

base_api = NinjaAPI(title="djangoshop", version="0.0.0")


@base_api.get("")
def health_check_handler(request):
    return {"ping": "pong"}


urlpatterns = [
    path("", base_api.urls),
    path("admin/", admin.site.urls),
]
