import streamlit as st
import pickle
movies_list=pickle.load(open("movies.pkl","rb"))
# print(movies_list)
import pandas as pd
movies=pd.DataFrame(movies_list)

st.title("Movie Recommender System")
option=st.selectbox("Enter the movie name:",set(movies_list['title']))
# st.text("")
def recommend(movie):
    similarity=pickle.load(open("similarity_matrix.pkl","rb"))
    index=movies[movies["title"]==movie].index[0]
    
    ans=sorted(list(enumerate(similarity[index])),reverse=True,key=lambda x:x[1])[1:6]
    l=[]
    for i in ans:
        l.append(movies.iloc[i[0]]['title'])
    return l

if st.button("Recommend 5 movies"):
    recommendations=recommend(option)
    for i in recommendations:
        st.write(i)