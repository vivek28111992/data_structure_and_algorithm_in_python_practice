# The input Function
# A program that demonstrates the use of the input and print functions.

age = int(input('Enter your age in years: '))
max_heart_rate = 206.9 - (0.67 * age)                   # as per Med Sci Sports Exerc.
target = 0.65 * max_heart_rate
print('Your target fat-burning heart rate is {0:.5}'.format(target))