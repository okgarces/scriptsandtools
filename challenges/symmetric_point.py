num_tests = raw_input()
str_r = ""

def mid_point(num, num2):
    num_r = (int(num2)*2) - int(num)
    return num_r


for i in range(0, int(num_tests)):
    num1 = raw_input().split(' ')
    str_r += "%s %s \n" % (mid_point(num1[0], num1[2]),mid_point(num1[1], num1[3]))

print str_r
