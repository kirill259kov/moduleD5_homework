from django.urls import path, include
from .views import PostsList, PostDetail, PostSearch, AddList, PostEdit, PostDelete

urlpatterns = [
    path('', PostsList.as_view()),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('search/', PostSearch.as_view(), name='post_search'),
    path('add/', AddList.as_view(), name='post_add'),
    path('<int:pk>/edit/', PostEdit.as_view(), name='post_edit'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    # path('accounts/', include('accounts.urls')),
]