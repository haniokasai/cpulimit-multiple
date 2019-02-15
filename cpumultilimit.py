# coding: UTF-8
import subprocess
import threading
import time
import traceback

from subprocess import check_output

#######config###########


limitpercent = 30
limitprocessname ="bedrock_server"

########################

########functions#######

def cd_exec(pid):
 lp = None
 print(pid);
 try:
  lp = subprocess.Popen([ "cpulimit", "-l", str(limitpercent), "-p", str(pid)], shell=False)
 except Exception:
  traceback.print_exc()
  print("limitprocessprocessException")

#https://stackoverflow.com/questions/26688936/how-to-get-pid-by-process-name

def scraiping_pid(processname):
 try:
  maped = map(int, check_output(["pidof", processname]).split())
  print(maped)
  return maped
 except Exception:
  traceback.print_exc()
  print("scraiping_pidException")

########################


########Main Thread#####

pidsmap = scraiping_pid(limitprocessname)
print("pidsmap:"+str(pidsmap))
for p in pidsmap:
 thread_1 = threading.Thread(target=cd_exec(p))

while True:
 newpid = scraiping_pid(limitprocessname)
 print("pidsmap:" + str(newpid))
 #差分で回す　newpid,pidsmap
 #https://xwave.exblog.jp/11309038/
 set_ab = set(newpid) - set(pidsmap)
 list_ab = list(set_ab)
 print("list_ab:" + str(list_ab))
 for l in list_ab:
  thread_2 = threading.Thread(target=cd_exec(l))

 pidsmap = newpid
 time.sleep(60)


########################

