import os, sys
import argparse
import mmap
import signal

parser = argparse.ArgumentParser()
parser.add_argument('-f')
args = parser.parse_args()
memoria = mmap.mmap(-1, 100)

def padre(s, f):
    memoria.seek(0)
    line = memoria.readline()
    print(line.decode())
    os.kill(h2, signal.SIGUSR1)

def end_h2(s, f):
    os._exit(0)

def end_p(s, f):
    os.kill(h2, signal.SIGUSR2)

def mayuscula(s, f):
    memoria.seek(0)
    line = memoria.readline()
    file.write(line.decode().upper())
    file.flush()
    


    
def main():
    signal.signal(signal.SIGUSR1, padre)
    signal.signal(signal.SIGUSR2, end_p)
    
    global h1
    h1 = os.fork()
    
    if h1 == 0:
        print("Ingresar linea de texto")
        for line in sys.stdin:
            if line == "bye\n":
                os.kill(os.getppid(), signal.SIGUSR2)
                os._exit(0)
            memoria.seek(0)
            memoria.write(line.encode())
            memoria.seek(0)
            os.kill(os.getppid(), signal.SIGUSR1) 
    
    else:
    
        global h2
        h2 = os.fork()
    
        if h2 == 0:
            signal.signal(signal.SIGUSR1, mayuscula)
            signal.signal(signal.SIGUSR2, end_h2)

            while True:
                signal.pause()

        else:
            os.waitpid(h1, 0)
            os.waitpid(h2, 0)
            

if __name__ == '__main__':
    file = open(args.f, 'a')
    main()