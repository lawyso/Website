from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView
from allauth.account.adapter import DefaultAccountAdapter
from Ufanisi.forms import ContactForm
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template.loader import get_template
from blog.models import Post


class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        blogs =Post.objects.all().order_by("-id")
        return render(request, 'ufanisi/index.html', context={"blogs":blogs})


class MembersArea(TemplateView):
    template_name = 'portal/index.html'

class AboutPageView(TemplateView):
    template_name = "ufanisi/about.html"

class MissionPageView(TemplateView):
    template_name = "ufanisi/projects.html"

class BlogPageView(TemplateView):
    template_name = "blog/blog.html"

def contact(request):
    form_class = ContactForm

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name'
                , '')
            contact_email = request.POST.get(
                'contact_email'
                , '')
            form_content = request.POST.get('content', '')

            # Email the profile with the
            # contact information
            template =get_template('ufanisi/contact_template.txt')
        context = {
            'contact_name': contact_name,
            'contact_email': contact_email,
            'form_content': form_content,
        }
        content = template.render(context)

        email = EmailMessage(
            "New contact form submission",
            content,
            "Your website" + '',
            ['info@unitedufanisi.org'],
            headers={'Reply-To': contact_email}
        )
        email.send()
        return redirect('/contact/')


    return render(request, 'ufanisi/contact.html', {
    'form': form_class,
})

class ServicePageView(TemplateView):
    template_name = "ufanisi/portal.html"

class SignupClosed(DefaultAccountAdapter):
    def is_open_for_signup(self, request):
        return False
