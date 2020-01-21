import os
import subprocess
import shlex
import sys
verbose = len(sys.argv) > 1 and sys.argv[1] == '-v'
if(verbose):
    import difflib
cwd = os.getcwd()

def runTest(folderName):
    config = subprocess.Popen(shlex.split('python3 initiate.py "'+folderName+'"/config.txt'), cwd=cwd)
    config.communicate()
    actions = subprocess.Popen(shlex.split('python3 action.py "'+folderName+'"/action.txt'), stdout=subprocess.PIPE, cwd=cwd)
    out = actions.communicate()[0].decode('utf-8')
    expectedOut = open(''+folderName+'/expectedOut.txt').read()
    if(out != expectedOut):
        print("Test "+folderName[5:]+" returned unexpected output")
        if(verbose):
            print("Output was: "+out)
            print("----------\nDifference is: ")
            for i,s in enumerate(difflib.ndiff(expectedOut, out)):
                if s[0]==' ': continue
                elif s[0]=='-':
                    print(u'Output missing "{}" from position {}'.format(s[-1],i))
                elif s[0]=='+':
                    print(u'Output added "{}" in position {}'.format(s[-1],i))    
    else:
        print("Test "+folderName[5:]+" Passed!")


for folder in os.listdir(cwd):
    if(folder[0:5] == "test "):
        runTest(folder)