from django.urls import path
from . import views

app_name = "data_explorer"

urlpatterns = [
    path('<int:case_id>/', views.sphere.as_view(), name="sphere"),
]