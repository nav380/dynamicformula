from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from app.models import Formula
from django.views.decorators.csrf import csrf_exempt



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


@csrf_exempt
def add_formula(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        expression = request.POST.get('expression')
        variables = request.POST.get('variables')
        print(f"Received data: name={name}, expression={expression}, variables={variables}")
        
        formula = Formula.objects.create(
            name=name,
            expression=expression,
            variables=variables
        )
        print(f"Formula created: {formula}")
        
        return redirect('home')
    
    return render(request, 'addformula.html')

    

