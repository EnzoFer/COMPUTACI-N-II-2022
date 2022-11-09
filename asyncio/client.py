import socket, getopt, sys

try:
    opt,arg = getopt.getopt(sys.argv[1:], 'h:p:')
    if len(opt) != 2:
        print("Cantidad de argumentos")
        exit()
except getopt.GetoptError as error:
    exit()

for (op,ar) in opt:
    if op == '-h':
       host = str(ar)
    if op == '-p':
        port = int(ar)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

while True:
    command = input('> ')
    if len(command) == 0 or command == "bye":
        print("Byes")
        s.send(command.encode("ascii"))
        break
    else:
        s.send(command.encode("ascii"))
        recv = str(s.recv(1024).decode("ascii"))
        print(recv)