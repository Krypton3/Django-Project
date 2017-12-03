from django.conf.urls import url

from . import views
app_name = 'main'
urlpatterns = [
    # ex: /main/
    url(r'^$', views.IndexView.as_view(), name="index"),
    # ex: /main/5/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name="detail"),
    # ex: /main/5/results/
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name="results"),
    # ex: /main/5/vote/
    url(r'^(?P<pk>[0-9]+)/vote/$', views.vote, name="vote")
]
