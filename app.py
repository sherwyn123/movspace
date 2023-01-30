import streamlit as st
from multiapp import MultiApp
from apps import home

app = MultiApp()

#st.markdown("""
## Multi-Page App
#This multi-page app is using the [streamlit-multiapps](https://github.com/upraneelnihar/streamlit-multiapps) framework developed by [Praneel Nihar](https://medium.com/@u.praneel.nihar). Also check out his [Medium article](https://medium.com/@u.praneel.nihar/building-multi-page-web-app-using-streamlit-7a40d55fa5b4).
#""")
import streamlit as st
import pickle#to copy the main daaa
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=dad7b6ea7c596a86a77f9ce34a954055&language=en-US".format(movie_id))
    data = response.json()#converts to json
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x: x[1])[1:6]#gets the first 5 similar vectors and stores in a variable
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in movie_list:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id

        recommended_movie_names.append(movies.iloc[i[0]].title)
        recommended_movie_posters.append(fetch_poster(movie_id))

    return recommended_movie_names,recommended_movie_posters

movies_dict = pickle.load(open('movie_dictionary.pkl','rb'))#opens the diction in read binary mode
movies=pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))

st.title('MOVIE SPACE')
movie_list=movies['title'].values
selected_movie_name = st.selectbox(
    'Please Enter Your Movie',
    movies['title'].values#list all the values from the dataset in the search menu
)

if st.button('Recommend'):
    names,posters = recommend(selected_movie_name)#stores the selected movie and its poster in these 2 variables
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0],use_column_width=True)
    with col2:
        st.text(names[1])
        st.image(posters[1],use_column_width=True)

    with col3:
        st.text(names[2])
        st.image(posters[2],use_column_width=True)
    with col4:
        st.text(names[3])
        st.image(posters[3],use_column_width=True)
    with col5:
        st.text(names[4])
        st.image(posters[4],use_column_width=True)


# Add all your application here
app.add_app("Home", home.app)
# The main app
app.run()