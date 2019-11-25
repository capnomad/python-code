N = int(input())

# Get the input
numArray = list(map(int, input().split()))

sum_integer = 0
# Write the logic to add these numbers here
#for i in numArray:
#    sum_integer += i

for i in range(0,N):
    sum_integer += numArray[i]
 
# Print the sum
print(sum_integer)