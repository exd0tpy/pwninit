import os
import sys
import argparse

C_END     = "\033[0m"
C_BOLD    = "\033[1m"
C_INVERSE = "\033[7m"
 
C_BLACK  = "\033[30m"
C_RED    = "\033[31m"
C_GREEN  = "\033[32m"
C_YELLOW = "\033[33m"
C_BLUE   = "\033[34m"
C_PURPLE = "\033[35m"
C_CYAN   = "\033[36m"
C_WHITE  = "\033[37m"
 
C_BGBLACK  = "\033[40m"
C_BGRED    = "\033[41m"
C_BGGREEN  = "\033[42m"
C_BGYELLOW = "\033[43m"
C_BGBLUE   = "\033[44m"
C_BGPURPLE = "\033[45m"
C_BGCYAN   = "\033[46m"
C_BGWHITE  = "\033[47m"

info = "["+C_BOLD + C_GREEN+"+"+C_END+"]"
info_success = "["+C_BOLD + C_GREEN+"Success!"+C_END+"]"
info_failed = "["+C_BOLD + C_RED+"Failed!"+C_END+"]"

parser = argparse.ArgumentParser(description='This tool is for pwnable binary')

parser.add_argument('-s','--strip',help='strip file extention like .dms', action='store_true')

parser.add_argument('binary',type=str,metavar='binary_name',help='binary path(name)')

parser.add_argument('--libc',type=str,default = '',help='custom libc file(optional)')


args = parser.parse_args()
binary = args.binary
libc = args.libc

print binary , libc

def print_info(text,flag):
  space = '                            '
  space = space[:-len(text)]
  if flag:
    print info+text+space+info_success
  else:
    print info+text+space+info_failed

def success(text):
  print_info(text,True)

def failed(text):
  print_info(text,False)

ori_binary_name = sys.argv[1]
if args.strip:
  binary_name = ori_binary_name.split('.')[0]
  result=os.system('mv ./'+ori_binary_name+' ./'+binary_name)
  if result == 0:
    success('change name')
  else:
    failed('change name')
else:
  binary_name = ori_binary_name
  



# = sys.argv[2]

#exploit_data = "from pwn import*\ncontext.log_level='debug'\ns = process(\'"+binary_name+"\')\n\ns.interactive()"
exploit_data = '''from pwn import*
context.log_level='debug'
s=process([\''''+binary_name+'''\'],env={"LD_PRELOAD":"'''+libc+'''"})
s.interactive()'''


result = os.system('chmod +x '+binary_name)
if result == 0:
  success('chmod')
else:
  failed('chmod')


result = os.system('checksec '+binary_name)
if result == 0:
  success('checksec')
else:
  failed('checksec')


try:
  f = open(binary_name+"_ex"+".py","wb")
  f.write(exploit_data)
  success('exploit file create')
except:
  failed('exploit file create')


