from django.shortcuts import render,HttpResponse
from page.models import Song



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
        print(musics)
    
    return render(request,'submit.html',{'musics':musics})







        
    


