from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

# Essa função abaixo não está protegida
def curriculo_spiff(request):
    return render(request, 'curriculo/curriculospiff.html')

# A função abaixo está protegida. Veja a anotação @login_required
@login_required
def curriculo_spiff_v2(request):
    return render(request, 'curriculo/meucurriculo.html')