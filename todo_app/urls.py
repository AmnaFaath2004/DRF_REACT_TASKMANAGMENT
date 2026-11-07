from django.urls import path, include
from rest_framework.routers import DefaultRouter
from todo_app.views import TodoView

router = DefaultRouter()
router.register(r'TodoView', TodoView, basename='TodoView')

urlpatterns = [
  path('', include(router.urls)),

]
