from datetime import datetime

name = input("enter your name:")

lists = """
****************************

Rice    Rs 20/kg
sugar   Rs 30/kg
salt    Rs 40/kg
oil     Rs 200/liter
paneer  Rs 100/kg
Boost   Rs 90/each
Maggie  Rs 50/each

*****************************
"""
price = 0
pricelist =[]
totalprice = 0
Finalfinalprice = 0
ilist =[]
qlist = []
plist = []

items = {"Rice": 20,
        "sugar": 30,
        "salt": 40, "oil":200,
        "paneer" : 100,
        "Boost":90,
        "Maggie":50 }

options = int(input("\nenter 1 to see the menu or 2 to exit : "))

if options == 1:
    print(lists)
    for i in range(len(items)):
        inp1 = int(input("\nif you want to buy enter 1 or enter 2 to exit"))
        if inp1 == 2:
            print("thanks for your time.")
            break
        elif inp1 == 1:
            item = input("\nEnter Items: ")
            quantity = int(input("Enter Quantity in KG's: "))
            if item in items.keys():
                price = quantity*(items[item])
                pricelist.append((item,quantity,items,price)) 
                ilist.append(item)
                qlist.append(quantity)
                totalprice += price
                plist.append(price)
                gst = totalprice*0.05
                Finalamount = totalprice+gst
            else:
                print("you entered wrong item")
            inp = input("\ndo u want to bill the list enter yes or no : ")
            if inp.lower() == "yes":
                pass
                if Finalamount!=0:
                    print(40*"=","Sampoorna SuperMarket",40*"=")
                    print(42*" ","Hyderabad",40*" ")
                    print(name,60*" ","Date:",datetime.now())
                    print(100*"-")
                    print("s.no",3*"\t ","items",4*"\t","Quantity",3*"\t","Price")
                    for j in range(len(ilist)):
                        print(j,3*"\t ",ilist[j],4*"\t",qlist[j],3*"\t ",plist[j])
                    print(100*"-")
                    print(9*"\t ","Total Amount: ",totalprice)
                    print(9*"\t","GST: ",2*"\t",gst)
                    print(100*"-")
                    print(9*"\t","Final Amount: ",Finalamount)
                    print(100*"-")
                    print(40*" ","Thanks for Shopping")
                    print(100*"-")
                    print()
            elif inp.lower() == "no":
                pass
            else:
                print("you have entered wrong input")
        else:
            print("you have entered wrong item")    
else:
    print("thanks for your time")
    pass