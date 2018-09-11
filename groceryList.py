import csv

class GroceryList:

    def __init__(self):
        self.itemList = []

    def readList(self):
        #read grocery list from database (file)
        self.itemList = []
        with open ('items.csv','r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                currItem = GroceryItem(row['idNum'],row['name'],int(row['stock']))
                self.itemList.append(currItem)

    def writeList(self):
        #write grocery list to database (file)
        with open ('items.csv','w') as f:
            f.write('idNum,name,stock\n')
            for i in self.itemList:
                f.write(i.idNum+','+i.name+','+str(i.stock)+','+'\n')

    def addItem():
        pass

    def removeItem():
        pass

class GroceryItem:

    def __init__(self):
        self.idNum = '00'
        self.name = 'ItemName'
        self.stock = 0
    
    def __init__(self,idNum,name,stock):
        self.idNum = idNum
        self.name = name
        self.stock = stock
        #print(self.idNum,self.name, self.stock)
        
    def setStock(self,stock):
        self.stock = stock

if __name__ == "__main__":

    grocList = GroceryList()
    grocList.readList()

    for i in grocList.itemList:
        #i.setStock(0)
        print(i.idNum, i.name, i.stock)

    grocList.writeList()
        
