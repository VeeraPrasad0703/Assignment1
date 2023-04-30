book1=int(input("Enter number of books of type 1:"))
book2=int(input("Enter number of books of type 2:"))
book3=int(input("Enter number of books of type 3:"))
if book1>0 or book2>0 or book3>0: #checking atleat one book is selected or not
    total=book1*499.0+book2*855.0+book3*645.0 #calculating total price
    invoice=total+total*0.12+200 #including gst and delivery charges
    print(invoice)
else:
    print("No Books selected Please Select books required to deliver")
