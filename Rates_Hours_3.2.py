#The program will calculate your pay based on hours worked and your rate. For every hour that you've worked over 40 hours a week, your rate is automatically increased by 1.5

hrs = input("Enter Hours:")
rate = input("Enter Rate:")
try:
    h = float(hrs)
    rate_raw = float(rate)
except:
    Print("Error please enter numer")

if h <=40:
    pay = h * rate_raw
    print(pay)
elif h > 40:
    pay = (40*rate_raw) + (h-40)*(1.5*rate_raw)
    print(pay)
else:
    print ('enter number')
