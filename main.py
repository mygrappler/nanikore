import math
from math import log10, floor

def round_sig(x, sig=2):
    return round(x, sig-int(floor(log10(x)))-1)

V0 = 10.00

Va = [5.000, 8.000, 9.000, 9.500, 9.700, 9.900, 9.950, 9.990]
Vb = [10.01, 10.05, 10.10, 10.30, 10.50, 11.00, 12.00, 15.00, 20.00]


for var in range(0, len(Va)):
    if (Va[var] == 0):
        print(0)
    vH = V0 - Va[var]
    vAll = Va[var] + V0
    V1 = round_sig(((vH*0.001)/vAll) * 100, 4)
    print(round_sig(-math.log10(V1), 4))
    if(Va[var] == 8):
        print(7)

for var in range(0, len(Vb)):
    vH = Vb[var] - V0
    vAll = Vb[var] + V0
    V1 = round_sig(((vH*0.001)/vAll) * 100, 4)
    print(round_sig(14 + math.log10(V1), 4))