from django.urls import path

from . import views

app_name = 'projects'
urlpatterns = [
    # ---Projects---
    path(
        'projects/',
        views.ProjectListView.as_view(),
        name='projects_list'
    ),
    path(
        'project/create/',
        views.ProjectCreate.as_view(),
        name='project_create',
    ),
    path(
        'project/<slug:slug>/',
        views.ProjectDetailView.as_view(),
        name='project_detail'
    ),
    path(
        'project/<slug:slug>/update/',
        views.ProjectUpdate.as_view(),
        name='project_update'
    ),
    path(
        'project/<slug:slug>/delete/',
        views.ProjectDelete.as_view(),
        name='project_delete'
    ),
    # ---END Projects---
    # ---Tasks---
    path(
        'tasks/',
        views.TaskListView.as_view(),
        name='tasks_list'
    ),
    path(
        'task/create/',
        views.TaskCreate.as_view(),
        name='task_create'
    ),
    path(
        'task/<slug:slug>/',
        views.TaskDetailView.as_view(),
        name='task_detail'
    ),
    path(
        'task/<slug:slug>/update/',
        views.TaskUpdate.as_view(),
        name='task_update'
    ),
    path(
        'task/<slug:slug>/delete/',
        views.TaskDelete.as_view(),
        name='task_delete'
    ),
    # ---END Tasks---
    # ---Brands---
    path(
        'brands/',
        views.BrandListView.as_view(),
        name='brands_list'
    ),
    path(
        'brand/create/',
        views.BrandCreate.as_view(),
        name='brand_create',
    ),
    path(
        'brand/<slug:slug>/',
        views.BrandDetailView.as_view(),
        name='brand_detail'
    ),
    path(
        'brand/<slug:slug>/update/',
        views.BrandUpdate.as_view(),
        name='brand_update'
    ),
    path(
        'brand/<slug:slug>/delete/',
        views.BrandDelete.as_view(),
        name='brand_delete'
    ),
    # ---END Brand---
    # ---Statuses---
    path(
        'statuses/',
        views.StatusListView.as_view(),
        name='statuses_list'
    ),
    path(
        'status/create/',
        views.StatusCreate.as_view(),
        name='status_create',
    ),
    path(
        'status/<slug:slug>/',
        views.StatusDetailView.as_view(),
        name='status_detail'
    ),
    path(
        'status/<slug:slug>/update/',
        views.StatusUpdate.as_view(),
        name='status_update'
    ),
    path(
        'status/<slug:slug>/delete/',
        views.StatusDelete.as_view(),
        name='status_delete'
    ),
    # ---END Status---
    path(
        'message',
        views.MessageCreate.as_view(),
        name='add_message'
    ),

]
