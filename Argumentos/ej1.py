import sys
import getopt

argv = sys.argv[1:]

try:
    opts, arg = getopt.getopt(argv, "-o:-n:-m:")

except:
    print ("Error")

for opt, ar in opts:
    if opt in "-o":
        calculo = ar
    if opt in "-n":
        n1 = ar
    if opt in "-m":
        n2 = ar

if calculo == "+":
    print (n1, "+" ,n2, "=" ,int(n1) + int(n2))

if calculo == "-":
    print (n1, "-" ,n2, "=" ,int(n1) - int(n2))

if calculo == "/":
    print (n1, "/" ,n2, "=" ,int(n1) / int(n2))

if calculo == "x":
    print (n1, "*" ,n2, "=" ,int(n1) * int(n2))
