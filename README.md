# Compiler
In this project we will create a compiler from scratch. The compiler we are programming, 
is a compiler for c. This compiler will be made in Python.

This project is made for the course Compilers at the University of Antwerp.

### Table Of contents
1. [ Assignments. ](#Assignments)
2. [ Testing. ](#Testing)
3. [ Files. ](#Files)
4. [ Sources. ](#sources)
5. [ Authors. ](#authors)

<a name="Assignments"></a>
### Assignments

#### Project 1
    - Installing Antlr
    - Constructing the grammar
    - Dot format visualisation

#### Project 2
    - Expanding the grammar with variables

#### Project 3
    - Adding comments "//" and multiline comments "/**/"
    - Convert C -> LLVM

#### Project 4

#### Project 5

#### Project 6

#### TODO list
- [x] Project 1
- [x] Project 2
- [x] Project 3
- [ ] Project 4
- [ ] Project 5
- [ ] Project 6
- [ ] LLVM
- [ ] MIPS

<a name="Testing"></a>
### How to test?
Guide on how to test our Compiler, the guide is meant for Pycharm users.

Check if the following path is set right. You could do this by running it on Pycharm, or Terminal, or by script.
If you do it in the terminal, match the parameters option of pycharm with the parameters in the Terminal.
#### Jetbrains Pycharm
<img src="Pictures/config.png" alt="drawing" style="width:600px;"></img>

#### Terminal
There are two ways to run it via terminal
Common parameter settings:
- -d : <path\>  : directory of the input files
- -t : <str\>   : file extension
- -f : [str]    : files to parse
- -a : parse all the files in the directory
- -h : for help
- -i : by index

Example code with specified input files:

    python3 -d ../input_files/ -t .c -f Project3 Project2 ...
    
Example code with only the input directory and file extension
    
    python3 -d ../input_files/ -t .c -a

 
##### Script
> **Warning** The LLVM class function _**execute()**_ does not work on windows. Disable it when testing on windows.

> How to disable?
> > comment out line 29 on run.py

```shell
cd src || exit &
python3 run.py -d ../input_files/ -t .c -a
```
How to compile the grammar:
1. Go to Grammar folder using ```cd``` command
2. Execute the following command:
```shell
antlr4 -o ../src/output -listener -visitor -Dlanguage=Python3 Math.g4  
```

<a name="Files"></a>
### Files
    Grammar: ../Grammars/Math.g4
    Python scripts: ../src/
    C Files: ../input_files/
    The output of the scripts: ../Output/

<a name="sources"></a>
### Sources
[ https://github.com/antlr/antlr4/blob/master/doc/getting-started.md ](#Antlr) --- Antlr installation  
[ https://graphviz.org/doc/info/lang.html ](#Dot_language) --- Dot language   
[ https://llvm.org/ ](#LLVM) --- LLVM  
[ https://llvm.org/docs/LangRef.html ](#LLVM refernce page) --- LLVM ref. page

<a name="authors"></a>
### Authors
| **Name**   | **Email**                           | **Student number** |
|------------|-------------------------------------|--------------------|
| _Jason L._ | Jason.Liu@student.uantwerpen.be     | 20213082           |
| _Orfeo T._ | Orfeo.Terkuçi@student.uantwerpen.be | 20213863           |


<br>
<img src="Pictures/UA.png" alt="drawing" style="width:150px;"/>