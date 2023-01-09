from django.urls import path
from . import views
# (.) se refere a pasta o qual estou.

urlpatterns = [
    path('cadastro/', views.cadastro, name="cadastro")

]