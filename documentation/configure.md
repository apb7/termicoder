# Configuring termicoder

### This document is still being worked out

## Configuring test scripts

We are aware that people use different compilers and systems
and hence compile commannds may vary so instead of hard coding them,
 we are using bash/batch scripts for compiling and running your code

**NOTE: we take care of passing the code file to the right language script.
 Each of compile scripts and run scripts should work only for
 the __particular__ language specified by the folder.**

To edit scripts run `termicoder test -et`.
This command launches a folder containing folders **bash** and **bat**
which contain scripts for bash and command prompt respectively.
Folders are subdivided into folders for various languages.
You only need to edit one's required by you.

**compile.sh**/**compile.bat**(only for languages c,c++,java)
these scripts are passed two arguments :
1) The code file or the program ex. `a.cpp`
2) The name of executable to be produced ex. `a`
Ihe script compiles the file a.cpp and produce a corresponding executable `a`.
Its all upto you how you handle this.
The second argument passed(the name of executable) will always be
the name of code file without the extension.
How you handle these arguments is its all upto you as run is
also handled by you so take care that they work in conjuction.

**run.sh**/**run.bat**(for all languages)
this script is passed the executable name for languages c,cpp,java
ex. `a` in the above case and the code file in case of python ex. `a.py`
the script should just run the corresponding program
we take care of input and output redirection to files.

In case of python its upto you to configure it for
python 2 or python 3, but only one of it can be chosen at a time.
