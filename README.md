<div align="center">
  <h1>Code-Bin/Dump</h>
  <img src="https://komarev.com/ghpvc/?username=1890&label=views&style=flat-square"><br>
  <h3>Bin for stuff that doesnt deserve their own repo<br>
  !Also if this isnt working DO NOT message me on discord or asking for help this is just some code i didnt rly think about not any real project!
</div>
    
<div> <!-- align="center" -->
  <h1 align="center">Compile</h>
  <h3 align="center">To be able to run these commands you need:
                          <br>- .Net5.0 (dotnet)
                          <br>- Mingw-w64 (GCC)
                          <br>- java development kit (java)  |  I  recomend the latest version (16/17 at the moment)
  <h3><pre>C# (<= .Net5.0):
        - Windows:  dotnet publish -r win-x64 -p:PublishSingleFile=true --self-contained false
        - Linux:    dotnet publish -r linux-x64 -p:PublishSingleFile=true --self-contained false
        - Mac-OS:   dotnet publish -r osx-x64 -p:PublishSingleFile=true --self-contained false
  <br>C/C++:
        - Windows:  g++ file.c          /  g++ file.cpp            --   gcc file.c         / gcc file.cpp
        - Linux:    g++ file.c          /  g++ file.cpp            --   gcc file.c         / gcc file.cpp
        - Mac-OS:   g++ -g hello.c -lm  /  g++ -g hello.cpp -lm    --   gcc -g hello.c -lm / gcc -g hello.cpp -lm
  <br>Java:
        Compile:
            - Windows/Linux/Mac-OS: javac -d ./build file.java
                                    cd ./build/
                                    jar cvf FILENAME.jar *
        Run:  
            - Windows/Linux/Mac-OS: java file.java
  </pre>
