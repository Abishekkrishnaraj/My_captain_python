# My_captain_python
# My_captain_python

#to print fibonacci series

n=int(input("no.of terms"))

r=0

m=1 

print(r,m,end=' ')

while(n>0):

    sum=r+m

    print(sum,end=' ')

    r=m

    m=sum

    n-=1
