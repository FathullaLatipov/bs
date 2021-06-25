from django.urls import path

from bright.views import HomeView, SalesView, SmmView, AdvertisingView, ClientView, ClientsView, IntroductionView, \
    MarketingView, VideoProductionView, WebView, Brif1View, Brif2View, CommunictyView, LigmagnitView, RetargetView, \
    TargetView, Target1View, Target2View, Target3View, WhysmmView, RegisterPage, LoginPage, LogOutUser

app_name = 'pages'

urlpatterns = [
    path('sales/', SalesView.as_view(), name='sales'),
    path('smm/', SmmView.as_view(), name='smm'),
    path('advertising/', AdvertisingView.as_view(), name='advertising'),
    path('client/', ClientView.as_view(), name='client'),
    path('clients/', ClientsView.as_view(), name='clients'),
    path('introduction/', IntroductionView.as_view(), name='introduction'),
    path('marketing/', MarketingView.as_view(), name='marketing'),
    path('videoproduction/', VideoProductionView.as_view(), name='videoproduction'),
    path('web/', WebView.as_view(), name='web'),
    path('brif1/', Brif1View.as_view(), name='brif1'),
    path('brif2/', Brif2View.as_view(), name='brif2'),
    path('communicty/', CommunictyView.as_view(), name='communicty'),
    path('ligmagnit/', LigmagnitView.as_view(), name='ligmagnit'),
    path('retarget/', RetargetView.as_view(), name='retarget'),
    path('ctarget/', TargetView.as_view(), name='target'),
    path('ctarget1/', Target1View.as_view(), name='target1'),
    path('ctarget2/', Target2View.as_view(), name='target2'),
    path('ctarget3/', Target3View.as_view(), name='target3'),
    path('whysmm/', WhysmmView.as_view(), name='whysmm'),
    path('login/', LoginPage, name='login'),
    path('register/',  RegisterPage,  name='register'),
    path('', LogOutUser, name='logout'),
    path('home', HomeView.as_view(), name='home')
]