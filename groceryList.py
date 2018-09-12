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
                f.write(hex(int(i.idNum,16))+','+i.name+','+str(i.stock)+'\n')

    def addItem(self, name, stock):
        #add new item to the grocery list
        lastId = self.itemList[-1].idNum
        newId = hex(int(lastId, 16) + 1)

        if stock < 0 or stock > 1:
            stock = 0
        
        self.itemList.append(GroceryItem(str(newId),str(name),int(stock)))

    def removeItem(self,idNum):
        #remove item from the grocery list 
        for i in self.itemList:
            if i.idNum == idNum:
                self.itemList.remove(i)

class GroceryItem:

    def __init__(self):
        self.idNum = '00'
        self.name = 'ItemName'
        self.stock = 0
    
    def __init__(self,idNum,name,stock):
        self.idNum = idNum
        self.name = name
        self.stock = stock
        
    def setStock(self,stock):
        self.stock = stock

if __name__ == "__main__":

    grocList = GroceryList()
    grocList.readList()

    for i in grocList.itemList:
        #i.setStock(0)
        print(i.idNum, i.name, i.stock)

    grocList.addItem('Beans',0)
    grocList.addItem('Salmon',1)
    grocList.removeItem('0x2c')
    
    grocList.writeList()
        
