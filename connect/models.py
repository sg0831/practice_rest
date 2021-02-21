from django.db import models

class Memo(models.Model):  # Memo라는 이름의 테이블 생성
	# 글자수의 제한이 없는 텍스트필드 형태의 필드
	content = models.TextField()
	# 데이터가 생성된 날짜를 DateTime형식으로 갖는 필드
	created = models.DateTimeField( auto_now_add = True )
	# 데이터가 마지막으로 수정된 날짜를 DateTime형식으로 갖는 필드
	updated = models.DateTimeField( auto_now = True )