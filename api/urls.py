from django.urls import path


from .views import (
    DreamCreateView,
      DreamListView,
        DreamCategoryListView,
          DreamDetailView,
            DreamModifyView,
              DreamDeleteView,)

urlpatterns = [

    path('dream/',                 DreamListView.as_view())          ,#Get
    path('dream/<int:pk>/',        DreamDetailView.as_view())        ,#Get
    path("dream/create/",          DreamCreateView.as_view())        ,#Post
    path('dream/category/',        DreamCategoryListView.as_view())  ,#Get
    path('dream/<int:pk>/modify/', DreamModifyView.as_view())        ,#Put or Patch
    path('dream/<int:pk>/delete/', DreamDeleteView.as_view())        ,#Delete


]