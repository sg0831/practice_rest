from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MemoSerializer
from .models import Memo
from rest_framework import permissions

class MemoView( viewsets.ModelViewSet ):
	queryset = Memo.objects.all()
	serializer_class = MemoSerializer
	permission_classes = (permissions.AllowAny,)
		