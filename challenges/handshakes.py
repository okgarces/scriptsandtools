num_tests = raw_input()
str_r = ""

def factorial(num):
    if num > 0:
        if num == 1:
            return 1
        else:
            return num * factorial(num-1)
    else:
        return 0

for i in xrange(int(num_tests)):
    num1 = int(raw_input())
    num_factorial = factorial(num1)
    num_r = num_factorial / (2 * factorial(num1-2))
    str_r += "%s \n" % num_r

print str_r.strip()
