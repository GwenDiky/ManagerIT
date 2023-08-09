from django.urls import path
from main.views import index, by_status
from main.views import TaskCreateView #представление
from main import views
from django.contrib import admin
from .feeds import LatestTasksFeed

app_name = "main" #именное пространство

#маршрутизатор
urlpatterns = [
    path('', index, name="home"),
    #path('all_tasks/', views.all_tasks, name="all_tasks"),
    path('all_tasks/', views.AllTasksView.as_view(), name="all_tasks"),
    path('<int:status_id>/', views.by_status, name="by_status"), #именованный маршрут
    path('add/', TaskCreateView.as_view(), name='add'),
    path('<int:year>/<int:month>/<int:day>/<slug:task>/', views.task_detail, name='task_detail'),
    path('<int:task_id>/share/', views.task_share, name="task_share"),
    path('<int:task_id>/comment/', views.task_comment, name="task_comment"),
    path('tag/<slug:tag_slug>/', views.index, name = "task_list_by_tag"),
    # <int:id> - конвертер пути
    path('feed/', LatestTasksFeed(), name='task_feed'),
    path('search/', views.task_search, name="task_search"),
]


admin.site.header = "IT PROJECT MANAGER"
admin.site.site_title = "Browser Title"
admin.site.index_title = "Welcom To IT Project Manager"