import csv

class GroceryList:

    def __init__(self):
        #compList = [GroceryItem('Eggs',1),GroceryItem('Bread',0)];
        self.itemList = []
        #print("Complete List: ", compList)

    def readList(gList):

        gList.itemList = []
        
        with open ('items.csv') as f:
            reader = csv.DictReader(f)
            for row in reader:
                #print(row['ingredient'])
                #itemList.append({'item':row['item'],'stock':row['stock']})
                currItem = GroceryItem(row['idNum'],row['item'],int(row['stock']))
                #gList.itemList.append({'item':currItem.getName(),'stock':currItem.getStock()})
                gList.itemList.append(currItem)
            #print(gList.itemList)

    def writeList():
        pass

    def getList(gList):
        return gList.itemList

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

    def getId(item):
        return item.id;

    def getName(item):
        return item.name

    def getStock(item):
        return item.stock
        
    def setStock(item,stock):
        self.stock = stock

if __name__ == "__main__":
    print("yes")
    newGList = GroceryList()
    newGList.readList()
    theList = newGList.getList()

    for i in theList:
        print(i.idNum, i.name, i.stock)
        
