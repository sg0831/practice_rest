# url 맵핑을 위한 path, include
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import MemoView

memo_list = MemoView.as_view({
	'post': 'create',
	'get': 'list'
})
memo_detail = MemoView.as_view({
	'get': 'retrieve',
	'put': 'update',
	'patch': 'partial_update',
	'delete': 'destroy'
})

urlpatterns = format_suffix_patterns([
	path('auth/', include('rest_framework.urls', namespace='rest_framework')),
	path('', memo_list, name='memo_list'),
	path('<int:pk>/', memo_detail, name='memo_detail'),
])