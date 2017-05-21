from django.conf.urls import url

from oneliners import views, ajax

urlpatterns = [
    url(r'^$', views.oneliners_default, name='index'),
    url(r'^sourcecode/$', views.sourcecode, name='sourcecode'),
    url(r'^mission/$', views.mission),
    url(r'^feeds/$', views.feeds),

    url(r'^oneliner/$', views.oneliners_default, name='oneliners_default'),
    url(r'^oneliner/newest/$', views.oneliners_newest, name='oneliners_newest'),
    url(r'^oneliner/popular/$', views.oneliners_popular, name='oneliners_popular'),
    url(r'^oneliner/(?P<pk>\d+)/$', views.oneliner, name='oneliner'),
    url(r'^oneliner/edit/(?P<pk>\d+)/$', views.oneliner_edit),
    url(r'^oneliner/new/$', views.oneliner_new),
    url(r'^oneliner/new/alternative/(?P<oneliner_pk>\d+)/$', views.oneliner_alternative),

    url(r'^profile/(?P<pk>\d+)/$', views.profile, name='profile'),
    url(r'^profile/(?P<pk>\d+)/oneliners/$', views.profile_oneliners, name='profile_oneliners'),
    url(r'^profile/$', views.profile),
    url(r'^profile/edit/$', views.profile_edit),
    url(r'^profile/oneliners/$', views.profile_oneliners),
    url(r'^profile/votes/$', views.profile_votes, name='profile_votes'),

    url(r'^search/$', views.search, name='search'),

    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout),

    url(r'^help/markdown/$', views.help_markdown),
]

urlpatterns += [
    url(r'^ajax/oneliner/(?P<oneliner_pk>\d+)/vote/$', ajax.oneliner_vote),
    url(r'^ajax/search/$', ajax.search),
    url(r'^ajax/search/tag/$', ajax.search_by_tag, name='search_by_tag'),
]
