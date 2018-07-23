from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from .models import Post
from django.utils import timezone
from django.views.generic import ListView,DetailView,FormView
from .forms import CreateCommentForm
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
class BlogList(ListView):
    template_name ="blog/blog.html"
    paginate_by = 1

    def get_queryset(self):
        qs =Post.objects.all()
        return qs
    def get_context_data(self, *args, **kwargs):
        context =super(BlogList,self).get_context_data(**kwargs)
        context['blog_list']=self.get_queryset()

        return context


class BlogDetail(FormView):
    form_class = CreateCommentForm
    template_name = "blog/post.html"

    def get_object(self):
        pk=self.kwargs.get('pk')

        post =get_object_or_404(Post,pk=pk)
        return post
    def get_success_url(self):
        return reverse('blog:details',kwargs={'pk',self.get_object().pk})

    def form_valid(self, form):

        instance =form.save(commit=False)
        instance.post=self.get_object()
        instance.user=self.request.user
        print(instance)
        instance.save()

        return super(BlogDetail).form_valid(form)


    def get_context_data(self, **kwargs):
        context =super(BlogDetail,self).get_context_data(**kwargs)
        context['post'] =self.get_object()
        return context
#@login_required(login_url=reverse_lazy('account_login'))
def blog_details(request,pk):
    post=get_object_or_404(Post,pk=pk)
    template_name = "blog/post.html"
    form = CreateCommentForm(request.POST or None)

    context={'post':post,'form':form}
    print(form.data)
    if request.method == "POST":

        if form.is_valid():
                instance =form.save(commit=False)
                instance.post=post
                instance.user=request.user
                print(instance)
                instance.save()
                return HttpResponseRedirect(post.get_absolute_url())

    return render(request,template_name,context)