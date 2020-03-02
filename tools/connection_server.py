import socket
import operator

ops={ "+": operator.add,
        '-' : operator.sub,
        '*' : operator.mul,
        '/' : operator.div,
        '%' : operator.mod,
        '^' : operator.xor}
s = socket.socket()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('172.24.98.43',8080))
while 1:

    data = s.recv(1024)
    print data
    data = s.recv(1024)
    operations = data.split(' ');
    print data
    if(len(operations)>2):
        operator = ops[operations[1]](int(operations[0]),int(operations[2]))
        s.send(str(operator))
    print data


