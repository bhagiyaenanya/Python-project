"""mainproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from library import views as bms
urlpatterns = [
    path('admin/', admin.site.urls),
    path('signin',bms.signin,name='signin'),
    path('index',bms.index,name='index'),
    path('signup',bms.signup,name='signup'),
    path('sign',bms.sign,name='sign'),
    path('star',bms.star,name='star'),
    path('sun',bms.sun,name='sun'),
    path('login',bms.login,name='login'),
    path('add',bms.add,name='add'),
    path('order',bms.order,name='order'),
    path('book',bms.book,name='book'),
    path('add1',bms.add1,name='add1'),
    path('edit/(P<ps>\d+)/$', bms.edit,name='edit'),
    path('edit1/(P<pk>\d+)/$', bms.edit1,name='edit1'),
    path('table/(P<rr>\d+)/$', bms.table, name='table'),
    path('table1/(P<rd>\d+)/$', bms.table1, name='table1'),
]
