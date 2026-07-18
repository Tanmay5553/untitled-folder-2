purchase_price =int(input("enter the purchase price :"))
selling_price =int(input("enter selling price :"))

if selling_price > purchase_price:
    profit = selling_price - purchase_price
    print("profit is ",profit )
else:
    loss = purchase_price - selling_price
    print("loss is ",loss)

    
    
    