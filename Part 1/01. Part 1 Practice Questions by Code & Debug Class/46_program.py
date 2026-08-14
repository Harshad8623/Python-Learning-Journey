# Write a function fizzbuzz(n) that takes a single number and prints "Fizz" if it divisible by 3 , "Buzz" if it is divisible by 5 , "FizzBuzz" if it's divisible by both otherwise print the number itself 
def fizzbuzz(n):
    if n % 3 == 0 :
        if n % 5 == 0:
            return "FizzBuzz"
        return "Fizz"
    else:
        if n % 5 == 0:
            return "Buzz"
        return n

print(fizzbuzz(11))
print(fizzbuzz(10))
print(fizzbuzz(15))
print(fizzbuzz(11))