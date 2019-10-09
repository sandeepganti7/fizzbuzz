"""This code has been taken from the link: https://www.w3resource.com/python-exercises/python-conditional-exercise-10.php """

for fizzbuzz in range(1,100):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("fizzbuzz")
        continue
    elif fizzbuzz % 3 == 0:
        print("fizz")
        continue
    elif fizzbuzz % 5 == 0:
        print("buzz")
        continue
    print(fizzbuzz)
