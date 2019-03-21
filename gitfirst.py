import subprocess
import sys

if (not len(sys.argv)==2):
 print("Automate first upload to git. usage: python gitfirst.py https://github.com/...")
 sys.exit(0)

commands = [
"git init",
"git add -A",
"git commit -m \"first commit\"",
"git remote add origin %s" %(sys.argv[1]),
"git push -u origin master"
]

for i in commands:
 try:
  print(subprocess.check_output(i, shell=True))
 except Exception as e:
  print("error at %s. skipping.."%(str(e)))
