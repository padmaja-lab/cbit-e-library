from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='library-home'),
    path('it_sems/', views.it_sems, name='library-it-sems'),
    path('cse_sems/', views.cse_sems, name='library-cse-sems'),
    path('ece_sems/', views.ece_sems, name='library-ece-sems'),
    path('eee_sems/', views.eee_sems, name='library-eee-sems'), 
    path('it_sem1/', views.it_sem1, name='library-it-sem1'), 
    path('it_sem2/', views.it_sem2, name='library-it-sem2'), 
    path('it_sem3/', views.it_sem3, name='library-it-sem3'), 
    path('it_sem4/', views.it_sem4, name='library-it-sem4'), 
    path('it_sem5/', views.it_sem5, name='library-it-sem5'), 
    path('it_sem3_DMA/',views.it_sem3_DMA, name='library-it-sem3-DMA'), 
    path('subjectview_sem3/', views.subjectview_sem3 , name='subjectview_sem3'),
    path('subjectview_sem1/', views.subjectview_sem1 , name='subjectview_sem1'),
    path('subjectview_sem2/', views.subjectview_sem2 , name='subjectview_sem2'),
    path('subjectview_sem4/', views.subjectview_sem4 , name='subjectview_sem4'),
    path('subjectview_sem5/', views.subjectview_sem5 , name='subjectview_sem5'),
    path('subjectview_sem6/', views.subjectview_sem6 , name='subjectview_sem6'),
    path('subjectview_sem7/', views.subjectview_sem7 , name='subjectview_sem7'),
    path('subjectview_sem8/', views.subjectview_sem8 , name='subjectview_sem8'),
  
]
