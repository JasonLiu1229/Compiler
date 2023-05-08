<br>
<img src="Pictures/UA.png" alt="drawing" style="width:150px;"/>

# Compiler
In this project, we will create a compiler from scratch.  
This compiler is capable of compiling **C language code**.  
It will be made in Python.

This project is made for the course Compilers at the **University of Antwerp**.

### Table Of contents
1. [ Assignments. ](#Assignments)
2. [ Testing. ](#Testing)
3. [ Files. ](#Files)
4. [ Sources. ](#sources)
5. [ Authors. ](#authors)

<a name="Assignments"></a>
### Assignments

#### TODO list
- [x] Project 1
- [x] Project 2
- [x] Project 3
- [X] Project 4
  - [X] For loops
  - [X] While loops
  - [X] Break
  - [X] Continue
- [X] Project 5
  - [X] Function declarations
  - [X] Function definitions
  - [X] Function calls
  - [X] Return
  - [X] Return values and type checking / **void type**
  - [X] No dead code after **return, break, continue**
- [X] Project 6
  - [X] Arrays
    - [X] Declarations
    - [X] Access
  - [X] Printf
  - [X] Scanf
  - [X] Includes
- [ ] LLVM
  - [ ] Project 1
  - [ ] Project 2
  - [ ] Project 3
  - [ ] Project 4
  - [ ] Project 5
  - [ ] Project 6
- [ ] MIPS
  - [ ] Project 1
  - [ ] Project 2
  - [ ] Project 3
  - [ ] Project 4
  - [ ] Project 5
  - [ ] Project 6

<a name="Testing"></a>
### Testing
Guide on how to test our Compiler, the guide is meant for Pycharm users.

Check if the following path is set right. You could do this by running it on Pycharm, or Terminal, or by script.
If you do it in the terminal, match the **"parameters"** option of pycharm with the parameters in the Terminal.
#### Jetbrains Pycharm
<img src="Pictures/config.png" alt="drawing" style="width:600px;"></img>

#### Terminal
There are two ways to run it via terminal
Common parameter settings:

| Short command | Long command | Type    | Required                  | Description                          |
|---------------|--------------|---------|---------------------------|--------------------------------------|
| -d            | --directory  | <path\> | **Yes**                   | Directory of the input files         |
| -t            | --type       | <str\>  | **Yes**                   | File extension                       |
| -f            | --files      | [str]   | Exclusive. Takes priority | Files to parse                       |
| -a            | --all        | NaN     | Exclusive. Least priority | Parse all the files in the directory |
| -i            | --index      | <int\>  | Exclusive                 | Parse the i-th file in the directory |
| -h            | --help       | NaN     | NaN                       | For help                             |

Example code with specified input files:

    python3 -d ../input_files/ -t .c -f Project3 Project2 ...
    
Example code with only the input directory and file extension
    
    python3 -d ../input_files/ -t .c -a

Example code with only the input directory and an index
    
    python3 -d ../input_files/ -t .c -i 3

 
##### Script
> **Warning** The LLVM class function _**execute()**_ does not work on windows. Disable it when testing on windows.

> How to disable?
> > comment on line 36 on run.py

#### Available tests
##### Simple tests for projects 1-3
```shell
cd src || exit &
python3 run.py -d ../input_files/ -t .c -a
```
##### Projects 1-3 without main
```shell
cd src || exit &
python3 run.py -d ../input_files/projecten_123_zonder_main/ -t .c -a
```

#### Compiling the grammar
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
<a href="https://github.com/antlr/antlr4/blob/master/doc/getting-started.md"> Antlr4 installation </a>
<br>
<a href="https://graphviz.org/doc/info/lang.html"> Dot language reference </a>
<br>
<a href="https://llvm.org/"> LLVM </a>
<br>
<a href="https://llvm.org/docs/LangRef.html"> LLVM ref. page </a>  


<a name="authors"></a>
### Authors
| **Name**   | **Email**                           | **Student number** |
|------------|-------------------------------------|--------------------|
| _Jason L._ | Jason.Liu@student.uantwerpen.be     | 20213082           |
| _Orfeo T._ | Orfeo.Terkuçi@student.uantwerpen.be | 20213863           |
