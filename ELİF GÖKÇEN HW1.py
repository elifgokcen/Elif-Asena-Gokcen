
import random 
import datetime
class Portfolio(object):
    funddict = {}
    stockdict = {}
    cash = 0 
    history = []
    
    def purchMF (self,quantity,mfname):
        mfname1 = mfname.getname()
        if mfname1 in self.fundict:
            if type(quantity) == float:
                Portfolio.funddict[mfname1] += quantity
                Portfolio.cash -= quantity
                Portfolio.history.append(" At" + str(datetime) + " , "+ str(quantity) + " quantity of " + str(mfname1) + " had been purchased.")
            else: 
                print(" Mutual funds can only be purchased as fractional shares. ")
        else: 
            print(str(mfname1) + " cannot be found. ")
              
    def purchST (self,share,stname):
        stname1 = stname.getname()
        if stname1 in self.stockdict:
            if type(share) == int:
                price1 = stname.getprice()
                Portfolio.stockdict[stname1] += price1*share 
                Portfolio.cash -=price1*share
                Portfolio.history.append(str(share) + " unit of " + str(stname1) + " had been purchased.")
            else:
                print(" Stocks can only be purchased or sold as whole units. ")
        else:
            print(str(stname1) + " cannot be found. ")
        
    def sellMF (self,quantity,mfname):
            mfname1 = mfname.getname()
            if mfname1 in self.fundict:
                random1 = quantity*random.uniform(0.9,1.2)
                Portfolio.funddict[mfname1] -=random1
                Portfolio.cash += random1
                Portfolio.history.append(str(quantity) + " quantity of " + str(mfname1) + " had been sold.")
            else: 
                print(str(mfname1) + " cannot be found. ")
        
    def sellST (self,share,stname):
        price1 = stname.getprice()
        stname1= stname.getname()
        if stname1 in self.stockdict:
            if type(share) == int:
                random2 = price1*random.uniform(0.5,1.5)
                Portfolio.stockdict[stname1] -= share*random2
                Portfolio.cash += random2   
                Portfolio.history.append(str(share) + " unit of " + str(stname1) + " had been sold.")
            else:
                print(" Stocks can only be purchased or sold as whole units. ")
        else: 
            print(str(stname1) + " cannot be found. ")
            
    def history (self):
        return self.history
            
    def addcash (self,quantity):
        Portfolio.cash += quantity
        
    def wtdcash (self,quantity):
        Portfolio.cash -=quantity
        
class mutualfund (Portfolio):
    def __init__(self,mfname):
        self.mfname = mfname
    def getname(self):
        return self.mfname
    
class stock (Portfolio):
    def __init__(self,stname,price):
        self.stname = stname
        self.price = price 
    def getname(self):
        return self.stname
    def getprice(self):
        return self.price

