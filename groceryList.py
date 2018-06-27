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
            print(row['ingredient'])
            ingList.append({'ingredient':row['ingredient'],'status':row['status']})
        #print(ingList)
    return render_template('ingredients.html',ingList=ingList)

@app.route('/list')
def listPage():
    return 'List Page'

@app.route('/associations')
def assocPage():
    return 'Associations Page'

if __name__ == "__main__":
    app.run(host="0.0.0.0")
