a = int(raw_input("Enter Number of time(s) the button pressed: "))
l=['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-']
if a<=0:
    print "error in input :: Values exist from 1 and above only"
else:
    for i in range (1,a+1):
       for j in range (0,50):
          if (j+1)%i == 0:
             if l[j]=='*':
                 l[j]='-'
             elif l[j]=='-':
                 l[j]='*'
    for k in range (0,50):
       print l[k],
