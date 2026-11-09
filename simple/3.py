import math

t0 = 100
ts = 20
t10 = 80
t = 10

k = -math.log((t10 - ts)/(t0 - ts))/t

time = 20
t20 = ts + (t10-ts)*math.exp(-k * time)

print("Newton's Law of Cooling")
print("Cooling Constant (k) =", round(k, 4))
print("Temperature after 20 minutes =", round(t20, 2), "°C")