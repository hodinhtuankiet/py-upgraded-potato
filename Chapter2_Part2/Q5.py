n=int(input(" Enter an integer greater than 0 : "))
sum=0.0
for i in range(1,n+1):
    sum += float(float(i)/(i+1))
print(sum)
