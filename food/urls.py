from django.urls import path
from . import views

app_name='food'
urlpatterns = [
    #/food/
    path('', views.IndexClassView.as_view(), name='index'),
    #/food/{id}
    path('<int:pk>/', views.FoodDetail.as_view(), name='detail'),  #it was '<int:item_id>/' in function based view
    path('item/', views.item, name='item'),
    # add items
    path('add/', views.CreateItem.as_view(), name='create_item'),
    # edit
    path('update/<int:item_id>/', views.update_item, name='update_item'),
    # delete
    path('delete/<int:item_id>/', views.delete_item, name='delete_item'),
]