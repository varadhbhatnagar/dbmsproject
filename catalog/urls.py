from django.conf.urls import url
from . import views

app_name = 'catalog'
urlpatterns=[

    url(r'^(?P<cat_id>[0-9]+)/$',views.detail, name='detail'),
    url(r'^$', views.index , name='index'),
    url(r'^(?P<cat_id>[0-9]+)/detail/(?P<product_id>[0-9]+)/$', views.element , name='element'),
    url(r'^user/(?P<user_id>[0-9]+)/$', views.userdetail, name='user')
]