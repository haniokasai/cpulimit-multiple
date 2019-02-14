# coding: UTF-8
import subprocess
import threading
from subprocess import check_output

#######config###########

limitpercent = 30
limitprocessname ="bedrock_server"

########################

########functions#######

def cd_exec(pid):
 lp = None
 try:
  lp = subprocess.Popen([ "cpulimit", "-l", limitpercent, "-p",pid ], shell=False)
  lp.wait()
 except Exception:
  print("limitprocessprocessException")

#https://stackoverflow.com/questions/26688936/how-to-get-pid-by-process-name

def scraiping_pid(processname):
 try:
  maped = map(int, check_output(["pidof", processname]).split())
  print(maped)
  return maped
 except Exception:
  print("scraiping_pidException")

def checkschedule(pid):


########################


########Main Thread#####

pidsmap = scraiping_pid(limitprocessname)
for p in pidsmap:
 thread_1 = threading.Thread(target=cd_exec(p))

while True:
 newpid = scraiping_pid(limitprocessname)
 #差分で回す　newpid,pidsmap
 thread_1 = threading.Thread(target=cd_exec(p))
 pidsmap = newpid
 

########################

