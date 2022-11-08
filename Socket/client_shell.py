import socket, sys, argparse

parser = argparse.ArgumentParser()
parser.add_argument('-ht', help="Ingrese host del servidor")
parser.add_argument('-p', type=int, help="Ingrese puerto del servidor")
args = parser.parse_args()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
h = args.ht
p = args.p
s.connect((h, p))

while True:
    command = input('> ')
    if len(command) == 0 or command == "exit":
        print("Saliendo...")
        s.send(command.encode("ascii"))
        break
    else:
        s.send(command.encode("ascii"))
        recv = str(s.recv(1024).decode("ascii"))
        print(recv)
