from flask import Flask,jsonify,request

from Data_Main import data

app = Flask(__name__)

@app.route("/")

def index():
    return jsonify({
        "data":data,
        "message":"Successful"
    }),200

@app.route("/star")

def stars():
    name = request.args.get("name")
    star_data = next(item for item in data if item["name"] == name)
    return jsonify({
        "data":star_data,
        "message":"Successful"
    }),200


if __name__ == "__main__":
    app.run()