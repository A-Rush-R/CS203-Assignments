p_limit = float(input("Enter the limit on the probability in %: "))

while not (p_limit > 0 and p_limit < 100) :
    print("The value must be between 0 and 100!")
    p_limit = float(input("Enter the limit on the probability in %: ")) 

# Converts p into a decimal value
p = p_limit/100

prob = 1.0
k = 1

# Loop along the probability of this not happening
while prob > (1-p):
    prob = prob * (365-k)/365
    k += 1

print(k)