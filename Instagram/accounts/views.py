from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.contrib.auth.forms import AuthenticationForm

@require_http_methods(['GET', 'POST'])
def login(request):
    if request.user.is_authenticated:
        return redirect('feeds:index')
    
    if request.method=='POST':
        form = AuthenticationForm(request, request.POST)
        input_id = request.POST['username']

        if '@' in  input_id:
            request.POST['username'] = 'admin'

        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)
