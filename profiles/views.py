from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.views.generic import (TemplateView,
                                    View,
                                    UpdateView,
                                    ListView,
                                    DetailView, )
from django.shortcuts import render, get_object_or_404,redirect, HttpResponseRedirect

from .forms import UserForm, ProfileForm
from .models import Profile


User = get_user_model()


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profiles/profile.html'


class ProfileListView(ListView):
    queryset = Profile.objects.all()


class UserDetailView(DetailView):
    queryset = Profile.objects.all()
    template_name = "profiles/profile.html"

    def get_object(self):
        return get_object_or_404(User, username__iexact=self.kwargs.get("username"))


@login_required
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return HttpResponseRedirect('/portal/index')

    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'profiles/update.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })




