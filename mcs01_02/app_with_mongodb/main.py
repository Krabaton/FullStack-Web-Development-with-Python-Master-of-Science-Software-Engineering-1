from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://mydb:27017")
db = client["mydatabase"]

@app.route("/")
def index():
    result = []
    cursor = db.cats.find()
    for cat in cursor:
        print(cat)
        result.append({"id": str(cat.get("_id")), "name": cat.get("name")})

    return result

if __name__ == "__main__":
    app.run(host="0.0.0.0")
