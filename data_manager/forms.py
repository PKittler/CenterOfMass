from django import forms
from .models import Case, Masspoint


class NewCaseForm(forms.ModelForm):

    class Meta:
        model = Case
        fields = ('name', 'description', 'label_x_max', 'label_x_min', 'label_y_max', 'label_y_min', 'label_z_max', 'label_z_min')


class EditCaseForm(forms.ModelForm):

    class Meta:
        model = Case
        fields = ('name', 'description', 'label_x_max', 'label_x_min', 'label_y_max', 'label_y_min', 'label_z_max', 'label_z_min')


class AddMasspointForm(forms.ModelForm):

    class Meta:
        model = Case
        fields = ('id', 'lastname', 'firstname', 'x_value', 'y_value', 'z_value', 'mass')


class EditMasspointForm(forms.ModelForm):

    class Meta:
        model = Case
        fields = ('id', 'lastname', 'firstname', 'x_value', 'y_value', 'z_value', 'mass')