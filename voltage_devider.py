print("Voltage devider! ")
vmax = float(input("Enter maximum output = "))
vmin = float(input("Enter minimum output = "))
in_volt = float(input("Enter input voltage = "))
for r1 in range(1,20):
    for r2 in range(1,20):
        vo = (r2/(r2+r1))*in_volt
        if vo == vmin or vo == vmax:
            print("R1 = {} and, R2 = {} , output voltage = {} ".format(r1,r2,vo))
print("thanks")