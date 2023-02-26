from django.shortcuts import render

# Create your views here.
def inicio(request):
    _context ={}
    return render(request, 'dashboard.html', context = _context)
