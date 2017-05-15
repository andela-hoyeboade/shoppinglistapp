from account.forms import LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse
from django.shortcuts import redirect, render
from django.template import RequestContext
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'account/index.html'
    form_class = LoginForm

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['loginform'] = LoginForm()
        return context

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect(reverse('shop_list'))

            messages.add_message(request, messages.ERROR,
                                 'Your account has been disabled')
            return redirect(reverse('index'),
                            context_instance=RequestContext(request))
        else:
            messages.add_message(request, messages.ERROR,
                                 'Incorrect username or password')
            return redirect(reverse('index'),
                            context_instance=RequestContext(request))
