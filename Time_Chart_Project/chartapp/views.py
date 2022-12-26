from django.shortcuts import render, redirect
from . models import budget
from . forms import BudgetForm

# Create your views here.

def index(request):
    budgets = budget.objects.all()

    if request.method == 'POST':
        form = BudgetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = BudgetForm()        

    context = {
        "budgets": budgets,
        "form": form
    }

    return render(request, 'chartapp/index.html', context)
