from flask import Flask
from flask import render_template
import csv

app = Flask(__name__)

@app.route('/')
def mainPage():
    return 'Hello'

@app.route('/ingredients')
def ingredientsPage():
    ingList = []
    with open ('ingredients.csv') as f:
        reader = csv.DictReader(f)
        for row in reader:
            #print(row['ingredient'])
            ingList.append({'ingredient':row['ingredient'],'status':row['status']})
        #print(ingList)
    return render_template('ingredients.html',ingList=ingList)

@app.route('/list')
def listPage():
    return render_template('list.html')

@app.route('/associations')
def assocPage():
    return render_template('associations.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0")
