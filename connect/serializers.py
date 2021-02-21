from rest_framework import serializers
from .models import Memo

class MemoSerializer( serializers.ModelSerializer ):
	class Meta:
		model = Memo
		fields = ( 'content', 'created', 'updated' )
		read_only_fields = ( 'created', 'updated' )