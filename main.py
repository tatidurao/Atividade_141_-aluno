from flask import Flask, jsonify, request
import pandas as pd

movies_data = pd.read_csv('final.csv')

app = Flask(__name__)

all_movies = movies_data[["original_title", "poster_link","release_date","runtime","weighted_rating"]]

liked_movies=[]
not_liked_movies =[]
did_not_watch=[]

def assign_val():
  m_data = {
    "original_title": all_movies.iloc[0,0],
    "poster_link": all_movies.iloc[0,1],
    "release_date": all_movies.iloc[0,2] or "N/A",
    "duration": all_movies.iloc[0,3],
    "rating": all_movies.iloc[0,4]/2

  }
  return m_data





if __name__ == "__main__":
  app.run()
