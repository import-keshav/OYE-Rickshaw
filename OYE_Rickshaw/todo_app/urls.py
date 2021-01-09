from django.urls import path

from . import views
urlpatterns = [
	path('get-todo', views.GetTODO.as_view()),
	path('create-todo', views.CreateTODO.as_view()),
	path('update-todo/<int:pk>', views.UpdateTODO.as_view()),
	path('delete-todo/<int:pk>', views.DeleteTODO.as_view()),
	path('search-todo', views.SearchTODO.as_view()),
]