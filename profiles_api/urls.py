from django.urls import path,include
from rest_framework.routers import DefaultRouter
from profiles_api import views

router=DefaultRouter()
router.register('Hello-viewset',views.HelloViewSet,base_name='hello-viewset')
router.register('profile',views.UserProfileViewSet)

urlpatterns=[
    path('hello-view/',views.HelloApiView.as_view()),
    path('login/',views.UserLoginAPiView.as_view()),
    path('',include(router.urls)),
]
