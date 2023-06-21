from django.shortcuts import render, redirect
from .models import District, Branch

def home(request):
    return render(request, 'home.html')

def login(request):
    if request.method == 'POST':
        # Handle login form submission
        username = request.POST['username']
        password = request.POST['password']
        # Perform authentication logic
        return redirect('new_page')
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Perform registration logic here

        return redirect('login')

    return render(request, 'register.html')

def new_page(request):
    return render(request, 'new_page.html', {'districts': District.objects.all()})

def get_branches(request):
    district_id = request.GET.get('district_id')
    branches = Branch.objects.filter(district_id=district_id)
    return render(request, 'branch_dropdown.html', {'branches': branches})
