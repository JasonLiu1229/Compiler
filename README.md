<br>
<img src="Pictures/UA.png" alt="drawing" style="width:150px;"/>

# Compiler

In this project, we will create a compiler from scratch.  
This compiler is capable of compiling **C language code**.  
It will be made in Python.

This project is made for the course Compilers at the **University of Antwerp**.

### Table Of contents

1. [Assignments.](#Assignments)
2. [Testing.](#Testing)
3. [Files.](#Files)
4. [Sources.](#sources)
5. [Authors.](#authors)

<a name="Assignments"></a>

### Assignments

#### TODO list

<ul>
    <li><input type="checkbox" checked> Project 1</li>
    <li><input type="checkbox" checked> Project 2</li>
    <li><input type="checkbox" checked> Project 3</li>
    <li><input type="checkbox" checked> Project 4</li>
    <ul>
        <li><input type="checkbox" checked> For loops</li>
        <li><input type="checkbox" checked> While loops</li>
        <li><input type="checkbox" checked> Break</li>
        <li><input type="checkbox" checked> Continue</li>
    </ul>
    <li><input type="checkbox" checked> Project 5</li>
    <ul>
        <li><input type="checkbox" checked> Function declarations</li>
        <li><input type="checkbox" checked> Function definitions</li>
        <li><input type="checkbox" checked> Function calls</li>
        <li><input type="checkbox" checked> Return</li>
        <li><input type="checkbox" checked> Return values and type checking / **void type**</li>
        <li><input type="checkbox" checked> No dead code after **return, break, continue**</li>
    </ul>
    <li><input type="checkbox" checked> Project 6</li>
    <ul>
        <li><input type="checkbox" checked> Arrays</li>
        <ul>
            <li><input type="checkbox" checked> Declarations</li>
            <li><input type="checkbox" checked> Access</li>
        </ul>
        <li><input type="checkbox" checked> Printf</li>
        <li><input type="checkbox" checked> Scanf</li>
        <li><input type="checkbox" checked> Includes</li>
    </ul>
    <li><input type="checkbox"> LLVM</li>
    <ul>
        <li><input type="checkbox" checked> Project 1</li>
        <li><input type="checkbox" checked> Project 2</li>
        <li><input type="checkbox" checked> Project 3</li>
        <li><input type="checkbox"> Project 4</li>
        <li><input type="checkbox"> Project 5</li>
        <li><input type="checkbox" checked> Project 6 - **Half implemented**</li>
    </ul>
    <li><input type="checkbox"> MIPS</li>
    <ul>
        <li><input type="checkbox" checked> Project 1</li>
        <li><input type="checkbox" checked> Project 2</li>
        <li><input type="checkbox"> Project 3</li>
        <li><input type="checkbox" checked> Project 4</li>
        <li><input type="checkbox" checked> Project 5</li>
        <li><input type="checkbox" checked> Project 6</li>
    </ul>
</ul>

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

| Short command | Long command    | Type    | Required                  | Description                                                                           |
|---------------|-----------------|---------|---------------------------|---------------------------------------------------------------------------------------|
| -d            | --directory     | <path\> | **Yes**                   | Directory of the input files                                                          |
| -t            | --type          | <str\>  | **Yes**                   | File extension                                                                        |
| -f            | --files         | [str]   | Exclusive. Takes priority | Files to parse                                                                        |
| -a            | --all           | NaN     | Exclusive. Least priority | Parse all the files in the directory                                                  |
| -i            | --index         | <int\>  | Exclusive                 | Parse the i-th file in the directory                                                  |
| -v            | --verbose       | NaN     | No                        | Print the AST                                                                         |
| -nw           | --no-warning    | NaN     | No                        | Do not print warnings                                                                 |
| -e            | --execute-with  | <str/>  | No                        | Execute the mips code generated for the program.<br/> Can be "spim", "mars" or "both" |
| -s            | --silent        | NaN     | No                        | Do not print the output of the program                                                |
| -nd           | --no-disclaimer | NaN     | No                        | Remove the disclaimers for "spim" and "mars" from the output                          |
| -vs           | --visualise     | NaN     | No                        | Generate a dot format file and compile it to a png                                    |
| -h            | --help          | NaN     | NaN                       | For help                                                                              |

Example code with specified input files:

    python3 -d ../input_files/ -t .c -f Project3 Project2 ...

Example code with only the input directory and file extension

    python3 -d ../input_files/ -t .c -a

Example code with only the input directory and an index

    python3 -d ../input_files/ -t .c -i 3

[//]: # (##### Script)

[//]: # (> **Warning** The LLVM class function _**execute&#40;&#41;**_ does not work on windows. Disable it when testing on windows.)

[//]: # ()
[//]: # (> How to disable?)

[//]: # (> > comment on line 36 on run.py)

#### Available tests

##### All correct programs

```shell
cd src || exit &
python3 run.py -d ../input_files/CorrectCode/fully_working/ -t .c -a -e mars -nd
```

##### All programs with errors

```shell
cd src || exit &
python3 run.py -d ../input_files/SemanticErrors/fully_working/ -t .c -a -e mars -nd
```

##### Recursive fibonacci

```shell
cd src || exit &
python3 run.py -d ../input_files/CorrectCode/fully_working/ -t .c -f fibonacciRecursive -e mars
```

##### Scanf tests

```shell
cd src || exit &
python3 run.py -d ../input_files/CorrectCode/fully_working/ -t .c -f Scanf1 Scanf2 -e mars
```

##### Printf tests

```shell
cd src || exit &
python3 run.py -d ../input_files/CorrectCode/fully_working/ -t .c -f Printf1 Printf2 Printf3 -e mars
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
    The output of the scripts: ../MIPS_output/ for asm files and ../Output/graphics for png files

<a name="sources"></a>

### Sources

<a href="https://github.com/antlr/antlr4/blob/master/doc/getting-started.md"> Antlr4 installation </a>
<br>
<a href="https://graphviz.org/doc/info/lang.html"> Dot language reference </a>
<br>
<a href="https://llvm.org/"> LLVM </a>
<br>
<a href="https://llvm.org/docs/LangRef.html"> LLVM ref. page </a>  
<br>
<a href="https://courses.missouristate.edu/kenvollmar/mars/help/syscallhelp.html"> Mips syscall info </a>
<br>
<a href="https://people.cs.pitt.edu/~childers/CS0447/lectures/mips-isa4.pdf"> while loops mips </a>
<br>
<a href="https://stackoverflow.com/questions/29832201/unaligned-address-in-store-error-when-saving-a-word"> Unaligned address in store error, using the wrong load</a>

<a name="authors"></a>

### Authors

| **Name**   | **Email**                           | **Student number** |
|------------|-------------------------------------|--------------------|
| _Jason L._ | <Jason.Liu@student.uantwerpen.be>     | 20213082           |
| _Orfeo T._ | Orfeo.Terkuç<i@student.uantwerpen.be> | 20213863           |
