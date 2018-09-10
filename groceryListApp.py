from flask import Flask
from flask import render_template
from groceryList import GroceryList, GroceryItem
import csv

app = Flask(__name__)

@app.route('/')
def mainPage():
    return 'Hello'

@app.route('/ingredients')
def ingredientsPage():
    groceries = GroceryList()
    groceries.readList()
    grocList = groceries.getList()

    ingList = []
    
    for i in grocList:
        ingList.append(i.name)
##    ingList = []
##    with open ('ingredients.csv') as f:
##        reader = csv.DictReader(f)
##        for row in reader:
##            #print(row['ingredient'])
##            ingList.append({'ingredient':row['ingredient'],'status':row['status']})
##        #print(ingList)
    return render_template('ingredients.html',ingList=ingList)

@app.route('/list')
def listPage():
    return render_template('list.html')

@app.route('/associations')
def assocPage():
    return render_template('associations.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0")
