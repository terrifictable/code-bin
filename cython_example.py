# you can put the normal python and cython code into one .pyx file and compile it, it will still work
# oh yea and save this as a ".pyx" file instead of ".py" if you want this to work (and follow the description of this commit for more information about building and executing this)

# ====== PYTHON ======
# cython_example.py
def prime_finder_vanilla(amount):
    primes = []

    found = 0
    number = 2
    while found < amount:
        for x in primes:
            if number % x == 0:
                break

        else:
            primes.append(number)  # x
            found += 1
        number += 1
    return primes


# ====== CYTHON ======
# cython_example.pyx
def prime_finder_optimized(int amount):
    cdef int number, x, found
    cdef int primes[100000]

    amount = min(amount, 100000)

    found = 0
    number = 2
    while found < amount:
        for x in primes[:found]:
            if number % x == 0:
                break

        else:
            primes[found] = number
            found += 1
        number += 1

    return_list = [p for p in primes[:found]]
    return return_list
# ==============================
  
  
  
# ==============================
# SETUP.PY
from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize("cython_example.pyx") # replace "cython_example" with the name of your pyx file
)
# ==============================



# ==============================
# EXAMPLE.PY
import cython_example
import time

x = 30000

print("Execution time of \"Python\" and \"Cython\"")

start_vanilla = time.time()
cython_example.prime_finder_vanilla(x)
end_vanilla = time.time()

print("Python > " + str(end_vanilla - start_vanilla))

start_c = time.time()
cython_example.prime_finder_optimized(x)
end_c = time.time()

print("Cython > " + str(end_c - start_c))
# ==============================
