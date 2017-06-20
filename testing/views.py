from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect, render_to_response
from testing.forms import RegistrationForm, EditProfileForm, Form3_form
from testing.models import Document, Form1, Form3
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.template.loader import get_template 
from django.template import Context
from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils.encoding import smart_str
import os
from django.conf import settings
from django.views.static import serve

from testing.forms import Form1_form



def HomePageView(request):
  template = get_template('index.html')
  variables = Context({ 'user': request.user })
  output = template.render(variables)
  return HttpResponse(output)


def register_page(request):
    if request.method == 'POST':
      form = RegistrationForm(request.POST, request.FILES)
      if form.is_valid():
        user = User.objects.create_user(username=form.cleaned_data['username'],password=form.cleaned_data['password1'],email=form.cleaned_data['email'])
        user.first_name=form.cleaned_data['first_name']
        user.last_name=form.cleaned_data['last_name']
        user.save()
        if form.cleaned_data['itemsField'] == '1':
          
          g = Group.objects.get(name='WGWP')
          g.user_set.add(user)
        else:
          
          g = Group.objects.get(name='GO')
          g.user_set.add(user)
        
        newdoc = Document(docfile = request.FILES['docfile'])
        newdoc.save()
        return HttpResponseRedirect('/')
    else:
      form = RegistrationForm()

    variables = RequestContext(request, {'form': form})
    return render_to_response('registration/register.html',variables)


def logout_page(request):
  logout(request)
  return HttpResponseRedirect('/')

def faq(request):
  return HttpResponseRedirect('/')


def profile_view(request):
  user = request.user
  form = EditProfileForm(initial={'first_name':user.first_name, 'last_name':user.last_name})
  context = {
    "form":form
  }  
  return render(request, 'registration/profile.html', context)

def edit_profile(request):
  user = request.user
  form = EditProfileForm(request.POST or None, initial={'first_name':user.first_name, 'last_name':user.last_name})
  if request.method == 'POST':
    if form.is_valid():
      user.first_name = request.POST['first_name']
      user.last_name = request.POST['last_name']
      user.save()
      return HttpResponseRedirect('/profile')

  context={
    "form":form
  }
  return render(request,'registration/edit_profile.html', context)


def download_page(request):
  
  filepath=settings.MEDIA_ROOT+'/SWM_2016.pdf'
  return serve(request, os.path.basename(filepath), os.path.dirname(filepath))


def frm1(request):
  form = Form1_form
  user = request.user
  if  request.method=="POST":
    form = Form1_form(request.POST)
    feed_cont = form.save(commit=False)
    feed_cont.user=request.user
    feed_cont.save()
    if form.is_valid():
      form.save()
      return HttpResponseRedirect('/')
    else:
       form=Form1_form()
  return render_to_response('registration/form1.html',{'form': form} , context_instance=RequestContext(request))


def frm3(request):
  form = Form3_form
  user = request.user
  if  request.method=="POST":
    form = Form3_form(request.POST)
    if form.is_valid():
      feed_cont = form.save(commit=False)
      feed_cont.user=request.user
      feed_cont.save()
      newdoc = Form3(ww_waste = request.FILES['ww_waste'])
      newdoc.save()
        
      form.save()
      return HttpResponseRedirect('/')
    else:
       form=Form3_form()
  return render_to_response('registration/form3.html',{'form': form} , context_instance=RequestContext(request))



