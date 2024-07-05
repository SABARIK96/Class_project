import streamlit as st
import pickle as pkl 
import pandas as pd 
import requests


def fetch_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=b2207a8c606175bdd3f80ca0485ce8c0'.format(movie_id))
    data= response.json()
    return 'https://image.tmdb.org/t/p/w300/'+data['poster_path']



def recommended(movie):
    movie_index=movies[movies['title']== movie].index[0]
    distances = similairty[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]

    recommended_movies=[]
    recommended_movies_posters=[]
    for i in movies_list:
        movie_id = movies.iloc[i[0]].id
        #fetching poster right now with the help of API
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters

# for importinh the movies from datframe 
movies_dict =pkl.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similairty= movies_dict =pkl.load(open('similarity.pkl','rb'))

#for making the title 
st.title('Movie recommender system')
selected_movie_name = st.selectbox(
    "How would you like to be contacted?",
    movies['title'].values)

#create a button for recommendation 

if st.button("Recommended"):
    names,posters= recommended(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
       st.text(names[2])
       st.image(posters[2])

    with col4:
       st.text(names[3])
       st.image(posters[3])

    with col5:
       st.text(names[4])
       st.image(posters[4])

st.write("You selected:",selected_movie_name )


