from django.urls import path

from . import views

urlpatterns = [
    path('tag/<slug:slug>/', views.PostListView.as_view(), name='tag'),
    path("<slug:category>/<slug:slug>/", views.PostDetailView.as_view(), name="detail_post"),
    path("<slug:category_slug>/", views.PostListView.as_view(), name="category"),
    # path("", views.PostListView.as_view()),
]
