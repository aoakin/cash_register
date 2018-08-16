#cash register
#Ayo Akinrinade 08.12.18

cs = 0
ff = 0
h = 0
s = 0
sd = 0
md = 0
ld = 0
ss = 0
ms = 0

cashier_name = input("Cashier Name: ")
print("------Cash Register------")
print("=========================")
print("Cashier: %s" % cashier_name)
print("1. Chicken Strips - $3.50")
print("2. French Fries   - $2.50")
print("3. Hamburger      - $4.00")
print("4. Salad          - $3.75")
print("5. Sm Drink       - $1.25")
print("6. Md Drink       - $1.50")
print("7. Lg Drink       - $1.75")
print("8. Sm Milk Shake  - $2.25")
print("9. Md Milk Shake  - $2.75")
print("=========================")
order = input(": ")

L = list(order)
cs = L.count("1")
ff = L.count("2")
h = L.count("3")
s = L.count("4")
sd = L.count("5")
md = L.count("6")
ld = L.count("7")
ss = L.count("8")
ms = L.count("9")
total_cost = (3.5*cs)+(2.5*ff)+(4*h)+(3.75*s)+(1.25*sd)+(1.5*md)+(1.75*ld)+(2.25*ss)+(2.75*ms)
print("\nOrder----------------")
print("%d Chicken Strips" % cs)
print("%d French Fries" % ff)
print("%d Hamburgers" % h)
print("%d Salads" % s)
print("%d Small Drinks" % sd)
print("%d Medium Drinks" % md)
print("%d Large Drinks" % ld)
print("%d Small Milk Shakes" % ss)
print("%d Medium Milk Shakes" % ms)
print("Total Cost-----------")
print("$ %.2f" % total_cost)
print("Cashier: %s" % cashier_name)
print("---------------------")
print("   Have a Good Day")