"""importing math module"""
import math 
"""creating a dictionary with key values as product name and creating list and appended product price in that list"""
product={"A":[20],"B":[40],"C":[50]} 
totalproduct={}
totQ,giftfee=0,0

"""looping through product dictionay and taking user inputs for quantity and gift wrap ,appending the values to the respective product values"""
for each in (product):
    a=(int(input("how many product "+each+":")))
    product[each].append(a)
    g=(str(input("Do you want gift wrap?(y/n)?"))).upper()
    product[each].append(g)
    if g=="Y":
        giftfee+=a
    totQ+=a

shippingfee=math.ceil(totQ/10)*5

"""first result"""
sub=0
for each in (product):
    total=product[each][0]*product[each][1]
    sub+=total
    print(f"product{each} , quantity:{product[each][1]} , total:{total}$")
    
"""second result"""
print("subtotal:",sub,"$")

totalproduct['subtotal']=sub
totalproduct['totalquantity']=totQ
"""creating a Discount class for calculating discount rates for total cart """
class Discount:
    def __init__(self,product,totalproduct):
        self.product=product
        self.totalproduct=totalproduct
    def flat_10_discount(self):
        discount=0
        if self.totalproduct["subtotal"]>200:
            discount=10
        return discount
    def bulk_5_discount(self):
        discount=0
        for each in self.product:
            if self.product[each][1]>10:
                eachdis=(self.product[each][0]*self.product[each][1]*5)/100
                discount+=eachdis
        return discount
    def bulk_10_discount(self):
        if self.totalproduct['totalquantity']>20:
            return (self.totalproduct['subtotal']*10)/100
        return 0
    def tiered_50_discount(self):
        discount=0
        if self.totalproduct["totalquantity"]>30:
            for each in self.product:
                if (self.product[each][1])>15:
                    eachdis=(((self.product[each][1]-15)*self.product[each][0])*50)/100
                    discount+=eachdis
        return discount
    
productlist=Discount(product,totalproduct)
f1=productlist.flat_10_discount()
b5=productlist.bulk_5_discount()
b10=productlist.bulk_10_discount()
t=productlist.tiered_50_discount()

maxdiscount={f1:"flat_10_discount",b5:"bulk_5_discount",b10:"bulk_10_discount",t:"tiered_50_discount"}
new=list(maxdiscount.keys())
new.sort(reverse=True)

"""Third Result"""
if new[0]==0:
    print("No discount ")
else:
    print('discount name applied:',maxdiscount[new[0]],',discount amount:',new[0])
    
"""fourth result"""
print("the shipping fee:",shippingfee,',gift wrap fee:',giftfee)

'''fifth result-total price after discount price applied and adding giftwrapping and shipping cost '''
print("Total:",(totalproduct['subtotal']-new[0]+shippingfee+giftfee))
