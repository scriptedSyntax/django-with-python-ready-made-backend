from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import Collection, Piece
from django.views import generic
from . forms import UserForm
from django.contrib.auth import authenticate,login
from django.views.generic import View
# Create your views here.

class IndexView(generic.ListView):
    template_name = 'genre/genretemplate.html'

    def get_queryset(self):
        return Collection.objects.all()

class DetailsView(generic.DetailView):  #return detail of an object
    model=Collection
    template_name = 'genre/detailstemplate.html'


class UserFormView(View):
    form_class=UserForm
    template_name='genre/formtemplate.html'

    def get(self,request):
        form=self.form_class(None)
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form=self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)  # Prevents premature saving
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)  # Encrypts the password
            user.save()  # Now save the user

            newuser=authenticate(username=username,password=password)

            if newuser is not None:
                if newuser.is_active:
                    login(request, newuser)
                    return redirect("/genre")

        return render(request, self.template_name, {'form':form})

# ##################################################################break here################
# from django.shortcuts import render, redirect
# from django.http import HttpResponse
# from django.contrib.auth import authenticate, login
# from django.views import generic, View
# from django.urls import reverse
# from .models import Collection, Piece
# from .forms import UserForm
#
#
# class index(generic.ListView):
#     template_name = 'genre/genretemplate.html'
#
#     def get_queryset(self):
#         return Collection.objects.all()
#
#
# class details(generic.DetailView):
#     model = Collection
#     template_name = 'genre/detailstemplate.html'
#
#
# class UserFormView(View):
#     form_class = UserForm
#     template_name = 'genre/formtemplate.html'
#
#     def get(self, request):
#         form = self.form_class()
#         return render(request, self.template_name, {'form': form})
#
#     def post(self, request):
#         form = self.form_class(request.POST)
#
#         if form.is_valid():
#             user = form.save(commit=False)
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user.set_password(password)
#             user.save()
#
#             newuser = authenticate(username=username, password=password)
#
#             if newuser is not None:
#                 if newuser.is_active:
#                     login(request, newuser)
#                     return redirect(reverse("index"))
#
#         return render(request, self.template_name, {'form': form})
