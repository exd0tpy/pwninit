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
success = "["+C_BOLD + C_GREEN+"Success!"+C_END+"]"

parser = argparse.ArgumentParser(description='This tool is for pwnable binary')

parser.add_argument('binary',type=str,metavar='binary_name',help='Enter binary path(name)')

parser.add_argument('--libc',type=str,default = '',help='Enter custom libc file(optional)')


args = parser.parse_args()
binary = args.binary
libc = args.libc

print binary , libc

def print_info(text):
	space = '                            '
	space = space[:-len(text)]
	print info+text+space+success


binary_name = sys.argv[1]
# = sys.argv[2]

#exploit_data = "from pwn import*\ncontext.log_level='debug'\ns = process(\'"+binary_name+"\')\n\ns.interactive()"
exploit_data = '''from pwn import*
context.log_level='debug'
s=process([\''''+binary_name+'''\'],env={"LD_PRELOAD":"'''+libc+'''"})
s.interactive()'''

os.system('chmod +x '+binary_name)
print_info('chmod')
os.system('checksec '+binary_name)
print_info('checksec')

f = open(binary_name+"_ex"+".py","wb")

f.write(exploit_data)
print_info('exploit file create')


