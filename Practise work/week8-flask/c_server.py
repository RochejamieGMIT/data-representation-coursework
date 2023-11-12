from flask import Flask,request,redirect,url_for,jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return "HEllllllO"

@app.route("/datainquery",methods=["GET"])
def inquery():
    queryargs={
        "firstname": request.args["firstname"],
        "age": request.args["age"]
    }
    
    print(queryargs)
    
    return jsonify(queryargs)

@app.route("/dataasjson",methods=["POST"])
def asjson():
    book={
        "Title": request.json["Title"],
        "Author": request.json["Author"],
        "ISBN": request.json["ISBN"],
        "Price": request.json["Price"]
    }
    #Put in DB
    print(book)
    
    return jsonify(book)


if __name__ =="__main__":
    app.run(debug=True)
