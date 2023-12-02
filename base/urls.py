from django.urls import path
from .  import views
from django.conf.urls.static import static
urlpatterns = [
    path('login/',views.loginPage,name="login"),
    path('register/',views.rgPage,name="register"),
    path('',views.homePage,name="home"),
    path('scan/',views.scan,name="scan"),
    path('result/',views.result,name="result"),
    
    
    
]
