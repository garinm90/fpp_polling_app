from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.fields import CurrentUserDefault
from .models import Show, Playlist
from .serializers import ShowSerializer, PlaylistSerializer


# class ShowListView(generics.CreateAPIView):
#     serializer_class = ShowSerializer

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)


# class ShowDeleteView(generics.DestroyAPIView):
#     serializer_class = ShowSerializer

#     def get_queryset(self):
#         user = self.request.user
#         return user.show.all()


class ShowViewSet(viewsets.ModelViewSet):
    serializer_class = ShowSerializer
    queryset = 
    def get_queryset(self):
        user = self.request.user
        # This is a stupid hack because it expects a list of crap.
        # I have no idea how to make this work one to one :|
        get_object_or_404()
        show_list = [user.show]
        return show_list
