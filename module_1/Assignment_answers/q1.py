# i)Using temp variable

var1 = 30
var2 = 20
print(f"Variables before swaping\nVariable 1:{var1}\nVariable 2:{var2}")
temp = var1
var1 = var2
var2 = temp
print(f"Variables after swaping\nVariable 1:{var1}\nVariable 2:{var2}")

# ii) without using third variable

var1 = 30
var2 = 20
print(f"Variables before swaping\nVariable 1:{var1}\nVariable 2:{var2}")
var1 = var1 + var2
var2 = var1 - var2
var1 = var1 - var2
print(f"Variables after swaping\nVariable 1:{var1}\nVariable 2:{var2}")