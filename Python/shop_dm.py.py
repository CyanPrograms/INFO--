# -*- coding: utf-8 -*-
"""
@author: Luka Orlić
"""

import pickle

shop = {"stock":[] , "cart":[]}

def product_find(productname,where="cart"):
    for position, i in enumerate(shop[where]):
        if i["name"]==productname:
          return(position)
    return(-1)

def print_bill(where="cart"):
    if len(shop[where]) == 0:
        print(where + " is empty!")
    else:
        print("\n-- " + where + " " + (41-len(where)) * "-")
        total = 0.0
        for i in shop[where]:
            price = i["quantity"] * i["price"]
            total += price
            print("%20s" % i["name"] + "%5d" % i["quantity"] + "%10.2f" % i["price"] + 
                  "%10.2f" % price)
        print(45 * "-")
        print("%45.2f" % total) 
        print(45 * "-" + "\n")

def add_product(where, name, price, quantity):
    product = dict()
    product["name"]=name
    product["price"]=price
    product["quantity"]=quantity
    shop[where].append(product)
    
def save_shop_to_disk():
    with open(r'c:\test\shop.pickle', 'wb') as f:
        pickle.dump(shop, f)
    
def load_shop_from_disk():
    global shop
    if len(shop["stock"]) > 0 or len(shop["cart"]) > 0:
        if input("Stock date will be lost! Are you sure? (yes/no) ").lower() != "yes":
            return
    with open(r'c:\test\shop.pickle', 'rb') as f:
        shop = pickle.load(f)
    
def parser(cmd):
    l = list()
    x = cmd.split(" ")        
    for i in x:
        j = i.strip()
        if j!="":
            l.append(j)
    return(l)


def test_init():
    add_product("stock","milk",0.95,6)
    add_product("stock","water",0.35,12)
    add_product("stock","bread",1.15,2)
    add_product("stock","salt",2.13,1)
    add_product("stock","butter",3.95,1)
    add_product("stock","beer",4.95,2)
    add_product("cart","newspaper",2.99,1)
    
# test_init() # polnitev za testiranje

work = True

while work:
    cmd = []
    while cmd == []:
        cmd = parser(input("> ").lower())
    if cmd[0] in ['quit', 'exit']:
        print("Exiting...")
        work = False
    elif cmd[0] == "show":
        if len(cmd) in [2,3,4] and cmd[1] in ['cart', 'stock']:
            if len(cmd) == 2:
                print_bill(cmd[1])
            elif len(cmd) == 3:
                p = product_find(cmd[2],cmd[1])
                if p > -1:
                    print("name     : %20s " % shop[cmd[1]][p]["name"])
                    print("price    : %20d " % shop[cmd[1]][p]["quantity"])
                    print("quantity : %20.2f " % shop[cmd[1]][p]["price"])
                else:
                    print("Product " + cmd[2] + " is not contained in " + cmd[1])
            elif len(cmd) == 4:
                if cmd[3] in ['name', 'price', 'quantity']:
                    p = product_find(cmd[2],cmd[1]) 
                    if p > -1:
                        if cmd[3] == "price":
                            print("%.2f" % shop[cmd[1]][p][cmd[3]])
                        else:
                            print(shop[cmd[1]][p][cmd[3]])
                    else:
                        print("Product " + cmd[2] + " is not contained in " + cmd[1])
                else:
                    print("Property " + cmd[3] + " doesn't exists!")
            else:
                print("Incorrect number of parameters.")
        else:
            if len(cmd) not in [2,3,4]:
                print("Incorrect number of parameters.")
            else:
                print(cmd[1] + " is not permitted.")
    elif cmd[0] == "set":
        if len(cmd) == 5 and cmd[1] in ['cart', 'stock'] and cmd[3] in ['name', 'price', 'quantity']:
            p = product_find(cmd[2],cmd[1])
            if p > -1:
                try:
                    if cmd[3] == "name":
                        shop[cmd[1]][p][cmd[3]] = cmd[4]
                    elif cmd[3] == "quantity":
                        m = int(cmd[4])
                        if m < 0:
                            raise ValueError
                        if m == 0:
                            shop[cmd[1]].remove(shop[cmd[1]][p])
                        else:
                            shop[cmd[1]][p][cmd[3]] = m
                    elif cmd[3] == "price":
                        fm = float(cmd[4])
                        if fm <= 0:
                            raise ValueError
                        shop[cmd[1]][p][cmd[3]] = fm
                except ValueError:
                    print("Setting incorrect value!")
            else:
                print("Product " + cmd[2] + " is not contained in " + cmd[1])
        else:
            print("Incorrect set command!")                     
    elif cmd[0] == "save":
        save_shop_to_disk()
    elif cmd[0] == "load":
        load_shop_from_disk()
    elif cmd[0] == "+":
        if len(cmd) in [2,3]:
            try:
                if len(cmd) < 3:
                    m = 1
                else:
                    m = int(cmd[2])
                    if m < 1:
                        raise ValueError                    
                pc = product_find(cmd[1],"cart")
                ps = product_find(cmd[1],"stock")
                if ps >= 0:
                    mq = shop["stock"][ps]["quantity"]
                    mp = shop["stock"][ps]["price"]
                    if mq >= m:
                        shop["stock"][ps]["quantity"] -= m
                        #if int(shop["stock"][ps]["quantity"]) == 0:
                        #    shop["stock"].remove(shop["stock"][ps])
                        if pc >= 0:
                            shop["cart"][pc]["quantity"] += m
                            shop["cart"][pc]["price"] = mp
                        else:
                            add_product("cart",cmd[1],mp,m)
                    else:
                        print("Not enough products in stock!")
                else:
                    print("Procut not in stock!")
            except ValueError:
                print("Invalid parameter value!")
        else:
            print("Incorrect number of parameters.")
    elif cmd[0] == "-":
        if len(cmd) in [2,3]:
            try:
                if len(cmd) < 3:
                    m = 1
                else:
                    m = int(cmd[2])
                    if m < 1:
                        raise ValueError                    
                pc = product_find(cmd[1],"cart")
                ps = product_find(cmd[1],"stock")
                if pc >= 0:
                    mq = shop["cart"][pc]["quantity"]
                    mp = shop["cart"][pc]["price"]
                    if m <= mq:
                       shop["cart"][pc]["quantity"] -= m
                       if int(shop["cart"][pc]["quantity"]) == 0:
                           shop["cart"].remove(shop["cart"][pc])
                       if ps >= 0:
                           shop["stock"][ps]["quantity"] += m
                           shop["stock"][ps]["price"] = mp
                       else:
                           add_product("stock",cmd[1],mp,m)
                else:
                    print("Procut not in cart!")
            except ValueError:
                print("Invalid parameter value!")
        else:
            print("Incorrect number of parameters.")
    else:
        print("Unknow command!")
