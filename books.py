from flask import Flask,request,jsonify
import sqlite3
from data import  *
app = Flask(__name__)

book_data =[
    {    
        "id":1,
        "title": "The Hobbit",
        "author":"Rampal",
        "genre":["Fantasy","Adventure"],
        "price": 10.5,
        },
         {
         "id":2,      
        "title": "atom",
        "author":"brown",
        "genre":["sci-fic","Adventure"],
        "price": 5,
        },
         {
         "id":3,
        "title": "Rich dad",
        "author":"jackson",
        "genre":["Adventure"],
        "price": 13.5,
        },

        {"id":4,
        "title": "hope ",
        "author":"kim sew",
        "genre":["Fantasy","Adventure"],
        "price": 19.5,
        },
         {
               
        "id":5,
        "title": "The Hobbit",
        "author":"Rampal",
        "genre":["Fantasy","Adventure"],
        "price": 10.5,
        }
        
]


def db_connection():
      conn =  None
      try:
            conn = sqlite3.connect('api.db')
      except sqlite3.error as e:
            print(e)
      return conn

@app.route('/books',methods=['GET','POST'])
def books():
    conn =  db_connection()
    cursor = conn.cursor()
    if request.method =='GET':
           cursor = conn.execute("SELECT * FROM demo")
           data =  [dict (id =row[0],title=row[1],author=row[2],genre=row[3],price=row[4])for  row in cursor.fetchall()] 
           if data is not None:
            return jsonify({'data':data})
          
    if request.method == 'POST':
          book_name = request.json['title']
          book_author = request.json['author']
          book_genre  = request.json['genre']
          book_price =  request.json['price']
          #conn.execute("INSERT INTO DEMO (title,author,genre,price) values (%s,%s,%s,%s)",(book_name,book_author,book_genre,book_price))
          conn.execute("INSERT INTO DEMO (title, author ,genre,price ) VALUES (?, ?, ?,?)",(book_name, book_author,book_genre, book_price))
          conn.commit()
          return f"Book with the id :created successfully!"

    else:
          return  f'{request.method} not allowed'


@app.route('/books/<int:id>',methods = ['GET','PUT','DELETE'])
def singlebook(id):
      if request.method == 'GET':
            for book in book_data:
                  if book["id"]==id:
                        return jsonify(book)
      if request.method == 'PUT':
            for book in book_data:
                  if book["id"] == id:
                        book["title"] = request.form["title"]
                        book["author"] = request.form["author"]
                        book["genre"] = request.form["genre"]
                        book["price"] = request.form["price"]
                        updated_book ={
                              "id":id,
                              "title":book["title"],
                              "author":book["author"],
                              "genre":book["genre"],
                              }
                        return jsonify(updated_book)
      if request.method == 'DELETE':
            for index,book in enumerate(book_data):
                  if book["id"]==id:
                        book_data.pop(index)
                        return jsonify(book_data)
                                       

                  
   
if __name__=='__main__':
        app.run(debug=True)
    