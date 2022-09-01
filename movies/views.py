from rest_framework import generics
from .serializer import MovieSerializer
from .models import Movie
from .permissions import IsOwnerOrReadOnly


class MovieList(generics.ListAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieDetail(generics.RetrieveAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
