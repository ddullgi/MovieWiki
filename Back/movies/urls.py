from django.urls import path
from . import views

app_name = "movies"

urlpatterns = [
    # 인기 영화 리스트
    path('list/', views.popular_movie_list_info),
    # 영화 상세 정보
    path('<int:movie_id>/', views.moviedetail),
    # 영화 타이틀 검색
    path('search/<str:q>/', views.search),
    # 장르 필터
    path('genre/<int:genre_id>/', views.genre_filter),
    # 국가 필터
    path('country/<int:country_id>/', views.country_filter),
    # 감독 필터
    path('director/<int:director_id>/', views.director_filter),
    # 배우 필터
    path('actor/<int:actor_id>/', views.actor_filter),
    # 년도 필터
    path('year/<int:year>/', views.year_filter),
    # 날씨
    path('weather/<str:area>/', views.weather),

]