from flask import Flask, request, jsonify
import util 

app=Flask(__name__)

@app.route('/get_location_names')
def get_location_names():
    response = jsonify({
        'locations': util.get_location_name()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict_home_price',methods=['POST'])
def predict_home_price():
    total_area = float(request.form['total_area'])
    location = request.form['location']
    bhk= int(request.form['bhk'])
    baths = int(request.form['baths'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(location, total_area, bhk, baths)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__=="__main__":
    print("Starting Python Flask Server for Home Price Prdiction")
    util.load_saved_artifacts()
    app.run()