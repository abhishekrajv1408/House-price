from flask import Flask,render_template,request
import pandas as pd
from models import predict_di
app=Flask(__name__)

@app.route("/")
def name():
    return render_template('home.html')

@app.route("/result", methods=["POST","Get"])
def home( ):
    if request.method=="POST":
        a=int(request.form["bedrooms"])
        b=float(request.form["bathrooms"])
        c=int(request.form["sqft_living"])
        d=int(request.form["grade"])
        e=int(request.form["sqft_above"])
        f=int(request.form["sqft_basement"])
        g=float(request.form["lat"])
        h=int(request.form["sqft_living15"])
        df={"bedrooms":[a],
        "bathrooms":[b],
        "sqft_living":[c],
        "grade":[d],
        "sqft_above":[e],
        "sqft_basement":[f],
        "lat":[g],
        "sqft_living15":[h]
        }
        data=pd.DataFrame(df)
        data_1=predict_di(data)
    return render_template('sub.html',data=data_1)





if __name__ == "__main__":
    app.run( debug=True )
