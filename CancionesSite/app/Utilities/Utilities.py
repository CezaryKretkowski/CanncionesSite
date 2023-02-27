from ..Cart import Cart
class Utilities(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Utilities, cls).__new__(cls)
        return cls.instance     

          
    def chanks(self,list,col):
        rows=[]
        colIterator=0
        cols=[];
        for i in list:
            if colIterator<col:
                cols.append(i)
            else:
                rows.append(cols)
                cols=[]
                colIterator=0
                cols.append(i)
            colIterator+=1
        if cols:
            rows.append(cols)  
         
        return rows
    
def Basket(request):
    return {"Basket":Cart(request)}
     


    