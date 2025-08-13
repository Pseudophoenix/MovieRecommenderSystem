import streamlit as st
import pickle
import requests
movies_list=pickle.load(open("movies.pkl","rb"))
# print(movies_list)
import pandas as pd
movies=pd.DataFrame(movies_list)
def fetch_poster(movie_title):
    resp=requests.get(
        f"https://www.omdbapi.com/?t={movie_title}&apikey=7014fa2c&plot=full").json()
    # print(resp)
    if "Poster" in resp:
         return resp['Poster']
    else:
        return ""
st.title("Movie Recommender System")
option=st.selectbox("Enter the movie name:",set(movies_list['title']))
# st.text("")
def recommend(movie):
    similarity=pickle.load(open("similarity_matrix.pkl","rb"))
    index=movies[movies["title"]==movie].index[0]
    
    ans=sorted(list(enumerate(similarity[index])),reverse=True,key=lambda x:x[1])[1:6]
    l=[]
    re_pos=[]
    for i in ans:
        l.append(movies.iloc[i[0]]['title'])
        re_pos.append(fetch_poster(movies.iloc[i[0]]['title']))
    return l,re_pos

if st.button("Recommend 5 movies"):
    names,pos=recommend(option)
    col1, col2, col3=st.columns(3)
    with col1:
        st.header(names[0])
        if pos[0]:
            st.image(pos[0])
    with col2:
        st.header(names[1])
        if pos[1]:
            st.image(pos[1])
    with col3:
        st.header(names[2])
        if pos[2]:
            st.image(pos[2])