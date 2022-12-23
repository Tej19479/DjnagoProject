import math

print("Enter an amount to borrow")
p = input()
print("Enter an annual interest rate as a decimal value")
r = input()
print("Enter a loan lenght in years")
t = input()

p = float(p)
r = float(r)
t = float(t)
r = (r / 100) / 12

# m = (p * r * pow(1 + r, t)) / (pow(1 + r, t) - 1)

m = (p * (r / 12) * (math.pow(1 + r / 12, 12 * t))) / (math.pow(1 + r / 12, 12 + t) - 1)
print("Your payment will be: Rupiya" + str(m))
print("Month\tStartingBalance\tInterestRate\tInterestCharge\tPayment\tEndingBalance")

month = 12 * t
month = int(month)
startingBalance = p
endingBalance = p
for i in range(1, month + 1):
    interestCharge = r / 12 * startingBalance
    endingBalance = startingBalance + interestCharge - m
    print(str(i) + "\t\t$" + str(round(startingBalance, 2)) + "\t\t$" + str(round(interestCharge, 2)) + "\t\t$" + str(
        round(m, 2)) + "\t\t$" + str(round(endingBalance, 2)))
    startingBalance = endingBalance
