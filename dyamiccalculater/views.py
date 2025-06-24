from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from app.models import Formula


def home(request):
    fromulas = Formula.objects.all()
    return render(request, 'home.html', {'formulas': fromulas})

# views.py

from django.shortcuts import render, get_object_or_404

def solve_formula_view(request, pk):
    formula = get_object_or_404(Formula, pk=pk)
    count = formula.variables
    print(count)
    var_name = [f'x{i+1}' for i in range(count)]
    print(var_name)
    

    return render(request, "fromula.html", {
        "formula": formula,
        "var_name": var_name,
        "count": count,
    })

    

