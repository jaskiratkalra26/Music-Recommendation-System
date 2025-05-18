from django.shortcuts import render,HttpResponse
from page.models import Song


import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import os
import base64
load_dotenv()
client_id = os.getenv('client_id')
client_secret = os.getenv('client_secret')

def get_url(Song):
    auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(auth_manager=auth_manager)

    results = sp.search(q=Song, type='track', limit=1)
    track = results['tracks']['items'][0]

    album_images = track['album']['images']
    return album_images[0]['url']
# Create your views here.
import pickle
with open('recommendation_system.pkl','rb') as file:
    data = pickle.load(file)
newdf = data['newdf']
similarity = data['similarity']
def recommend(music):
    music_index = newdf[newdf['name'] == music].index[0]
    distances = similarity[music_index]
    music_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    musics = []
    for i in music_list:
        musics.append(newdf.iloc[i[0]]['name'])
    return musics


from django.views.decorators.csrf import requires_csrf_token
@requires_csrf_token

def index(request):
    newdf = data['newdf']
    options = newdf['name'].tolist()
    
    return render(request,'base.html',{'options':options})


def Data(request):
    if request.method == "POST":
        choice = request.POST.get('choice')
        
        Data = Song(choice= choice)
        
        
        Data.save()
        musics = recommend(str(choice).strip())
        cover_url = []
        for i in musics:
            cover_url.append(get_url(i))
        final = [(music,url) for music,url in zip(musics,cover_url)]
        
        
    
    return render(request,'submit.html',{'musics':final})






    








        
    


