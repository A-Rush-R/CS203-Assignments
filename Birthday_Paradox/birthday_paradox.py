p_limit = float(input("Enter probability that at least two students have the same birthday in %: "))

while not (p_limit > 0 and p_limit < 100) :
    print("The value must be between 0 and 100!")
    p_limit = float(input("Enter probability that at least two students have the same birthday in %: "))

# Converts p into a decimal value
p_coincident_birthday = p_limit/100

# Finding the required probability of no two students having the same birthday
p_n = 1- p_coincident_birthday

# p_k is the probability of no two students haveing the same birthday, when their are k students in the class
# for limiting case, there is only one student (k = 1) in the class and thereby the probability of no two students having the same birthday is 1
p_k = 1.0
k = 1

# Loop along the probability of this not happening
while p_k > p_n:
    # if p_neg is still not small enough, we increase the class strength by one
    k += 1
    p_k = p_k * (365-k)/365

print(k)