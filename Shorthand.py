
# short hand/assignment: += -= *= /= %= //=
# left side var of operation and assigning var of operation result should be same


wt1=98.5
wt2=65.3
'''
# += -=
wt1+=wt2 # wt1=wt1+wt2
wt2=wt1-wt2
wt1-=wt2 # wt1=wt1-wt2
'''

# *= /=
wt1*=wt2
wt2=wt1/wt2
wt1/=wt2

#print("Weight one",wt1,"Weight two",wt2)
print("Weight one %.2f and Weight Two is %.2f"%(wt1,wt2))




