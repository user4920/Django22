from django.urls import path
from . import views

urlpatterns = [ #IP주소/blog
    path('', views.PostList.as_view()), #인덱스부분 클래스로 대체
    path('<int:pk>/', views.PostDetail.as_view()),
    path('category/<str:slug>/', views.category_page), #IP주소/blog/category/slug/
    path('tag/<str:slug>/', views.tag_page), #IP주소/blog/tag/slug

    #path('', views.index), #IP주소/blog
    #path('<int:pk>/', views.single_post_page),
]