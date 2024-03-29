from django.contrib import admin
from django.urls import path , include
import api.views as views

urlpatterns = [
   path('',views.api_index_view,name='api_index'),
   path('ratereview/<str:review>',views.ratereview,name='ratereview'),
   path('wordcounter/<str:sentence>',views.wordcounter,name='wordcounter'),
   path('wordcounterapi/',views.wordcounterView,name='wordcounterapi'),
]
