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


