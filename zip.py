n1={1,2,3,4}
n2={'a','b','c','d'}
n3=list(zip(n1,n2))

l1=[100,200,300,400]
l2=[10,20,30,40]
for x,y in zip(l1,l2 [::-1]):
    print(x,y)

stocks=['bread','biscuit','chocolate']
price=[100,258,200]
new_dict={stocks:price for stocks,price in zip(stocks,price)}
print(new_dict)
