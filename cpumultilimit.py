# coding: UTF-8
import subprocess
import threading
import time
import traceback

from subprocess import check_output

#######config###########
#設定。limitpercentでcpulimit -l で指定するCPUの制限値
limitpercent = 30
#設定。limitprocessnameでcpulimitするプロセス名を指定する
limitprocessname ="bedrock_server"
########################

########functions#######

#cpulimitさせる関数
def cd_exec(pid):
 lp = None
 print(pid);
 try:
  lp = subprocess.Popen([ "cpulimit", "-l", str(limitpercent), "-p", str(pid)], shell=False)
 except Exception:
  traceback.print_exc()
  print("limitprocessprocessException")

#PIDをプロセス名から取得する関数
#https://stackoverflow.com/questions/26688936/how-to-get-pid-by-process-name
def scraiping_pid(processname):
 try:
  #コマンド出力をlistにするー＞utf-8としてデコードー＞setでリターン
  maped = set([i.decode("utf-8") for i in check_output(["pidof", processname]).split()])
  print(maped)
  return maped
 except Exception:
  traceback.print_exc()
  print("scraiping_pidException")

########################


########Main Thread#####

pidsmap = scraiping_pid(limitprocessname)
print("pidsmap:"+str(pidsmap))
#pid一覧に基づきcpulimitを投げる
for p in pidsmap:
 thread_1 = threading.Thread(target=cd_exec(p))

while True:
 newpid = scraiping_pid(limitprocessname)

 print("/////////")
 print("newpid:" + str(newpid))
 print("pidsmap:" + str(pidsmap))
 #まれにAttributeError: 'NoneType' object has no attribute 'difference'を吐くのでtryexceptで。
 try:
  # https://xwave.exblog.jp/11309038/
  # https://note.nkmk.me/python-list-str-num-conversion/
  # 差分で回す　newpidにあって、pidsmapにないpidを求める
  list_ab = newpid.difference(pidsmap)
  print("list_ab:" + str(list_ab))
  print("*********")

  for l in list_ab:
   thread_2 = threading.Thread(target=cd_exec(l))
 except Exception:
  traceback.print_exc()
#新しいpidsを設定
 pidsmap = newpid
 #pidofコマンドを連射しないように休む
 time.sleep(10)


########################

