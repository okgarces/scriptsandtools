num_tests = raw_input()
str_r = ""

for i in range(0, int(num_tests)):
    num1 = int(raw_input())
    str_r += "%s \n" % str(num1 + 1)

print str_r.strip()
