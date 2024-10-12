from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from .serializers import DreamCategorySerializer, DreamCommentSerializer, DreamSerializer
from .models import DreamCategory, Dream, DreamComment
from rest_framework.permissions import IsAuthenticated, AllowAny
from .permissions import IsObjOwnerOrStaff



# make the dream crud

class DreamListView(ListAPIView,  ):
    permission_classes = [AllowAny]

    serializer_class   = DreamSerializer
    queryset           = Dream.objects.all()
    lookup_field       = 'id'
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
       
class DreamDetailView(RetrieveAPIView):

    permission_classes = [AllowAny]

    serializer_class   = DreamSerializer
    queryset           = Dream.objects.all()
    lookup_field       = 'id'
    
class DreamCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class   = DreamSerializer
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



class DreamModifyView(UpdateAPIView):
    permission_classes = [IsAuthenticated, IsObjOwnerOrStaff]
    serializer_class   = DreamSerializer
    queryset           = Dream.objects.all()
    lookup_field       = 'id'

class DreamDeleteView(DestroyAPIView):
    permission_classes = [IsAuthenticated, IsObjOwnerOrStaff]
    serializer_class   = DreamSerializer
    queryset           = Dream.objects.all()
    lookup_field       = 'id'

# Categories 

class DreamCategoryListView(ListAPIView):
    permission_classes = [AllowAny]

    serializer_class   = DreamCategorySerializer
    queryset           = DreamCategory.objects.all()

