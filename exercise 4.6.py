def computepay(h,r):
    if h>40:
        rem=h-40
        return ((40*r)+(rem*r*1.5))
    if h<=40:
        return h*r

hrs = input("Enter Hours:")
rate=input('Enter rate per hour:')
h=int(hrs)
r=float(rate)

p = computepay(h,r)
print("Pay",p)
