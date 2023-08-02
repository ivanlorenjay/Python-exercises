# Your task is to complete the code in order to evaluate the following expression:
# 1 /x + 1 / x + 1/ x + 1/ x 

x = float(input("Introduce x: "))

y = 1 / (x + 1 / ( x + 1/ (x + 1/ x))) 

print("y =", y)

# Checker

# sample input      /       expected output
#    1                   y = 0.6000000000000001
#    10                  y = 0.09901951266867294
#    100                 y = 0.009999000199950014
#    -5                  y = -0.19258202567760344

# substitutes this variable for the expected output in each case
sample = -0.19258202567760344

if( y == sample):
    print("Correct!")
else:
    print("Incorrect!")
