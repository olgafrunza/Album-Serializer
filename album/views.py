from django.shortcuts import HttpResponse
from .models import Genre, Album, Artist, Song
from .serializers import GenreSerializer, AlbumSerializer, ArtistSerializer, SongSerializer 
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

def home(request):
    return HttpResponse('<h1>API Page</h1>')

class GenreView(ListCreateAPIView):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()

class GenreDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()

class AlbumView(ListCreateAPIView):
    serializer_class = AlbumSerializer
    queryset = Album.objects.all()

class AlbumDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = AlbumSerializer
    queryset = Album.objects.all()

class ArtistView(ListCreateAPIView):
    serializer_class = ArtistSerializer
    queryset = Artist.objects.all()

class ArtistDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = ArtistSerializer
    queryset = Artist.objects.all()

class SongView(ListCreateAPIView):
    serializer_class = SongSerializer
    queryset = Song.objects.all()

class SongDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = SongSerializer
    queryset = Song.objects.all()