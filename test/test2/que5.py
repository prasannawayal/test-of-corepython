price1=int(input('price of first product:'))
price2=int(input('price of second product:'))
price3=int(input('price of third product:'))
price4=int(input('price of fourth product:'))
price5=int(input('price of fifth product:'))
total_price=price1+price2+price3+price4+price5
gst=(total_price*18/100)
total_bill=total_price+gst
print('total price',total_price)
print('total bill of products after adding gst',total_bill)
