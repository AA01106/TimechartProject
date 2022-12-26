from django import forms
from . models import budget

class BudgetForm(forms.ModelForm):
    class Meta:
        model = budget
        fields = '__all__'
        widgets = {
            'category': forms.TextInput(attrs={'class': 'form-control'}),
            'num_of_budget': forms.TextInput(attrs={'class': 'form-control'}),
        }
