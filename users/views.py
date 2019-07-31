from django.shortcuts import render, HttpResponse
from users.models import User
from django.shortcuts import HttpResponseRedirect, reverse

# Create your views here.


def render_register_user_form(request):
    template = 'users/register_user_form.html'
    return render(request, template)


def process_register_user_form(request):
    if request.method == 'POST':
        new_user = User(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email=request.POST['email'],
            password=request.POST['password']
        )
        new_user.save()
        return HttpResponseRedirect(reverse('users:login')) # 5. Redirect user to login form.
    return HttpResponse('Error: method not allowed.')


def render_login_user_form(request): # 1. Make sure we pass a request parameter in our function.
    template = 'users/login_user_form.html' # 2. Define the template that is being rendered.
    return render(request, template) # 3. Return the render function with its necessary parameters.


def process_login_user_form(request): # 1. Make sure we pass a request parameter in our function.
    if request.method == 'POST': # 2. Check if incoming request method is POST.
        try:
            user = User.objects.get(email=request.POST['email'], password=request.POST['password'])
        except User.DoesNotExist:
            return HttpResponse('User does not exist.')

        return HttpResponseRedirect(reverse('books:catalogue', kwargs={'user_id': user.id})) # 5. Redirect user to book catalogue.
    return HttpResponse('Error: method not allowed.')