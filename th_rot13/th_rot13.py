import threading as th
import os
import sys
import codecs
import queue

def h1(w, q):
    sys.stdin = open(0)
    line = sys.stdin.readline()
    os.write(w, line.encode('ascii'))
    line = q.get()
    q.task_done()
    

def h2(q,r):
    line = os.read(r,100).decode()
    line = rot13(line)
    q.put(line)
    q.join()

def rot13(line):
    line_rot13 = codecs.encode(line, 'rot_13')
    return line_rot13

def main():
    r,w = os.pipe()
    q = queue.LifoQueue()

hilo = th.Thread(target = h1, args = (w,q))
hilo2 = th.Thread(target = h2, args = (q,r))

hilo.start()
hilo2.start()
hilo.join()
hilo2.join()

if __name__ == '__main__':
    main()