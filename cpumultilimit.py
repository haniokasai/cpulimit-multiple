# coding: UTF-8
import subprocess
from subprocess import check_output

#######config###########

limitpercent = 30
limitprocessname ="bedrock_server"

########################

########functions#######

def cd_exec(self,pid):
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

########################


########Main Thread#####

scraiping_pid("bedrock_server")

########################

