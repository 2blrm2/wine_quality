from flask import Flask, render_template, request, jsonify
import os
import yaml,joblib
import numpy as np
from prediction_service import prediction

webapp_root = "webapp"
parms_path= "params.yaml"
static_dir = os.path.join(webapp_root, "static")
template_dir = os.path.join(webapp_root, "templates")


def read_parms(config_path):
    with open(config_path,'w') as f:
        config = yaml.safe_load(f)
    return config

def predict(data):
    config = read_parms(parms_path)
    model_dir_path = config['webapp_model_dir']
    model= joblib.load(model_dir_path)
    prediction= model.predict(data)
    print(prediction)
    return prediction[0]

def api_response(request):
    try:
        data= np.array([list(request.json.values())])
        response=predict(data)
        response= {"response": response}
        return response
    except Exception as e:
        print(e)
        error = {"error": "Something went wrong !! Try again"}
        return error

app = Flask(__name__, static_folder=static_dir,template_folder=template_dir)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            if request.form:
                data= dict((request.form).values())
                data = [list(map(float,data))]
                response = predict(data)
                return render_template("index.html",response = response)
            elif request.json:
                response= api_response(request)
                return jsonify(response)

        except Exception as e:
            print(e)
            error= {"error" : "Something went wrong !! Try again"}
            return render_template("404.html",error = error)
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)