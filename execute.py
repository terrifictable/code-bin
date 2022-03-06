import subprocess
import os

def execute_cmd(cmd) -> str:
     stdout, stderr = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).communicate()
     return stdout.strip().decode('ISO-8859-1')

def execute_js(cmd) -> str:
       with open("./temp.js", "w") as f:
               f.write(cmd)
       stdout, stderr = subprocess.Popen("node temp.js", shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).communicate()
       os.remove("./temp.js")
       return stdout.decode("ISO-8859-1")
    
def execute_c(cmd):
    with open("./temp.c", "w") as f:
        f.write(cmd)

    try:
        subprocess.Popen("gcc temp.c", shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        stdout, _ = subprocess.Popen("a.exe", shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).communicate()

        os.remove("./temp.c")
        os.remove("./a.exe")

        return stdout.decode("ISO-8859-1")
    except Exception as e:
        return e

def execute_func(val, func): func(val)
  
print(execute_func("Hello World!", print))
print(execute_js("""console.log("Hello World!")"""))
print(execute_c("""#include <stdio.h>\nint main() { printf("Hello World!"); }"""))
print(execute_cmd("echo Hello World"))
