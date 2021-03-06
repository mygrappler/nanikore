import math
from math import log10, floor

def round_sig(x, sig=2):
    return round(x, sig-int(floor(log10(x)))-1)

V0 = 10.00

Va = [5.000, 8.000, 9.000, 9.500, 9.700, 9.900, 9.950, 9.990]
Vb = [10.01, 10.05, 10.10, 10.30, 10.50, 11.00, 12.00, 15.00, 20.00]


for var in range(0, len(Va)):
    if (var == 0):
        print("pH: 1")

    vH = (V0 - Va[var]) * 0.0001
    vAll = Va[var] + V0
    V1 = round_sig((vH/vAll) * 1000, 4)
    ansA = round_sig(-math.log10(V1), 4)
    print("pH: " + str(ansA))

    if(var == 7):
        print("pH: 7")

for var in range(0, len(Vb)):
    vH = (Vb[var] - V0) * 0.0001
    vAll = Vb[var] + V0
    V1 = round_sig((vH/vAll) * 1000, 4)
    ansB = round_sig(14 + math.log10(V1), 4)
    print("pH: " + str(ansB))
