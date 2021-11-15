from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic
from data_manager.models import Case, Masspoint

# from .forms import NewCaseForm, EditCaseForm, AddMasspointForm, EditMasspointForm


class sphere(generic.ListView):
    template_name = "data_explorer/explorer.html"
    context_object_name = "masspoints_list"

    def get_queryset(self):
        return Masspoint.objects.filter(id = self.kwargs["case_id"])

    def get_context_data(self, **kwargs):
        case_id = self.kwargs["case_id"]
        context = super().get_context_data(**kwargs)
        context["case_id"] = self.kwargs["case_id"]
        context["masspoints_list"] = Masspoint.objects.filter(case_id = case_id)
        return context
