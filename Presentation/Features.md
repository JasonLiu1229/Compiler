# All working features
> These are all the working features of the project.
 
## Features
Compile all `.c` files.
```shell
python3 ../src/run.py -d ../input_files/CorrectCode/fully_working/ -t .c -a -e spim
```
The output of the scripts is located in the `MIPS_output` folder.
### Mandatory features
#### Correct code
> Binary operations
```shell
python3 ../src/run.py -d ../input_files/CorrectCode/fully_working/ -t .c -f binaryOperations1 \
binaryOperations2 -e spim -nd
```
> Comparison operations
```shell
python3 ../src/run.py -d ../input_files/CorrectCode/fully_working/ -t .c -f comparisons1 \
comparisons2 -e spim -nd
```
> Unary operations
```shell
python3 ../src/run.py -d ../input_files/CorrectCode/fully_working/ -t .c -f unaryOperations \
-e spim -nd
```
> Variables
>> Types: int, float, char
```shell
python3 ../src/run.py -d ../input_files/CorrectCode/fully_working/ -t .c -f variables1 \
variables2 variables5 -e spim -nd
```
>> Pointers
```shell
python3 ../src/run.py -d ../input_files/CorrectCode/fully_working/ -t .c -f variables4 \
variables6 dereferenceAssignment -e spim -nd
```
>> Arrays
```shell
python3 ../src/run.py -d ../input_files/CorrectCode/fully_working/ -t .c -f variables3 \
variables7 variables8 -e spim -nd
```
> Conditionals: if, else, scopes
```shell
python3 ../src/run.py -d ../input_files/CorrectCode/fully_working/ -t .c -f if ifElse \
scoping  -e spim -nd
```
> Loops: while, for
```shell
python3 ../src/run.py -d ../input_files/CorrectCode/fully_working/ -t .c -f for while -e spim -nd
```
> Functions
>> Forward declaration
```shell
python3 ../src/run.py -d ../input_files/CorrectCode/fully_working/ -t .c -f \
forwardDeclaration -e spim -nd
```
>> Recursive
```shell
python3 ../src/run.py -d ../input_files/CorrectCode/fully_working/ -t .c -f fibonacciRecursive \
-e spim -nd
```
>> General tests
```shell
python3 ../src/run.py -d ../input_files/CorrectCode/fully_working/ -t .c -f pointerArgument \
prime -e spim -nd
```
> Printf
```shell
python3 ../src/run.py -d ../input_files/CorrectCode/fully_working/ -t .c -f printf1 printf2 \
printf3 -e spim -nd
```
> Scanf
```shell
python3 ../src/run.py -d ../input_files/CorrectCode/fully_working/ -t .c -f scanf1 scanf2 \
-e spim -nd
```
#### Semantic errors
> Incompatible types
>> Working because of conversions
```shell
python3 ../src/run.py -d ../input_files/SemanticErrors/fully_working/ -t .c -f \
incompatibleTypes1 incompatibleTypes2 incompatibleTypes4 incompatibleTypes5 \
incompatibleTypes6 incompatibleTypes7  -e spim -nd
```
>> Errors, as intended
```shell
python3 ../src/run.py -d ../input_files/SemanticErrors/fully_working/ -t .c -f \
incompatibleTypes3  -e spim -nd
```
> Undeclared variables
```shell
python3 ../src/run.py -d ../input_files/SemanticErrors/fully_working/ -t .c -f \
undeclaredVariable1 undeclaredVariable2 undeclaredVariable3  -e spim -nd
```
> Redeclared variables
```shell
python3 ../src/run.py -d ../input_files/SemanticErrors/fully_working/ -t .c -f \
variableRedefinition1 variableRedefinition2 variableRedefinition3 variableRedefinition4 \
variableRedefinition5 variableRedefinition6 -e spim -nd
```
> Undeclared functions
```shell
python3 ../src/run.py -d ../input_files/SemanticErrors/fully_working/ -t .c -f \
undeclaredFunction -e spim -nd
```
> Redeclared functions
```shell
python3 ../src/run.py -d ../input_files/SemanticErrors/fully_working/ -t .c -f \
declarationDeclarationMismatch1 declarationDeclarationMismatch2 \
declarationDeclarationMismatch3 -e spim -nd
```
> Redefined functions
```shell
python3 ../src/run.py -d ../input_files/SemanticErrors/fully_working/ -t .c -f \
declarationDefinitionMismatch1 declarationDefinitionMismatch2 \
declarationDefinitionMismatch3 functionRedefinition1 functionRedefinition2 \
 functionRedefinition3 -e spim -nd
```
> Definition in local scope
```shell
python3 ../src/run.py -d ../input_files/SemanticErrors/fully_working/ -t .c -f \
definitionInLocalScope -e spim -nd
```
> Parameter mismatch
```shell
python3 ../src/run.py -d ../input_files/SemanticErrors/fully_working/ -t .c -f \
functionCallargumentmismatch1 functionCallargumentmismatch2 functionCallargumentmismatch3 \
functionCallargumentmismatch4 -e spim -nd
```
> Parameter redefinition
```shell
python3 ../src/run.py -d ../input_files/SemanticErrors/fully_working/ -t .c -f \
parameterRedefinition1 parameterRedefinition2
 parameterRedefinition3 -e spim -nd
```
> Return type mismatch
```shell
python3 ../src/run.py -d ../input_files/SemanticErrors/fully_working/ -t .c -f \
returnTypeMismatch -e spim -nd
```
> Invalid include
```shell
python3 ../src/run.py -d ../input_files/SemanticErrors/fully_working/ -t .c -f \
invalidIncludeError -e spim -nd
```
> Main not found
```shell
python3 ../src/run.py -d ../input_files/SemanticErrors/fully_working/ -t .c -f mainNotFound -e spim -nd
```
> Return outside function
```shell
python3 ../src/run.py -d ../input_files/SemanticErrors/fully_working/ -t .c -f returnOutsideFunction -e spim -nd
```
> Dereference type mismatch
```shell
python3 ../src/run.py -d ../input_files/SemanticErrors/fully_working/ -t .c -f dereferenceTypeMismatch1 \
dereferenceTypeMismatch2 -e spim -nd
```
> Array errors
```shell
python3 ../src/run.py -d ../input_files/SemanticErrors/fully_working/ -t .c -f arrayAccesstypeMismatch \
arrayAccesstypeMismatch2
 arrayCompareError arraySizeTypeMismatch -e spim -nd
```
> Continue and break outside loop
```shell
python3 ../src/run.py -d ../input_files/SemanticErrors/fully_working/ -t .c -f invalidLoopControlStatement -e spim -nd
```
> Invalid operations
```shell
python3 ../src/run.py -d ../input_files/SemanticErrors/fully_working/ -t .c -f invalidUnaryOperation \
pointerOperationError -e spim -nd
```

### Optional features
> Implicit casting
```shell
python3 ../src/run.py -d ../input_files/CorrectCode/fully_working/ -t .c -f floatToIntConversion \
intToFloatconversion  -e spim -nd
```
> Modulo
```shell
python3 ../src/run.py -d ../input_files/CorrectCode/fully_working/ -t .c -f modulo -e spim -nd
```
> Increment and decrement
```shell
python3 ../src/run.py -d ../input_files/CorrectCode/fully_working/ -t .c -f increment decrement -e spim -nd
```
> Switch
```shell
python3 ../src/run.py -d ../input_files/CorrectCode/fully_working/ -t .c -f switch1 switch2 -e spim -nd
```
> No code for unused variables
```shell
python3 ../src/run.py -d ../input_files/CorrectCode/fully_working/ -t .c -f unusedVariables -e spim -nd
```
> Comments
```shell
python3 ../src/run.py -d ../input_files/CorrectCode/fully_working/ -t .c -f comments -e spim -nd
```
>> [.asm file for comment test](../MIPS_output/comments.asm)


## Authors
| **Name**   | **Email**                           | **Student number** |
|------------|-------------------------------------|--------------------|
| _Jason L._ | Jason.Liu@student.uantwerpen.be     | 20213082           |
| _Orfeo T._ | Orfeo.Terkuçi@student.uantwerpen.be | 20213863           |