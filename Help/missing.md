# Missing features

## Const variabelen:
```shell
python3 ../src/run.py -d ../input_files/CorrectCode/fully_working/ -t .c -f variableConst -e spim -nd -v
```
[variableConst.c](../input_files/CorrectCode/fully_working/variableConst.c)  
[variableConst.asm](../MIPS_output/variableConst.asm)

## Constant folding
```shell
python3 ../src/run.py -d ../input_files/CorrectCode/fully_working/ -t .c -f constantFolding constantFolding2 -e spim -nd -v
```
[constantFolding.c](../input_files/CorrectCode/fully_working/constantFolding.c) and
[constantFolding2.c](../input_files/CorrectCode/fully_working/constantFolding2.c)  
[constantFolding.asm](../MIPS_output/constantFolding.asm) and
[constantFolding2.asm](../MIPS_output/constantFolding2.asm)

## Constant propagation:
```shell
python3 ../src/run.py -d ../input_files/CorrectCode/fully_working/ -t .c -f constantPropagation -e spim -nd -v
```

## R-value assignment:
```shell
python3 ../src/run.py -d ../input_files/SemanticErrors/fully_working/ -t .c -f rvalueAssignment1 rvalueAssignment2 -e spim -nd -v
```
[rvalueAssignment1.c](../input_files/SemanticErrors/fully_working/rvalueAssignment1.c) and
[rvalueAssignment2.c](../input_files/SemanticErrors/fully_working/rvalueAssignment2.c)

## Const re-assignment:
```shell
python3 ../src/run.py -d ../input_files/SemanticErrors/fully_working/ -t .c -f constReassignment -e spim -nd -v
```
