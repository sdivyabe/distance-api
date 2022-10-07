from flask import Flask, render_template, request, flash
import requests

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        s_orgin = request.form['orgin']
        s_destination = request.form['destination']
        link = 'https://maps.googleapis.com/maps/api/distancematrix/json?origins='+s_orgin+'&destinations='+s_destination+'&units=imperial&key=AIzaSyDLGe2lR-Q04Bqmef0WhiGjlXEA_zr1tQg'
        value = requests.get(link)
        return render_template('index.html', data=value.json())
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)