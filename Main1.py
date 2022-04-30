from flask import Flask, render_template, redirect, request, url_for
import pickle
import bz2file as bz2
# model = pickle.load(open('RandomForest.pkl', 'rb'))
def decompress_pickle(file):

    data = bz2.BZ2File(file, 'rb')
    data = pickle.load(data)
    return data
model = decompress_pickle('RandomForest.pbz2')
app = Flask(__name__)


app.config['SECRET_KEY'] = "Yashnegi@01"


@app.route("/", methods=["GET", "POST"])
def forMain():
    return render_template("base.html")



@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        prediction=0
        p, d, c, e = 1, 0, 0, 0
        m, a = 1, 0
        f, s, t, fou, td = 1, 0, 0, 0, 0
        i, dea = 1, 0
        year = int(request.form['year'])
        k = int(request.form.get('SP'))
        fuel = request.form['fuel']
        seller = request.form.get('cars')
        trans = request.form['trans']
        own = request.form['ownership']

        if fuel == "Petrol":
            p, d, c, e = 1, 0, 0, 0
        elif fuel == "Diesel":
            p, d, c, e = 0, 1, 0, 0
        elif fuel == "CNG":
            p, d, c, e = 0, 0, 1, 0
        else:
            p, d, c, e = 0, 0, 0, 1

        if seller == "Individual":
            i, dea = 1, 0
        else:
            i, dea = 0, 1

        if trans == "Manual":
            m, a = 1, 0
        else:
            m, a = 0, 1

        if own == "FO":
            f, s, t, fou, td = 1, 0, 0, 0, 0
        elif own == "SO":
            f, s, t, fou, td = 0, 1, 0, 0, 0
        elif own == "TO":
            f, s, t, fou, td = 0, 0, 1, 0, 0
        elif own == "FOU":
            f, s, t, fou, td = 0, 0, 0, 1, 0
        else:
            f, s, t, fou, td = 0, 0, 0, 0, 1

        p1 = model.predict([[k, 2020-year, d, e, c, p, i, d, m, fou, s, td, t]])
        prediction = round(p1[0], 2)
        if p1<0:
            return render_template('base.html',to="Sorry you cannot sell this car")
        else:
            
            return render_template('base.html',to="Rs. {}".format(prediction))
    else:
        return render_template('base.html')
    
    

if __name__ == "__main__":
    app.run(debug=True)
