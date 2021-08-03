from django.urls import path
from .views import *

urlpatterns = [
    # 전체 studio_concept 조회(컨셉북)
    path('studios/', StudioConceptList.as_view()),
    # 특정 studio_concept 찜 추가/삭제
    path('studios/<int:pk>/like', StudioConceptLike.as_view()),
]
