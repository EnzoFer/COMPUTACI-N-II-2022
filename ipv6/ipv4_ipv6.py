import argparse, subprocess, os, threading, socket, socketserver

class ThreadServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass
class ProcessServer(socketserver.ForkingMixIn, socketserver.TCPServer):
    pass

class ThreadServer_ipv6(socketserver.ThreadingMixIn, socketserver.TCPServer):
    address_family = socket.AF_INET6
    pass
class ProcessServer_ipv6(socketserver.ForkingMixIn, socketserver.TCPServer):
    address_family = socket.AF_INET6
    pass

class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            content = self.request.recv(1024).strip()
            if content == 'exit' or len(content) == 0:
                print(f"Cliente {self.client_address[0]} desconectado")
                exit(0)
            print(f"{self.client_address[0]}")
            command = subprocess.Popen([content], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            stdout, stderr = command.communicate()
            if command.returncode == 0:
                ans = "OK \n"+stdout
            else:
                ans = "ERROR \n"+stderr
            self.request.send(ans.encode())

def menu(d, c):

    if d[0] == socket.AF_INET:
        print("Server on ipv4")

        if args.c == "t":
            server = ThreadServer((HOST,PORT), MyServer)

        if args.c == "p":
            server = ProcessServer((HOST,PORT), MyServer)

    elif d[0] == socket.AF_INET6:
        print("Server on ipv6")

        if args.c == "t":
            server = ThreadServer_ipv6((HOST,PORT), MyServer)

        if args.c == "p":
            server = ProcessServer_ipv6((HOST,PORT), MyServer)

    server.serve_forever()

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('-p', type=int, help="Ingresar puerto")
    parser.add_argument('-c', type=str, help="'p': generar un proceso. 't'_: generar un hilo")
    args = parser.parse_args()
    
    HOST, PORT = "", args.p
    socketserver.TCPServer.allow_reuse_address = True
    directions = socket.getaddrinfo("localhost", args.p, socket.AF_UNSPEC, socket.SOCK_STREAM)
    workers = []
    
    for dir in directions:
        workers.append(threading.Thread(target=menu, args=(dir,args.p)))
    for worker in workers:
        worker.start()