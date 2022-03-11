all:
  echo ---Help---
  echo make compile_c    | Compile and run "execute.c"
  echo make compile_cpp  | Compile adn run "execute.cpp"
  echo make run_py       | Run "execute.py" (and install requirements if needed)
  echo make clean        | Remove all ".jar .exe .o" files

compile_c:
  gcc execute.c -o execute_c.exe
  execute_c.exe
  # rm execute_c.exe

compile_cpp:
  gcc execute.cpp -o execute_cpp.exe
  execute_cpp.exe
  # rm execute_cpp.exe

run_py:
  python3 execute.py

clean:
  rm *.jar *.exe output *.o
 
