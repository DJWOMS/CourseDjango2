from django.urls import path

from .views import get_page


urlpatterns = [
    path('<path:url>', get_page, name="page"),
]
