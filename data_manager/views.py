from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic
from .models import Case, Masspoint
from .forms import NewCaseForm, EditCaseForm, AddMasspointForm, EditMasspointForm


class IndexView(generic.ListView):
    template_name = "data_manager/index.html"
    content_object_name = "latest_cases_list"

    def get_queryset(self):
        return Case.objects.order_by('name')


def NewCaseView(request):
    if request.method == "POST":
        form = NewCaseView(request.POST)

        if form.is_valid():
            form.save()

        return redirect('data_manager:index')
    else:
        form = NewCaseForm()
        return render(request, 'data_manager/new_case.html', {'form': form})


def EditCaseView(request, case_id):
    case = get_object_or_404(Case, id = case_id)
    form = EditCaseForm(request.POST or None, instance = case)

    if form.is_valid():
        case = form.save(commit=False)
        case.save()

        return redirect('data_manager:index')
    else:
        form = EditCaseForm(request.POST or None, instance = case)
        return render(request, 'data_manager/edit_case.html', {'form': form})


def DeleteCaseView(request, case_id):
    Case.objects.filter(id = case_id).delete()
    return redirect("data_manager:index")


class OverviewCaseView(generic.ListView):
    template_name = "data_manager/masspoints.html"
    content_object_name = "masspoints_list"

    def get_queryset(self):
        return Masspoint.objects.filter(id = self.kwargs["case_id"])

    def get_context_data(self, **kwargs):
        case_id = self.kwargs["case_id"]
        context = super().get_context_data(**kwargs)
        context["case_id"] = self.kwargs["case_id"]
        context["masspoints_list"] = Masspoint.objects.filter(case_id = case_id)
        return context


def AddMasspointView(request, case_id):
    case = get_object_or_404(Case, id = case_id)

    if request.method == "POST":
        masspoint = case.masspoint_set.create(lastname = request.POST["lastname"], firstname = request.POST["firstname"], x_value = request.POST["x_value"], y_value = request.POST["y_value"], z_value = request.POST["z_value"], mass = request.POST["mass"])
        return redirect("data_manager:show_masspoints", case_id = case.id)
    else:
        form = AddMasspointForm()
        return  render(request, "data_manager/add_masspoint.html", {'form': form})


def EditMasspointView(request, case_id, masspoint_id):
    masspoint = get_object_or_404(Masspoint, id = masspoint_id)
    form = EditMasspointForm(request.POST or None, instance = masspoint)

    if form.is_valid():
        masspoint = form.save(commit=False)
        masspoint.save()

        return redirect("data_manager:show_masspoints", case_id)
    else:
        form = EditMasspointForm(request.POST or None, instance = masspoint)
        return render(request, "data_manager/edit_masspoint.html", {'form': form})


def DeleteMasspointView(request, case_id, masspoint_id):
    Masspoint.objects.filter(id = masspoint_id).delete()
    return redirect("data_manager:show_masspoints", case_id)


class WDSView(generic.DetailView):
    model = Case
    template_name = "data_manager/add_case.html"