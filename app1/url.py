from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index_page'),
    url(r'^page/(?P<id>\d+)/$', views.page, name="inner_page"),
    url(r'^comments/$', views.comments, name="comment_page"),
    url(r'^app_list/$', views.App1List.as_view()),
]