from django.urls import include, path
from . import views

app_name = "data_manager"

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('new/', views.NewCaseView, name="new_case"),
    path('<int:case_id>/', views.OverviewCaseView.as_view(), name="overview_case"),
    path('<int:case_id>/add/', views.AddMasspointView, name="add_masspoint"),
    path('<int:case_id>/edit/', views.EditCaseView, name="edit_case"),
    path('<int:case_id>/delete/', views.DeleteCaseView, name="delete_case"),
    path('<int:case_id>/<int:masspoint_id>/edit/', views.EditMasspointView, name="edit_masspoint"),
    path('<int:case_id>/<int:masspoint_id>/delete/', views.DeleteMasspointView, name="delete_masspoint"),
]