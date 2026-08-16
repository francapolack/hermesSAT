import math

r=6871
ascension=20
tasa=15

conversion=math.radians(ascension*tasa)

cosine=math.cos(conversion)
print(f"Cosino en radianes:{cosine}")
print(f"{"SEPARADOR":-^30}")
cosino=math.degrees(cosine)
print(f"Cosino en grados:{cosino}")
print(f"{"SEPARADOR":-^30}")