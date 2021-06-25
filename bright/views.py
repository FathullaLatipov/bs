from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from bright.forms import CreateUserForm


def RegisterPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Аккаунт создан для' + user)

            return redirect('pages:login')

    context = {'form': form}
    return render(request, './register.html', context)


def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('pages:home')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, './login.html', context)


def LogOutUser(request):
    logout(request)
    return redirect('pages:login')


class HomeView(TemplateView):
    template_name = 'index.html'


class SalesView(TemplateView):
    template_name = 'sales.html'


class SmmView(TemplateView):
    template_name = 'smm.html'


class AdvertisingView(TemplateView):
    template_name = './sales pages/advertising.html'


class ClientView(TemplateView):
    template_name = './sales pages/client.html'


class ClientsView(TemplateView):
    template_name = './sales pages/clients.html'


class IntroductionView(TemplateView):
    template_name = './sales pages/introduction.html'


class MarketingView(TemplateView):
    template_name = './sales pages/marketing.html'


class VideoProductionView(TemplateView):
    template_name = './sales pages/videoproduction.html'


class WebView(TemplateView):
    template_name = './sales pages/web.html'


# smm
class Brif1View(TemplateView):
    template_name = './smm pages/brif1.html'


class Brif2View(TemplateView):
    template_name = './smm pages/brif2.html'


class CommunictyView(TemplateView):
    template_name = './smm pages/communicty.html'


class LigmagnitView(TemplateView):
    template_name = './smm pages/ligmagnit.html'


class RetargetView(TemplateView):
    template_name = './smm pages/retarget.html'


class TargetView(TemplateView):
    template_name = './smm pages/target.html'


class Target1View(TemplateView):
    template_name = './smm pages/target1.html'


class Target2View(TemplateView):
    template_name = './smm pages/target2.html'


class Target3View(TemplateView):
    template_name = './smm pages/target3.html'


class WhysmmView(TemplateView):
    template_name = './smm pages/why_smm.html'
