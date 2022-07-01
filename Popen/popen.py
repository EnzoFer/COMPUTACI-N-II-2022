import argparse
import string
import subprocess as sp
import datetime as dt

parser = argparse.ArgumentParser(description = "popen")

parser.add_argument('-c', "--command", type = str)
parser.add_argument('-f',"--output_file", type = str)
parser.add_argument('-l', "--log_file", type = str)

args = parser.parse_args()

file_output = open(args.output_file, 'a')
process = sp.Popen([args.command], stdout= file_output, stderr= sp.PIPE, shell=True, universal_newlines=True)
exc = process.communicate()[1]

if not exc:
    date_time = dt.datetime.now()
    text = f"{date_time}:El comando {args.command} funciona"
    file = open(args.log_file, 'a')
    file.write(text)
    file.close()

else:
    date_time = dt.date_time.now()
    text = f"{date_time}:{exc}"
    file = open(args.log_file, 'a')
    file.write(text)
    file.close()

file_output.writelines()
file_output.close()