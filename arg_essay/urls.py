from django.urls import path, re_path
from . import views


urlpatterns = [

    #path('/', views.deafault, ),

    path('essay_question', views.essayQuestion, name='essay-question'),
    path('claim', views.claim_creator, name='claim-creator'),
    path('body_one', views.body_para_one, name='body-one'),
    path('body_two', views.body_para_two, name='body-two'),
    path('body_three', views.body_para_three, name='body-three'),
    path('essay_view', views.essay_view, name='essay-v'),


    path('essay_question', views.to_essay_question, name='to-essay-question'),
    path('claim', views.to_claim, name='to-claim'),
    path('body_one', views.to_tiqa_one, name='to-tiqa-one'),
    path('body_two', views.to_tiqa_two, name='to-tiqa-two'),
    path('body_three', views.to_tiqa_three, name='to-tiqa-three'),
    path('essay_view', views.to_essay_view, name='to-essay-view'),


    #path('update_field', views.update_field, name='update-field'),
    

]