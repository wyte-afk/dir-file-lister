import subprocess

# file and directory listing ; by "github.com/wyte4"

returned_text = subprocess.check_output("dir", shell=True, universal_newlines=True)

print('\nA cool dir files lister by ©wyte4\n')
print(returned_text)