import math

r=6871
ascension=20
tasa=math.degrees(15)

cos=math.cos((tasa*ascension))
sin=math.sin((tasa*ascension))


x=r*math.degrees(cos)*math.degrees(cos)
print("-----------------")
print(x)
y=r*math.degrees(cos)*math.degrees(sin)
print("-----------------")
print(y)
z=r*math.degrees(sin)
print("-----------------")
print(z)