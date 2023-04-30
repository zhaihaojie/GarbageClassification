from django.urls import path, re_path
from . import views

# namespace
# app_name = 'tasks'
'''
    在根目录urls include时 格式为 include((app.urls,app_name),namespace) 时 此处不用指定app_name
    若是include(app.urls,namespace)则需要
'''

urlpatterns = [
    # retrieve 检索 task list
    path('', views.task_list, name='task_list'),
    # create a task
    path('create', views.task_create, name='task_create'),
    # retrieve single task object
    # ?P<pk> 表明这一组变量命名为pk
    re_path(r'^(?P<pk>\d+)/$', views.task_detail, name='task_detail'),
    # delete a task
    re_path(r'^(?P<pk>\d+)/delete/$', views.task_delete, name='task_delete'),
    # update a task
    re_path(r'^(?P<pk>\d+)/update/$', views.task_update, name='task_update')
]
