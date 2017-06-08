from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, render_to_response
from testing.forms import RegistrationForm
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.template.loader import get_template 
from django.template import Context

"""
from testing.forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})



"""

from django.shortcuts import render

from django.views.generic import TemplateView

# Create your views here.
#class HomePageView(TemplateView):
#    def get(self, request, **kwargs):
#        return render(request, 'index.html')

def HomePageView(request):
  template = get_template('index.html')
  variables = Context({ 'user': request.user })
  output = template.render(variables)
  return HttpResponse(output)


def register_page(request):
    if request.method == 'POST':
      form = RegistrationForm(request.POST)
      if form.is_valid():
        user = User.objects.create_user(username=form.cleaned_data['username'],password=form.cleaned_data['password1'],email=form.cleaned_data['email'])
        return HttpResponseRedirect('/')
    else:
      form = RegistrationForm()
      
    variables = RequestContext(request, {'form': form})
    return render_to_response('registration/register.html',variables)


def logout_page(request):
  logout(request)
  return HttpResponseRedirect('/')
"""

# Create your views here.
from testing.forms import BookForm

def save_book(request):  
  form = BookForm
  if request.POST:
     form = BookForm(request.POST)
     if form.is_valid():
        form.save()
  return render_to_response('book.html.html',{'form': form} ,                 context_instance=RequestContext(request))
"""  