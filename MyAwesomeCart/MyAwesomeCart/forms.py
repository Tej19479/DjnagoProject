import amortizatiom

'''def emi(p, r, t):
    # for one month interest
    outstanding_principal = p
    r = (r / 100) / 12
    ime = 2
    print("roi", r)
    # for one month period
    for x in range(0, ime):
        t = t * 12

        emi = (p * r * pow(1 + r, t)) / (pow(1 + r, t) - 1)
        print("emi is", emi)
        interest_paid = outstanding_principal * r
        base_principal_paid = emi - interest_paid
        outstanding_principal = outstanding_principal - base_principal_paid

        print("interest_paid", interest_paid)
        # print("base_pricipal_paid", base_principal_paid)
        print("outstanding_principal", outstanding_principal)

    return emi'''




principal = 10000
rate = 12
time = 12
#emi = emi(principal, rate, time)
emi = amortization_schedule(principal, rate, time)
