from xml.etree.ElementInclude import include
from django.urls import path, include 
from. import views
from rest_framework_simplejwt import views as jwt_views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register("register", views.createProject)

urlpatterns = [

    path('Project/', views.getProjectDetail.as_view()),

    # path('Project/create/', views.createProject.as_view()),
    path('Project/create/', include(router.urls)),

    path('Project/search/', views.searchProject.as_view()),

    path('Project/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
   
    path('Project/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    
    path('Project/user/', views.Users.as_view()),

    path('Project/notice/', views.getNotification.as_view()),

    path('Project/delete/', views.delete.as_view()),



]
