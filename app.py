from flask import Flask, request,jsonify

app=Flask(__name__)
@app.route("/",methods=["GET"])
def home():
    return jsonify({"message":"Hello, DecodeLabs!"})

@app.route("/user",methods=["POST"])
def user():
    data = request.get_json()
    
    if not data or "name" not in data:
        return jsonify({"error":"Name is required"}), 400
    return jsonify({"message":f"Hello,{data['name']}!"}),201

if __name__=="__main__":
    app.run(debug=True)