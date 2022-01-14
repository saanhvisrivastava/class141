from flask import Flask,jsonify,request
import csv

all_movies=[]
with open('movies.csv',encoding='utf-8') as f:
    reader=csv.reader(f)

    data=list(reader)
    all_movies=data[1:]

#print(all_movies)

liked_movies=[]
not_liked_movies=[]
not_watched=[]

app=Flask(__name__)#default route- get all movies
@app.route('/get-movies')
def get_movies():
    return jsonify({
        'data':all_movies[0],
        'status':'success'
    })

@app.route('/liked-movies',methods=['POST'])
def liked_movies():
    movie=all_movies[0]
    all_movies=all_movies[1:]
    liked_movies.append(movie)

     return jsonify({
       
        'status':'success'
    }),201

@app.route('/not_liked-movies',methods=['POST'])
def not_liked_movies():
    movie=all_movies[0]
    all_movies=all_movies[1:]
    not_liked_movies.append(movie)

     return jsonify({
       
        'status':'success'
    }),201

@app.route('/not_watched',methods=['POST'])
def not_watched():
    movie=all_movies[0]
    all_movies=all_movies[1:]
    not_watched.append(movie)

     return jsonify({
       
        'status':'success'
    }),201
    
    





if __name__ =='__main__':
    app.run()

    