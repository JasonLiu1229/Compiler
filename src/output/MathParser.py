# Generated from Math.g4 by ANTLR 4.11.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,59,682,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,1,0,5,0,78,8,0,10,0,
        12,0,81,9,0,1,0,1,0,1,0,5,0,86,8,0,10,0,12,0,89,9,0,1,0,3,0,92,8,
        0,1,0,1,0,4,0,96,8,0,11,0,12,0,97,1,0,3,0,101,8,0,5,0,103,8,0,10,
        0,12,0,106,9,0,1,0,1,0,1,1,1,1,4,1,112,8,1,11,1,12,1,113,1,1,3,1,
        117,8,1,1,1,1,1,4,1,121,8,1,11,1,12,1,122,1,1,3,1,126,8,1,1,1,1,
        1,4,1,130,8,1,11,1,12,1,131,1,1,3,1,135,8,1,1,1,1,1,4,1,139,8,1,
        11,1,12,1,140,1,1,3,1,144,8,1,1,1,1,1,4,1,148,8,1,11,1,12,1,149,
        1,1,3,1,153,8,1,1,1,3,1,156,8,1,1,2,3,2,159,8,2,1,2,1,2,1,2,1,2,
        5,2,165,8,2,10,2,12,2,168,9,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,5,3,179,8,3,10,3,12,3,182,9,3,1,3,3,3,185,8,3,1,3,1,3,1,3,1,3,
        1,3,3,3,192,8,3,1,3,1,3,3,3,196,8,3,1,4,1,4,1,4,3,4,201,8,4,1,5,
        1,5,1,5,1,5,1,5,3,5,208,8,5,1,5,1,5,1,5,5,5,213,8,5,10,5,12,5,216,
        9,5,1,5,3,5,219,8,5,1,5,1,5,1,5,1,6,1,6,1,6,5,6,227,8,6,10,6,12,
        6,230,9,6,1,7,3,7,233,8,7,1,7,1,7,3,7,237,8,7,1,7,5,7,240,8,7,10,
        7,12,7,243,9,7,1,7,1,7,1,7,3,7,248,8,7,1,7,3,7,251,8,7,1,7,1,7,5,
        7,255,8,7,10,7,12,7,258,9,7,1,7,3,7,261,8,7,1,7,1,7,1,7,3,7,266,
        8,7,3,7,268,8,7,1,8,3,8,271,8,8,1,8,1,8,3,8,275,8,8,1,8,5,8,278,
        8,8,10,8,12,8,281,9,8,1,8,1,8,1,8,3,8,286,8,8,1,8,1,8,1,8,1,9,3,
        9,292,8,9,1,9,1,9,3,9,296,8,9,1,9,5,9,299,8,9,10,9,12,9,302,9,9,
        1,9,1,9,1,9,3,9,307,8,9,1,9,1,9,1,10,1,10,1,10,4,10,314,8,10,11,
        10,12,10,315,1,11,1,11,1,11,1,11,3,11,322,8,11,1,12,1,12,1,12,3,
        12,327,8,12,1,12,1,12,1,13,1,13,1,13,4,13,334,8,13,11,13,12,13,335,
        1,13,3,13,339,8,13,1,13,1,13,1,13,5,13,344,8,13,10,13,12,13,347,
        9,13,1,13,3,13,350,8,13,1,13,1,13,5,13,354,8,13,10,13,12,13,357,
        9,13,1,13,3,13,360,8,13,1,13,1,13,5,13,364,8,13,10,13,12,13,367,
        9,13,1,13,3,13,370,8,13,1,13,1,13,4,13,374,8,13,11,13,12,13,375,
        1,13,3,13,379,8,13,1,13,5,13,382,8,13,10,13,12,13,385,9,13,1,13,
        1,13,1,14,1,14,1,14,1,14,1,14,5,14,394,8,14,10,14,12,14,397,9,14,
        1,15,1,15,1,15,4,15,402,8,15,11,15,12,15,403,1,15,3,15,407,8,15,
        1,15,1,15,1,15,5,15,412,8,15,10,15,12,15,415,9,15,1,15,3,15,418,
        8,15,1,15,1,15,5,15,422,8,15,10,15,12,15,425,9,15,1,15,3,15,428,
        8,15,1,15,1,15,5,15,432,8,15,10,15,12,15,435,9,15,1,15,3,15,438,
        8,15,1,15,1,15,4,15,442,8,15,11,15,12,15,443,1,15,3,15,447,8,15,
        1,15,1,15,1,15,5,15,452,8,15,10,15,12,15,455,9,15,1,15,1,15,1,16,
        1,16,1,16,5,16,462,8,16,10,16,12,16,465,9,16,1,17,1,17,1,17,5,17,
        470,8,17,10,17,12,17,473,9,17,1,18,3,18,476,8,18,1,18,1,18,1,18,
        1,18,3,18,482,8,18,1,18,1,18,1,18,1,18,1,18,1,18,5,18,490,8,18,10,
        18,12,18,493,9,18,1,18,1,18,1,18,1,18,3,18,499,8,18,1,18,1,18,1,
        18,1,18,1,18,3,18,506,8,18,1,19,1,19,1,19,1,19,1,19,1,19,1,20,1,
        20,1,20,1,20,1,20,1,20,3,20,520,8,20,1,21,1,21,1,21,1,22,1,22,1,
        22,1,22,1,22,1,22,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,
        23,1,24,1,24,1,24,1,24,1,24,1,24,3,24,547,8,24,1,25,1,25,1,25,1,
        25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,3,25,562,8,25,1,
        26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,3,26,574,8,26,1,
        27,1,27,1,27,1,27,1,27,3,27,581,8,27,1,28,1,28,1,28,1,28,1,28,1,
        28,1,28,1,28,1,28,1,28,1,28,1,28,3,28,595,8,28,1,29,1,29,1,29,1,
        29,1,29,1,30,1,30,1,30,1,30,3,30,606,8,30,1,31,5,31,609,8,31,10,
        31,12,31,612,9,31,1,31,1,31,1,32,1,32,1,33,1,33,1,33,1,33,1,33,1,
        33,1,33,1,33,1,33,1,33,1,33,1,33,5,33,630,8,33,10,33,12,33,633,9,
        33,1,34,1,34,1,34,1,34,3,34,639,8,34,1,34,1,34,1,34,1,34,1,34,1,
        34,1,34,1,34,1,34,1,34,1,34,5,34,652,8,34,10,34,12,34,655,9,34,1,
        35,1,35,1,35,1,35,1,35,1,35,1,35,3,35,664,8,35,1,36,1,36,1,36,1,
        36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,3,36,678,8,36,1,37,1,
        37,1,37,1,315,2,66,68,38,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,
        30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,
        74,0,7,2,0,1,1,57,57,3,0,40,40,42,42,44,44,3,0,39,39,41,41,43,43,
        1,0,45,46,1,0,34,36,1,0,50,51,1,0,28,30,775,0,79,1,0,0,0,2,155,1,
        0,0,0,4,158,1,0,0,0,6,195,1,0,0,0,8,200,1,0,0,0,10,202,1,0,0,0,12,
        223,1,0,0,0,14,267,1,0,0,0,16,270,1,0,0,0,18,291,1,0,0,0,20,310,
        1,0,0,0,22,321,1,0,0,0,24,323,1,0,0,0,26,330,1,0,0,0,28,388,1,0,
        0,0,30,398,1,0,0,0,32,458,1,0,0,0,34,466,1,0,0,0,36,505,1,0,0,0,
        38,507,1,0,0,0,40,513,1,0,0,0,42,521,1,0,0,0,44,524,1,0,0,0,46,530,
        1,0,0,0,48,546,1,0,0,0,50,561,1,0,0,0,52,573,1,0,0,0,54,580,1,0,
        0,0,56,594,1,0,0,0,58,596,1,0,0,0,60,605,1,0,0,0,62,610,1,0,0,0,
        64,615,1,0,0,0,66,617,1,0,0,0,68,638,1,0,0,0,70,663,1,0,0,0,72,677,
        1,0,0,0,74,679,1,0,0,0,76,78,3,38,19,0,77,76,1,0,0,0,78,81,1,0,0,
        0,79,77,1,0,0,0,79,80,1,0,0,0,80,104,1,0,0,0,81,79,1,0,0,0,82,103,
        3,2,1,0,83,91,3,16,8,0,84,86,5,1,0,0,85,84,1,0,0,0,86,89,1,0,0,0,
        87,85,1,0,0,0,87,88,1,0,0,0,88,92,1,0,0,0,89,87,1,0,0,0,90,92,5,
        57,0,0,91,87,1,0,0,0,91,90,1,0,0,0,92,103,1,0,0,0,93,100,3,18,9,
        0,94,96,5,1,0,0,95,94,1,0,0,0,96,97,1,0,0,0,97,95,1,0,0,0,97,98,
        1,0,0,0,98,101,1,0,0,0,99,101,5,57,0,0,100,95,1,0,0,0,100,99,1,0,
        0,0,101,103,1,0,0,0,102,82,1,0,0,0,102,83,1,0,0,0,102,93,1,0,0,0,
        103,106,1,0,0,0,104,102,1,0,0,0,104,105,1,0,0,0,105,107,1,0,0,0,
        106,104,1,0,0,0,107,108,5,0,0,1,108,1,1,0,0,0,109,116,3,4,2,0,110,
        112,5,1,0,0,111,110,1,0,0,0,112,113,1,0,0,0,113,111,1,0,0,0,113,
        114,1,0,0,0,114,117,1,0,0,0,115,117,5,57,0,0,116,111,1,0,0,0,116,
        115,1,0,0,0,117,156,1,0,0,0,118,125,3,36,18,0,119,121,5,1,0,0,120,
        119,1,0,0,0,121,122,1,0,0,0,122,120,1,0,0,0,122,123,1,0,0,0,123,
        126,1,0,0,0,124,126,5,57,0,0,125,120,1,0,0,0,125,124,1,0,0,0,126,
        156,1,0,0,0,127,134,3,66,33,0,128,130,5,1,0,0,129,128,1,0,0,0,130,
        131,1,0,0,0,131,129,1,0,0,0,131,132,1,0,0,0,132,135,1,0,0,0,133,
        135,5,57,0,0,134,129,1,0,0,0,134,133,1,0,0,0,135,156,1,0,0,0,136,
        143,3,10,5,0,137,139,5,1,0,0,138,137,1,0,0,0,139,140,1,0,0,0,140,
        138,1,0,0,0,140,141,1,0,0,0,141,144,1,0,0,0,142,144,5,57,0,0,143,
        138,1,0,0,0,143,142,1,0,0,0,144,156,1,0,0,0,145,152,3,56,28,0,146,
        148,5,1,0,0,147,146,1,0,0,0,148,149,1,0,0,0,149,147,1,0,0,0,149,
        150,1,0,0,0,150,153,1,0,0,0,151,153,5,57,0,0,152,147,1,0,0,0,152,
        151,1,0,0,0,153,156,1,0,0,0,154,156,3,30,15,0,155,109,1,0,0,0,155,
        118,1,0,0,0,155,127,1,0,0,0,155,136,1,0,0,0,155,145,1,0,0,0,155,
        154,1,0,0,0,156,3,1,0,0,0,157,159,5,11,0,0,158,157,1,0,0,0,158,159,
        1,0,0,0,159,160,1,0,0,0,160,166,5,25,0,0,161,162,3,54,27,0,162,163,
        5,2,0,0,163,165,1,0,0,0,164,161,1,0,0,0,165,168,1,0,0,0,166,164,
        1,0,0,0,166,167,1,0,0,0,167,169,1,0,0,0,168,166,1,0,0,0,169,170,
        3,54,27,0,170,5,1,0,0,0,171,172,5,21,0,0,172,173,5,3,0,0,173,184,
        5,31,0,0,174,180,5,2,0,0,175,176,3,8,4,0,176,177,5,2,0,0,177,179,
        1,0,0,0,178,175,1,0,0,0,179,182,1,0,0,0,180,178,1,0,0,0,180,181,
        1,0,0,0,181,183,1,0,0,0,182,180,1,0,0,0,183,185,3,8,4,0,184,174,
        1,0,0,0,184,185,1,0,0,0,185,186,1,0,0,0,186,196,5,4,0,0,187,188,
        5,21,0,0,188,191,5,3,0,0,189,192,3,64,32,0,190,192,3,74,37,0,191,
        189,1,0,0,0,191,190,1,0,0,0,192,193,1,0,0,0,193,194,5,4,0,0,194,
        196,1,0,0,0,195,171,1,0,0,0,195,187,1,0,0,0,196,7,1,0,0,0,197,201,
        3,64,32,0,198,201,3,74,37,0,199,201,5,31,0,0,200,197,1,0,0,0,200,
        198,1,0,0,0,200,199,1,0,0,0,201,9,1,0,0,0,202,203,5,23,0,0,203,204,
        5,3,0,0,204,205,5,31,0,0,205,214,5,2,0,0,206,208,5,49,0,0,207,206,
        1,0,0,0,207,208,1,0,0,0,208,209,1,0,0,0,209,210,3,64,32,0,210,211,
        5,2,0,0,211,213,1,0,0,0,212,207,1,0,0,0,213,216,1,0,0,0,214,212,
        1,0,0,0,214,215,1,0,0,0,215,218,1,0,0,0,216,214,1,0,0,0,217,219,
        5,49,0,0,218,217,1,0,0,0,218,219,1,0,0,0,219,220,1,0,0,0,220,221,
        3,64,32,0,221,222,5,4,0,0,222,11,1,0,0,0,223,228,3,14,7,0,224,225,
        5,2,0,0,225,227,3,14,7,0,226,224,1,0,0,0,227,230,1,0,0,0,228,226,
        1,0,0,0,228,229,1,0,0,0,229,13,1,0,0,0,230,228,1,0,0,0,231,233,5,
        11,0,0,232,231,1,0,0,0,232,233,1,0,0,0,233,234,1,0,0,0,234,236,5,
        25,0,0,235,237,5,49,0,0,236,235,1,0,0,0,236,237,1,0,0,0,237,241,
        1,0,0,0,238,240,5,34,0,0,239,238,1,0,0,0,240,243,1,0,0,0,241,239,
        1,0,0,0,241,242,1,0,0,0,242,244,1,0,0,0,243,241,1,0,0,0,244,247,
        5,27,0,0,245,246,5,48,0,0,246,248,3,66,33,0,247,245,1,0,0,0,247,
        248,1,0,0,0,248,268,1,0,0,0,249,251,5,11,0,0,250,249,1,0,0,0,250,
        251,1,0,0,0,251,252,1,0,0,0,252,256,5,25,0,0,253,255,5,34,0,0,254,
        253,1,0,0,0,255,258,1,0,0,0,256,254,1,0,0,0,256,257,1,0,0,0,257,
        260,1,0,0,0,258,256,1,0,0,0,259,261,5,49,0,0,260,259,1,0,0,0,260,
        261,1,0,0,0,261,262,1,0,0,0,262,265,5,27,0,0,263,264,5,48,0,0,264,
        266,3,66,33,0,265,263,1,0,0,0,265,266,1,0,0,0,266,268,1,0,0,0,267,
        232,1,0,0,0,267,250,1,0,0,0,268,15,1,0,0,0,269,271,5,11,0,0,270,
        269,1,0,0,0,270,271,1,0,0,0,271,274,1,0,0,0,272,275,5,25,0,0,273,
        275,5,26,0,0,274,272,1,0,0,0,274,273,1,0,0,0,275,279,1,0,0,0,276,
        278,5,34,0,0,277,276,1,0,0,0,278,281,1,0,0,0,279,277,1,0,0,0,279,
        280,1,0,0,0,280,282,1,0,0,0,281,279,1,0,0,0,282,283,5,27,0,0,283,
        285,5,3,0,0,284,286,3,12,6,0,285,284,1,0,0,0,285,286,1,0,0,0,286,
        287,1,0,0,0,287,288,5,4,0,0,288,289,3,26,13,0,289,17,1,0,0,0,290,
        292,5,11,0,0,291,290,1,0,0,0,291,292,1,0,0,0,292,295,1,0,0,0,293,
        296,5,25,0,0,294,296,5,26,0,0,295,293,1,0,0,0,295,294,1,0,0,0,296,
        300,1,0,0,0,297,299,5,34,0,0,298,297,1,0,0,0,299,302,1,0,0,0,300,
        298,1,0,0,0,300,301,1,0,0,0,301,303,1,0,0,0,302,300,1,0,0,0,303,
        304,5,27,0,0,304,306,5,3,0,0,305,307,3,12,6,0,306,305,1,0,0,0,306,
        307,1,0,0,0,307,308,1,0,0,0,308,309,5,4,0,0,309,19,1,0,0,0,310,313,
        3,22,11,0,311,312,5,2,0,0,312,314,3,22,11,0,313,311,1,0,0,0,314,
        315,1,0,0,0,315,316,1,0,0,0,315,313,1,0,0,0,316,21,1,0,0,0,317,322,
        3,64,32,0,318,322,3,60,30,0,319,322,3,24,12,0,320,322,3,74,37,0,
        321,317,1,0,0,0,321,318,1,0,0,0,321,319,1,0,0,0,321,320,1,0,0,0,
        322,23,1,0,0,0,323,324,5,27,0,0,324,326,5,3,0,0,325,327,3,20,10,
        0,326,325,1,0,0,0,326,327,1,0,0,0,327,328,1,0,0,0,328,329,5,4,0,
        0,329,25,1,0,0,0,330,383,5,5,0,0,331,338,3,6,3,0,332,334,5,1,0,0,
        333,332,1,0,0,0,334,335,1,0,0,0,335,333,1,0,0,0,335,336,1,0,0,0,
        336,339,1,0,0,0,337,339,5,57,0,0,338,333,1,0,0,0,338,337,1,0,0,0,
        339,382,1,0,0,0,340,382,3,28,14,0,341,349,3,40,20,0,342,344,5,1,
        0,0,343,342,1,0,0,0,344,347,1,0,0,0,345,343,1,0,0,0,345,346,1,0,
        0,0,346,350,1,0,0,0,347,345,1,0,0,0,348,350,5,57,0,0,349,345,1,0,
        0,0,349,348,1,0,0,0,350,382,1,0,0,0,351,359,3,44,22,0,352,354,5,
        1,0,0,353,352,1,0,0,0,354,357,1,0,0,0,355,353,1,0,0,0,355,356,1,
        0,0,0,356,360,1,0,0,0,357,355,1,0,0,0,358,360,5,57,0,0,359,355,1,
        0,0,0,359,358,1,0,0,0,360,382,1,0,0,0,361,369,3,46,23,0,362,364,
        5,1,0,0,363,362,1,0,0,0,364,367,1,0,0,0,365,363,1,0,0,0,365,366,
        1,0,0,0,366,370,1,0,0,0,367,365,1,0,0,0,368,370,5,57,0,0,369,365,
        1,0,0,0,369,368,1,0,0,0,370,382,1,0,0,0,371,378,3,56,28,0,372,374,
        5,1,0,0,373,372,1,0,0,0,374,375,1,0,0,0,375,373,1,0,0,0,375,376,
        1,0,0,0,376,379,1,0,0,0,377,379,5,57,0,0,378,373,1,0,0,0,378,377,
        1,0,0,0,379,382,1,0,0,0,380,382,3,2,1,0,381,331,1,0,0,0,381,340,
        1,0,0,0,381,341,1,0,0,0,381,351,1,0,0,0,381,361,1,0,0,0,381,371,
        1,0,0,0,381,380,1,0,0,0,382,385,1,0,0,0,383,381,1,0,0,0,383,384,
        1,0,0,0,384,386,1,0,0,0,385,383,1,0,0,0,386,387,5,6,0,0,387,27,1,
        0,0,0,388,389,5,22,0,0,389,390,3,66,33,0,390,395,5,1,0,0,391,394,
        3,2,1,0,392,394,3,28,14,0,393,391,1,0,0,0,393,392,1,0,0,0,394,397,
        1,0,0,0,395,393,1,0,0,0,395,396,1,0,0,0,396,29,1,0,0,0,397,395,1,
        0,0,0,398,453,5,5,0,0,399,406,3,6,3,0,400,402,5,1,0,0,401,400,1,
        0,0,0,402,403,1,0,0,0,403,401,1,0,0,0,403,404,1,0,0,0,404,407,1,
        0,0,0,405,407,5,57,0,0,406,401,1,0,0,0,406,405,1,0,0,0,407,452,1,
        0,0,0,408,452,3,28,14,0,409,417,3,40,20,0,410,412,5,1,0,0,411,410,
        1,0,0,0,412,415,1,0,0,0,413,411,1,0,0,0,413,414,1,0,0,0,414,418,
        1,0,0,0,415,413,1,0,0,0,416,418,5,57,0,0,417,413,1,0,0,0,417,416,
        1,0,0,0,418,452,1,0,0,0,419,427,3,44,22,0,420,422,5,1,0,0,421,420,
        1,0,0,0,422,425,1,0,0,0,423,421,1,0,0,0,423,424,1,0,0,0,424,428,
        1,0,0,0,425,423,1,0,0,0,426,428,5,57,0,0,427,423,1,0,0,0,427,426,
        1,0,0,0,428,452,1,0,0,0,429,437,3,46,23,0,430,432,5,1,0,0,431,430,
        1,0,0,0,432,435,1,0,0,0,433,431,1,0,0,0,433,434,1,0,0,0,434,438,
        1,0,0,0,435,433,1,0,0,0,436,438,5,57,0,0,437,433,1,0,0,0,437,436,
        1,0,0,0,438,452,1,0,0,0,439,446,3,56,28,0,440,442,5,1,0,0,441,440,
        1,0,0,0,442,443,1,0,0,0,443,441,1,0,0,0,443,444,1,0,0,0,444,447,
        1,0,0,0,445,447,5,57,0,0,446,441,1,0,0,0,446,445,1,0,0,0,447,452,
        1,0,0,0,448,452,3,34,17,0,449,452,3,32,16,0,450,452,3,2,1,0,451,
        399,1,0,0,0,451,408,1,0,0,0,451,409,1,0,0,0,451,419,1,0,0,0,451,
        429,1,0,0,0,451,439,1,0,0,0,451,448,1,0,0,0,451,449,1,0,0,0,451,
        450,1,0,0,0,452,455,1,0,0,0,453,451,1,0,0,0,453,454,1,0,0,0,454,
        456,1,0,0,0,455,453,1,0,0,0,456,457,5,6,0,0,457,31,1,0,0,0,458,459,
        5,17,0,0,459,463,7,0,0,0,460,462,3,2,1,0,461,460,1,0,0,0,462,465,
        1,0,0,0,463,461,1,0,0,0,463,464,1,0,0,0,464,33,1,0,0,0,465,463,1,
        0,0,0,466,467,5,16,0,0,467,471,7,0,0,0,468,470,3,2,1,0,469,468,1,
        0,0,0,470,473,1,0,0,0,471,469,1,0,0,0,471,472,1,0,0,0,472,35,1,0,
        0,0,473,471,1,0,0,0,474,476,5,11,0,0,475,474,1,0,0,0,475,476,1,0,
        0,0,476,477,1,0,0,0,477,478,5,25,0,0,478,479,5,27,0,0,479,481,5,
        7,0,0,480,482,5,28,0,0,481,480,1,0,0,0,481,482,1,0,0,0,482,483,1,
        0,0,0,483,484,5,8,0,0,484,485,5,48,0,0,485,491,5,5,0,0,486,487,3,
        74,37,0,487,488,5,2,0,0,488,490,1,0,0,0,489,486,1,0,0,0,490,493,
        1,0,0,0,491,489,1,0,0,0,491,492,1,0,0,0,492,494,1,0,0,0,493,491,
        1,0,0,0,494,495,3,74,37,0,495,496,5,6,0,0,496,506,1,0,0,0,497,499,
        5,11,0,0,498,497,1,0,0,0,498,499,1,0,0,0,499,500,1,0,0,0,500,501,
        5,25,0,0,501,502,5,27,0,0,502,503,5,7,0,0,503,504,5,28,0,0,504,506,
        5,8,0,0,505,475,1,0,0,0,505,498,1,0,0,0,506,37,1,0,0,0,507,508,5,
        24,0,0,508,509,5,39,0,0,509,510,5,27,0,0,510,511,5,9,0,0,511,512,
        5,41,0,0,512,39,1,0,0,0,513,514,5,12,0,0,514,515,5,3,0,0,515,516,
        3,50,25,0,516,517,5,4,0,0,517,519,3,30,15,0,518,520,3,42,21,0,519,
        518,1,0,0,0,519,520,1,0,0,0,520,41,1,0,0,0,521,522,5,13,0,0,522,
        523,3,30,15,0,523,43,1,0,0,0,524,525,5,15,0,0,525,526,5,3,0,0,526,
        527,3,50,25,0,527,528,5,4,0,0,528,529,3,30,15,0,529,45,1,0,0,0,530,
        531,5,14,0,0,531,532,5,3,0,0,532,533,3,48,24,0,533,534,5,1,0,0,534,
        535,3,50,25,0,535,536,5,1,0,0,536,537,3,52,26,0,537,538,5,4,0,0,
        538,539,3,30,15,0,539,47,1,0,0,0,540,541,5,25,0,0,541,542,3,62,31,
        0,542,543,5,48,0,0,543,544,3,66,33,0,544,547,1,0,0,0,545,547,3,56,
        28,0,546,540,1,0,0,0,546,545,1,0,0,0,547,49,1,0,0,0,548,549,3,68,
        34,0,549,550,7,1,0,0,550,551,3,70,35,0,551,562,1,0,0,0,552,553,3,
        68,34,0,553,554,7,2,0,0,554,555,3,70,35,0,555,562,1,0,0,0,556,557,
        3,66,33,0,557,558,7,3,0,0,558,559,3,68,34,0,559,562,1,0,0,0,560,
        562,3,66,33,0,561,548,1,0,0,0,561,552,1,0,0,0,561,556,1,0,0,0,561,
        560,1,0,0,0,562,51,1,0,0,0,563,564,5,50,0,0,564,574,3,64,32,0,565,
        566,5,51,0,0,566,574,3,64,32,0,567,568,3,64,32,0,568,569,5,50,0,
        0,569,574,1,0,0,0,570,571,3,64,32,0,571,572,5,51,0,0,572,574,1,0,
        0,0,573,563,1,0,0,0,573,565,1,0,0,0,573,567,1,0,0,0,573,570,1,0,
        0,0,574,53,1,0,0,0,575,576,3,62,31,0,576,577,5,48,0,0,577,578,3,
        66,33,0,578,581,1,0,0,0,579,581,3,62,31,0,580,575,1,0,0,0,580,579,
        1,0,0,0,581,55,1,0,0,0,582,583,3,64,32,0,583,584,5,48,0,0,584,585,
        3,66,33,0,585,595,1,0,0,0,586,587,3,60,30,0,587,588,5,48,0,0,588,
        589,3,66,33,0,589,595,1,0,0,0,590,591,3,58,29,0,591,592,5,48,0,0,
        592,593,3,66,33,0,593,595,1,0,0,0,594,582,1,0,0,0,594,586,1,0,0,
        0,594,590,1,0,0,0,595,57,1,0,0,0,596,597,3,62,31,0,597,598,5,7,0,
        0,598,599,5,28,0,0,599,600,5,8,0,0,600,59,1,0,0,0,601,602,5,34,0,
        0,602,606,3,60,30,0,603,604,5,34,0,0,604,606,3,64,32,0,605,601,1,
        0,0,0,605,603,1,0,0,0,606,61,1,0,0,0,607,609,5,34,0,0,608,607,1,
        0,0,0,609,612,1,0,0,0,610,608,1,0,0,0,610,611,1,0,0,0,611,613,1,
        0,0,0,612,610,1,0,0,0,613,614,5,27,0,0,614,63,1,0,0,0,615,616,5,
        27,0,0,616,65,1,0,0,0,617,618,6,33,-1,0,618,619,3,68,34,0,619,631,
        1,0,0,0,620,621,10,3,0,0,621,622,5,37,0,0,622,630,3,68,34,0,623,
        624,10,2,0,0,624,625,5,38,0,0,625,630,3,68,34,0,626,627,10,1,0,0,
        627,628,7,3,0,0,628,630,3,68,34,0,629,620,1,0,0,0,629,623,1,0,0,
        0,629,626,1,0,0,0,630,633,1,0,0,0,631,629,1,0,0,0,631,632,1,0,0,
        0,632,67,1,0,0,0,633,631,1,0,0,0,634,635,6,34,-1,0,635,639,3,70,
        35,0,636,637,5,47,0,0,637,639,3,70,35,0,638,634,1,0,0,0,638,636,
        1,0,0,0,639,653,1,0,0,0,640,641,10,5,0,0,641,642,7,4,0,0,642,652,
        3,70,35,0,643,644,10,4,0,0,644,645,7,2,0,0,645,652,3,70,35,0,646,
        647,10,3,0,0,647,648,7,1,0,0,648,652,3,70,35,0,649,650,10,1,0,0,
        650,652,7,5,0,0,651,640,1,0,0,0,651,643,1,0,0,0,651,646,1,0,0,0,
        651,649,1,0,0,0,652,655,1,0,0,0,653,651,1,0,0,0,653,654,1,0,0,0,
        654,69,1,0,0,0,655,653,1,0,0,0,656,664,3,72,36,0,657,658,5,38,0,
        0,658,664,3,70,35,0,659,660,5,37,0,0,660,664,3,70,35,0,661,662,7,
        5,0,0,662,664,3,70,35,0,663,656,1,0,0,0,663,657,1,0,0,0,663,659,
        1,0,0,0,663,661,1,0,0,0,664,71,1,0,0,0,665,678,3,64,32,0,666,678,
        3,74,37,0,667,668,5,49,0,0,668,678,3,64,32,0,669,678,3,60,30,0,670,
        671,5,3,0,0,671,672,3,66,33,0,672,673,5,4,0,0,673,678,1,0,0,0,674,
        675,5,10,0,0,675,678,3,72,36,0,676,678,3,24,12,0,677,665,1,0,0,0,
        677,666,1,0,0,0,677,667,1,0,0,0,677,669,1,0,0,0,677,670,1,0,0,0,
        677,674,1,0,0,0,677,676,1,0,0,0,678,73,1,0,0,0,679,680,7,6,0,0,680,
        75,1,0,0,0,97,79,87,91,97,100,102,104,113,116,122,125,131,134,140,
        143,149,152,155,158,166,180,184,191,195,200,207,214,218,228,232,
        236,241,247,250,256,260,265,267,270,274,279,285,291,295,300,306,
        315,321,326,335,338,345,349,355,359,365,369,375,378,381,383,393,
        395,403,406,413,417,423,427,433,437,443,446,451,453,463,471,475,
        481,491,498,505,519,546,561,573,580,594,605,610,629,631,638,651,
        653,663,677
    ]

class MathParser ( Parser ):

    grammarFileName = "Math.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "','", "'('", "')'", "'{'", "'}'", 
                     "'['", "']'", "'.h'", "<INVALID>", "'const'", "'if'", 
                     "'else'", "'for'", "'while'", "'break'", "'continue'", 
                     "'switch'", "'case'", "'default'", "'printf'", "'return'", 
                     "'scanf'", "'#include'", "<INVALID>", "'void'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'*'", "'/'", "'%'", "'+'", 
                     "'-'", "'<'", "'<='", "'>'", "'>='", "'=='", "'!='", 
                     "'||'", "'&&'", "'!'", "'='", "'&'", "'++'", "'--'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "CAST", "CONST", "IF", "ELSE", 
                      "FOR", "WHILE", "BREAK", "CONTINUE", "SWITCH", "CASE", 
                      "DEFAULT", "PRINTF", "RETURN", "SCANF", "INCLUDE", 
                      "TYPE", "VOID", "VAR_NAME", "INT", "FLOAT", "CHAR", 
                      "FORMAT_STRING", "STRING", "ARG_TYPES", "STR", "DIV", 
                      "MOD", "SUM", "DIF", "LT", "LEQ", "GT", "GEQ", "EQ", 
                      "NEQ", "OR_OP", "AND_OP", "NOT_OP", "ASSIGN", "ADDR", 
                      "INCR", "DECR", "SP", "NEWLINE", "WS", "UNICODE_WS", 
                      "LN", "DELIM", "COMMENT", "LCOMMENT" ]

    RULE_math = 0
    RULE_instr = 1
    RULE_declr = 2
    RULE_printf = 3
    RULE_printf_arg = 4
    RULE_scanf = 5
    RULE_param_list = 6
    RULE_param_declr = 7
    RULE_func_defn = 8
    RULE_func_decl = 9
    RULE_arg_list = 10
    RULE_func_arg = 11
    RULE_func_call = 12
    RULE_func_scope = 13
    RULE_return_instr = 14
    RULE_scope = 15
    RULE_cont_instr = 16
    RULE_break_instr = 17
    RULE_array_decl = 18
    RULE_incl_stat = 19
    RULE_if_cond = 20
    RULE_else_cond = 21
    RULE_while_loop = 22
    RULE_for_loop = 23
    RULE_init = 24
    RULE_cond = 25
    RULE_incr = 26
    RULE_var_decl = 27
    RULE_assign = 28
    RULE_array_el = 29
    RULE_deref = 30
    RULE_lvar = 31
    RULE_rvar = 32
    RULE_expr = 33
    RULE_term = 34
    RULE_factor = 35
    RULE_primary = 36
    RULE_rtype = 37

    ruleNames =  [ "math", "instr", "declr", "printf", "printf_arg", "scanf", 
                   "param_list", "param_declr", "func_defn", "func_decl", 
                   "arg_list", "func_arg", "func_call", "func_scope", "return_instr", 
                   "scope", "cont_instr", "break_instr", "array_decl", "incl_stat", 
                   "if_cond", "else_cond", "while_loop", "for_loop", "init", 
                   "cond", "incr", "var_decl", "assign", "array_el", "deref", 
                   "lvar", "rvar", "expr", "term", "factor", "primary", 
                   "rtype" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    CAST=10
    CONST=11
    IF=12
    ELSE=13
    FOR=14
    WHILE=15
    BREAK=16
    CONTINUE=17
    SWITCH=18
    CASE=19
    DEFAULT=20
    PRINTF=21
    RETURN=22
    SCANF=23
    INCLUDE=24
    TYPE=25
    VOID=26
    VAR_NAME=27
    INT=28
    FLOAT=29
    CHAR=30
    FORMAT_STRING=31
    STRING=32
    ARG_TYPES=33
    STR=34
    DIV=35
    MOD=36
    SUM=37
    DIF=38
    LT=39
    LEQ=40
    GT=41
    GEQ=42
    EQ=43
    NEQ=44
    OR_OP=45
    AND_OP=46
    NOT_OP=47
    ASSIGN=48
    ADDR=49
    INCR=50
    DECR=51
    SP=52
    NEWLINE=53
    WS=54
    UNICODE_WS=55
    LN=56
    DELIM=57
    COMMENT=58
    LCOMMENT=59

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class MathContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MathParser.EOF, 0)

        def incl_stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathParser.Incl_statContext)
            else:
                return self.getTypedRuleContext(MathParser.Incl_statContext,i)


        def instr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathParser.InstrContext)
            else:
                return self.getTypedRuleContext(MathParser.InstrContext,i)


        def func_defn(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathParser.Func_defnContext)
            else:
                return self.getTypedRuleContext(MathParser.Func_defnContext,i)


        def func_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathParser.Func_declContext)
            else:
                return self.getTypedRuleContext(MathParser.Func_declContext,i)


        def DELIM(self, i:int=None):
            if i is None:
                return self.getTokens(MathParser.DELIM)
            else:
                return self.getToken(MathParser.DELIM, i)

        def getRuleIndex(self):
            return MathParser.RULE_math

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMath" ):
                listener.enterMath(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMath" ):
                listener.exitMath(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMath" ):
                return visitor.visitMath(self)
            else:
                return visitor.visitChildren(self)




    def math(self):

        localctx = MathParser.MathContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_math)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==24:
                self.state = 76
                self.incl_stat()
                self.state = 81
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 104
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 4081818781355048) != 0:
                self.state = 102
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                if la_ == 1:
                    self.state = 82
                    self.instr()
                    pass

                elif la_ == 2:
                    self.state = 83
                    self.func_defn()
                    self.state = 91
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [-1, 1, 3, 5, 10, 11, 23, 25, 26, 27, 28, 29, 30, 34, 37, 38, 47, 49, 50, 51]:
                        self.state = 87
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==1:
                            self.state = 84
                            self.match(MathParser.T__0)
                            self.state = 89
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        pass
                    elif token in [57]:
                        self.state = 90
                        self.match(MathParser.DELIM)
                        pass
                    else:
                        raise NoViableAltException(self)

                    pass

                elif la_ == 3:
                    self.state = 93
                    self.func_decl()
                    self.state = 100
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [1]:
                        self.state = 95 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while True:
                            self.state = 94
                            self.match(MathParser.T__0)
                            self.state = 97 
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            if not (_la==1):
                                break

                        pass
                    elif token in [57]:
                        self.state = 99
                        self.match(MathParser.DELIM)
                        pass
                    else:
                        raise NoViableAltException(self)

                    pass


                self.state = 106
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 107
            self.match(MathParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declr(self):
            return self.getTypedRuleContext(MathParser.DeclrContext,0)


        def DELIM(self):
            return self.getToken(MathParser.DELIM, 0)

        def array_decl(self):
            return self.getTypedRuleContext(MathParser.Array_declContext,0)


        def expr(self):
            return self.getTypedRuleContext(MathParser.ExprContext,0)


        def scanf(self):
            return self.getTypedRuleContext(MathParser.ScanfContext,0)


        def assign(self):
            return self.getTypedRuleContext(MathParser.AssignContext,0)


        def scope(self):
            return self.getTypedRuleContext(MathParser.ScopeContext,0)


        def getRuleIndex(self):
            return MathParser.RULE_instr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstr" ):
                listener.enterInstr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstr" ):
                listener.exitInstr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstr" ):
                return visitor.visitInstr(self)
            else:
                return visitor.visitChildren(self)




    def instr(self):

        localctx = MathParser.InstrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_instr)
        self._la = 0 # Token type
        try:
            self.state = 155
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 109
                self.declr()
                self.state = 116
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1]:
                    self.state = 111 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 110
                        self.match(MathParser.T__0)
                        self.state = 113 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not (_la==1):
                            break

                    pass
                elif token in [57]:
                    self.state = 115
                    self.match(MathParser.DELIM)
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 118
                self.array_decl()
                self.state = 125
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1]:
                    self.state = 120 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 119
                        self.match(MathParser.T__0)
                        self.state = 122 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not (_la==1):
                            break

                    pass
                elif token in [57]:
                    self.state = 124
                    self.match(MathParser.DELIM)
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 127
                self.expr(0)
                self.state = 134
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1]:
                    self.state = 129 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 128
                        self.match(MathParser.T__0)
                        self.state = 131 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not (_la==1):
                            break

                    pass
                elif token in [57]:
                    self.state = 133
                    self.match(MathParser.DELIM)
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 136
                self.scanf()
                self.state = 143
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1]:
                    self.state = 138 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 137
                        self.match(MathParser.T__0)
                        self.state = 140 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not (_la==1):
                            break

                    pass
                elif token in [57]:
                    self.state = 142
                    self.match(MathParser.DELIM)
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 145
                self.assign()
                self.state = 152
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1]:
                    self.state = 147 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 146
                        self.match(MathParser.T__0)
                        self.state = 149 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not (_la==1):
                            break

                    pass
                elif token in [57]:
                    self.state = 151
                    self.match(MathParser.DELIM)
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 154
                self.scope()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MathParser.TYPE, 0)

        def var_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathParser.Var_declContext)
            else:
                return self.getTypedRuleContext(MathParser.Var_declContext,i)


        def CONST(self):
            return self.getToken(MathParser.CONST, 0)

        def getRuleIndex(self):
            return MathParser.RULE_declr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclr" ):
                listener.enterDeclr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclr" ):
                listener.exitDeclr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclr" ):
                return visitor.visitDeclr(self)
            else:
                return visitor.visitChildren(self)




    def declr(self):

        localctx = MathParser.DeclrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 157
                self.match(MathParser.CONST)


            self.state = 160
            self.match(MathParser.TYPE)
            self.state = 166
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 161
                    self.var_decl()
                    self.state = 162
                    self.match(MathParser.T__1) 
                self.state = 168
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

            self.state = 169
            self.var_decl()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintfContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.format_string = None # Token
            self._printf_arg = None # Printf_argContext
            self.vars_ = list() # of Printf_argContexts

        def PRINTF(self):
            return self.getToken(MathParser.PRINTF, 0)

        def FORMAT_STRING(self):
            return self.getToken(MathParser.FORMAT_STRING, 0)

        def printf_arg(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathParser.Printf_argContext)
            else:
                return self.getTypedRuleContext(MathParser.Printf_argContext,i)


        def rvar(self):
            return self.getTypedRuleContext(MathParser.RvarContext,0)


        def rtype(self):
            return self.getTypedRuleContext(MathParser.RtypeContext,0)


        def getRuleIndex(self):
            return MathParser.RULE_printf

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintf" ):
                listener.enterPrintf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintf" ):
                listener.exitPrintf(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintf" ):
                return visitor.visitPrintf(self)
            else:
                return visitor.visitChildren(self)




    def printf(self):

        localctx = MathParser.PrintfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_printf)
        self._la = 0 # Token type
        try:
            self.state = 195
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 171
                self.match(MathParser.PRINTF)
                self.state = 172
                self.match(MathParser.T__2)
                self.state = 173
                localctx.format_string = self.match(MathParser.FORMAT_STRING)
                self.state = 184
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==2:
                    self.state = 174
                    self.match(MathParser.T__1)
                    self.state = 180
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt==1:
                            self.state = 175
                            localctx._printf_arg = self.printf_arg()
                            localctx.vars_.append(localctx._printf_arg)
                            self.state = 176
                            self.match(MathParser.T__1) 
                        self.state = 182
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

                    self.state = 183
                    localctx._printf_arg = self.printf_arg()
                    localctx.vars_.append(localctx._printf_arg)


                self.state = 186
                self.match(MathParser.T__3)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 187
                self.match(MathParser.PRINTF)
                self.state = 188
                self.match(MathParser.T__2)
                self.state = 191
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [27]:
                    self.state = 189
                    self.rvar()
                    pass
                elif token in [28, 29, 30]:
                    self.state = 190
                    self.rtype()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 193
                self.match(MathParser.T__3)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Printf_argContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def rvar(self):
            return self.getTypedRuleContext(MathParser.RvarContext,0)


        def rtype(self):
            return self.getTypedRuleContext(MathParser.RtypeContext,0)


        def FORMAT_STRING(self):
            return self.getToken(MathParser.FORMAT_STRING, 0)

        def getRuleIndex(self):
            return MathParser.RULE_printf_arg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintf_arg" ):
                listener.enterPrintf_arg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintf_arg" ):
                listener.exitPrintf_arg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintf_arg" ):
                return visitor.visitPrintf_arg(self)
            else:
                return visitor.visitChildren(self)




    def printf_arg(self):

        localctx = MathParser.Printf_argContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_printf_arg)
        try:
            self.state = 200
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [27]:
                self.enterOuterAlt(localctx, 1)
                self.state = 197
                self.rvar()
                pass
            elif token in [28, 29, 30]:
                self.enterOuterAlt(localctx, 2)
                self.state = 198
                self.rtype()
                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 3)
                self.state = 199
                self.match(MathParser.FORMAT_STRING)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ScanfContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.format_string = None # Token
            self._rvar = None # RvarContext
            self.vars_ = list() # of RvarContexts

        def SCANF(self):
            return self.getToken(MathParser.SCANF, 0)

        def FORMAT_STRING(self):
            return self.getToken(MathParser.FORMAT_STRING, 0)

        def rvar(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathParser.RvarContext)
            else:
                return self.getTypedRuleContext(MathParser.RvarContext,i)


        def ADDR(self, i:int=None):
            if i is None:
                return self.getTokens(MathParser.ADDR)
            else:
                return self.getToken(MathParser.ADDR, i)

        def getRuleIndex(self):
            return MathParser.RULE_scanf

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScanf" ):
                listener.enterScanf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScanf" ):
                listener.exitScanf(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScanf" ):
                return visitor.visitScanf(self)
            else:
                return visitor.visitChildren(self)




    def scanf(self):

        localctx = MathParser.ScanfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_scanf)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            self.match(MathParser.SCANF)
            self.state = 203
            self.match(MathParser.T__2)
            self.state = 204
            localctx.format_string = self.match(MathParser.FORMAT_STRING)
            self.state = 205
            self.match(MathParser.T__1)
            self.state = 214
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 207
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==49:
                        self.state = 206
                        self.match(MathParser.ADDR)


                    self.state = 209
                    localctx._rvar = self.rvar()
                    localctx.vars_.append(localctx._rvar)
                    self.state = 210
                    self.match(MathParser.T__1) 
                self.state = 216
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

            self.state = 218
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==49:
                self.state = 217
                self.match(MathParser.ADDR)


            self.state = 220
            localctx._rvar = self.rvar()
            localctx.vars_.append(localctx._rvar)
            self.state = 221
            self.match(MathParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._param_declr = None # Param_declrContext
            self.params = list() # of Param_declrContexts

        def param_declr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathParser.Param_declrContext)
            else:
                return self.getTypedRuleContext(MathParser.Param_declrContext,i)


        def getRuleIndex(self):
            return MathParser.RULE_param_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParam_list" ):
                listener.enterParam_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParam_list" ):
                listener.exitParam_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_list" ):
                return visitor.visitParam_list(self)
            else:
                return visitor.visitChildren(self)




    def param_list(self):

        localctx = MathParser.Param_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_param_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
            localctx._param_declr = self.param_declr()
            localctx.params.append(localctx._param_declr)
            self.state = 228
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 224
                self.match(MathParser.T__1)
                self.state = 225
                localctx._param_declr = self.param_declr()
                localctx.params.append(localctx._param_declr)
                self.state = 230
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_declrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.const = None # Token
            self.type_ = None # Token
            self.reference = None # Token
            self._STR = None # Token
            self.ptr = list() # of Tokens
            self.var = None # Token
            self.default = None # ExprContext

        def TYPE(self):
            return self.getToken(MathParser.TYPE, 0)

        def VAR_NAME(self):
            return self.getToken(MathParser.VAR_NAME, 0)

        def ASSIGN(self):
            return self.getToken(MathParser.ASSIGN, 0)

        def CONST(self):
            return self.getToken(MathParser.CONST, 0)

        def ADDR(self):
            return self.getToken(MathParser.ADDR, 0)

        def STR(self, i:int=None):
            if i is None:
                return self.getTokens(MathParser.STR)
            else:
                return self.getToken(MathParser.STR, i)

        def expr(self):
            return self.getTypedRuleContext(MathParser.ExprContext,0)


        def getRuleIndex(self):
            return MathParser.RULE_param_declr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParam_declr" ):
                listener.enterParam_declr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParam_declr" ):
                listener.exitParam_declr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_declr" ):
                return visitor.visitParam_declr(self)
            else:
                return visitor.visitChildren(self)




    def param_declr(self):

        localctx = MathParser.Param_declrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_param_declr)
        self._la = 0 # Token type
        try:
            self.state = 267
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 232
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==11:
                    self.state = 231
                    localctx.const = self.match(MathParser.CONST)


                self.state = 234
                localctx.type_ = self.match(MathParser.TYPE)
                self.state = 236
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==49:
                    self.state = 235
                    localctx.reference = self.match(MathParser.ADDR)


                self.state = 241
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==34:
                    self.state = 238
                    localctx._STR = self.match(MathParser.STR)
                    localctx.ptr.append(localctx._STR)
                    self.state = 243
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 244
                localctx.var = self.match(MathParser.VAR_NAME)
                self.state = 247
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==48:
                    self.state = 245
                    self.match(MathParser.ASSIGN)
                    self.state = 246
                    localctx.default = self.expr(0)


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 250
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==11:
                    self.state = 249
                    localctx.const = self.match(MathParser.CONST)


                self.state = 252
                localctx.type_ = self.match(MathParser.TYPE)
                self.state = 256
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==34:
                    self.state = 253
                    localctx._STR = self.match(MathParser.STR)
                    localctx.ptr.append(localctx._STR)
                    self.state = 258
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 260
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==49:
                    self.state = 259
                    localctx.reference = self.match(MathParser.ADDR)


                self.state = 262
                localctx.var = self.match(MathParser.VAR_NAME)
                self.state = 265
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==48:
                    self.state = 263
                    self.match(MathParser.ASSIGN)
                    self.state = 264
                    localctx.default = self.expr(0)


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_defnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.const = None # Token
            self.type_ = None # Token
            self._STR = None # Token
            self.ptr = list() # of Tokens
            self.name = None # Token
            self.params = None # Param_listContext

        def func_scope(self):
            return self.getTypedRuleContext(MathParser.Func_scopeContext,0)


        def VAR_NAME(self):
            return self.getToken(MathParser.VAR_NAME, 0)

        def TYPE(self):
            return self.getToken(MathParser.TYPE, 0)

        def VOID(self):
            return self.getToken(MathParser.VOID, 0)

        def CONST(self):
            return self.getToken(MathParser.CONST, 0)

        def STR(self, i:int=None):
            if i is None:
                return self.getTokens(MathParser.STR)
            else:
                return self.getToken(MathParser.STR, i)

        def param_list(self):
            return self.getTypedRuleContext(MathParser.Param_listContext,0)


        def getRuleIndex(self):
            return MathParser.RULE_func_defn

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc_defn" ):
                listener.enterFunc_defn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc_defn" ):
                listener.exitFunc_defn(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_defn" ):
                return visitor.visitFunc_defn(self)
            else:
                return visitor.visitChildren(self)




    def func_defn(self):

        localctx = MathParser.Func_defnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_func_defn)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 270
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 269
                localctx.const = self.match(MathParser.CONST)


            self.state = 274
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [25]:
                self.state = 272
                localctx.type_ = self.match(MathParser.TYPE)
                pass
            elif token in [26]:
                self.state = 273
                localctx.type_ = self.match(MathParser.VOID)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 279
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==34:
                self.state = 276
                localctx._STR = self.match(MathParser.STR)
                localctx.ptr.append(localctx._STR)
                self.state = 281
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 282
            localctx.name = self.match(MathParser.VAR_NAME)
            self.state = 283
            self.match(MathParser.T__2)
            self.state = 285
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11 or _la==25:
                self.state = 284
                localctx.params = self.param_list()


            self.state = 287
            self.match(MathParser.T__3)
            self.state = 288
            self.func_scope()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.const = None # Token
            self.type_ = None # Token
            self._STR = None # Token
            self.ptr = list() # of Tokens
            self.name = None # Token
            self.params = None # Param_listContext

        def VAR_NAME(self):
            return self.getToken(MathParser.VAR_NAME, 0)

        def TYPE(self):
            return self.getToken(MathParser.TYPE, 0)

        def VOID(self):
            return self.getToken(MathParser.VOID, 0)

        def CONST(self):
            return self.getToken(MathParser.CONST, 0)

        def STR(self, i:int=None):
            if i is None:
                return self.getTokens(MathParser.STR)
            else:
                return self.getToken(MathParser.STR, i)

        def param_list(self):
            return self.getTypedRuleContext(MathParser.Param_listContext,0)


        def getRuleIndex(self):
            return MathParser.RULE_func_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc_decl" ):
                listener.enterFunc_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc_decl" ):
                listener.exitFunc_decl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_decl" ):
                return visitor.visitFunc_decl(self)
            else:
                return visitor.visitChildren(self)




    def func_decl(self):

        localctx = MathParser.Func_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_func_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 291
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 290
                localctx.const = self.match(MathParser.CONST)


            self.state = 295
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [25]:
                self.state = 293
                localctx.type_ = self.match(MathParser.TYPE)
                pass
            elif token in [26]:
                self.state = 294
                localctx.type_ = self.match(MathParser.VOID)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 300
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==34:
                self.state = 297
                localctx._STR = self.match(MathParser.STR)
                localctx.ptr.append(localctx._STR)
                self.state = 302
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 303
            localctx.name = self.match(MathParser.VAR_NAME)
            self.state = 304
            self.match(MathParser.T__2)
            self.state = 306
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11 or _la==25:
                self.state = 305
                localctx.params = self.param_list()


            self.state = 308
            self.match(MathParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arg_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._func_arg = None # Func_argContext
            self.args = list() # of Func_argContexts

        def func_arg(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathParser.Func_argContext)
            else:
                return self.getTypedRuleContext(MathParser.Func_argContext,i)


        def getRuleIndex(self):
            return MathParser.RULE_arg_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArg_list" ):
                listener.enterArg_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArg_list" ):
                listener.exitArg_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArg_list" ):
                return visitor.visitArg_list(self)
            else:
                return visitor.visitChildren(self)




    def arg_list(self):

        localctx = MathParser.Arg_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_arg_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 310
            localctx._func_arg = self.func_arg()
            localctx.args.append(localctx._func_arg)
            self.state = 313 
            self._errHandler.sync(self)
            _alt = 1+1
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1+1:
                    self.state = 311
                    self.match(MathParser.T__1)
                    self.state = 312
                    localctx._func_arg = self.func_arg()
                    localctx.args.append(localctx._func_arg)

                else:
                    raise NoViableAltException(self)
                self.state = 315 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,46,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_argContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def rvar(self):
            return self.getTypedRuleContext(MathParser.RvarContext,0)


        def deref(self):
            return self.getTypedRuleContext(MathParser.DerefContext,0)


        def func_call(self):
            return self.getTypedRuleContext(MathParser.Func_callContext,0)


        def rtype(self):
            return self.getTypedRuleContext(MathParser.RtypeContext,0)


        def getRuleIndex(self):
            return MathParser.RULE_func_arg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc_arg" ):
                listener.enterFunc_arg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc_arg" ):
                listener.exitFunc_arg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_arg" ):
                return visitor.visitFunc_arg(self)
            else:
                return visitor.visitChildren(self)




    def func_arg(self):

        localctx = MathParser.Func_argContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_func_arg)
        try:
            self.state = 321
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 317
                self.rvar()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 318
                self.deref()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 319
                self.func_call()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 320
                self.rtype()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Token
            self.args = None # Arg_listContext

        def VAR_NAME(self):
            return self.getToken(MathParser.VAR_NAME, 0)

        def arg_list(self):
            return self.getTypedRuleContext(MathParser.Arg_listContext,0)


        def getRuleIndex(self):
            return MathParser.RULE_func_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc_call" ):
                listener.enterFunc_call(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc_call" ):
                listener.exitFunc_call(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_call" ):
                return visitor.visitFunc_call(self)
            else:
                return visitor.visitChildren(self)




    def func_call(self):

        localctx = MathParser.Func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_func_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 323
            localctx.name = self.match(MathParser.VAR_NAME)
            self.state = 324
            self.match(MathParser.T__2)
            self.state = 326
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 19193135104) != 0:
                self.state = 325
                localctx.args = self.arg_list()


            self.state = 328
            self.match(MathParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_scopeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def printf(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathParser.PrintfContext)
            else:
                return self.getTypedRuleContext(MathParser.PrintfContext,i)


        def return_instr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathParser.Return_instrContext)
            else:
                return self.getTypedRuleContext(MathParser.Return_instrContext,i)


        def if_cond(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathParser.If_condContext)
            else:
                return self.getTypedRuleContext(MathParser.If_condContext,i)


        def while_loop(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathParser.While_loopContext)
            else:
                return self.getTypedRuleContext(MathParser.While_loopContext,i)


        def for_loop(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathParser.For_loopContext)
            else:
                return self.getTypedRuleContext(MathParser.For_loopContext,i)


        def assign(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathParser.AssignContext)
            else:
                return self.getTypedRuleContext(MathParser.AssignContext,i)


        def instr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathParser.InstrContext)
            else:
                return self.getTypedRuleContext(MathParser.InstrContext,i)


        def DELIM(self, i:int=None):
            if i is None:
                return self.getTokens(MathParser.DELIM)
            else:
                return self.getToken(MathParser.DELIM, i)

        def getRuleIndex(self):
            return MathParser.RULE_func_scope

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc_scope" ):
                listener.enterFunc_scope(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc_scope" ):
                listener.exitFunc_scope(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_scope" ):
                return visitor.visitFunc_scope(self)
            else:
                return visitor.visitChildren(self)




    def func_scope(self):

        localctx = MathParser.Func_scopeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_func_scope)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 330
            self.match(MathParser.T__4)
            self.state = 383
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 4081818720590888) != 0:
                self.state = 381
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,59,self._ctx)
                if la_ == 1:
                    self.state = 331
                    self.printf()
                    self.state = 338
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [1]:
                        self.state = 333 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while True:
                            self.state = 332
                            self.match(MathParser.T__0)
                            self.state = 335 
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            if not (_la==1):
                                break

                        pass
                    elif token in [57]:
                        self.state = 337
                        self.match(MathParser.DELIM)
                        pass
                    else:
                        raise NoViableAltException(self)

                    pass

                elif la_ == 2:
                    self.state = 340
                    self.return_instr()
                    pass

                elif la_ == 3:
                    self.state = 341
                    self.if_cond()
                    self.state = 349
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [1, 3, 5, 6, 10, 11, 12, 14, 15, 21, 22, 23, 25, 27, 28, 29, 30, 34, 37, 38, 47, 49, 50, 51]:
                        self.state = 345
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==1:
                            self.state = 342
                            self.match(MathParser.T__0)
                            self.state = 347
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        pass
                    elif token in [57]:
                        self.state = 348
                        self.match(MathParser.DELIM)
                        pass
                    else:
                        raise NoViableAltException(self)

                    pass

                elif la_ == 4:
                    self.state = 351
                    self.while_loop()
                    self.state = 359
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [1, 3, 5, 6, 10, 11, 12, 14, 15, 21, 22, 23, 25, 27, 28, 29, 30, 34, 37, 38, 47, 49, 50, 51]:
                        self.state = 355
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==1:
                            self.state = 352
                            self.match(MathParser.T__0)
                            self.state = 357
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        pass
                    elif token in [57]:
                        self.state = 358
                        self.match(MathParser.DELIM)
                        pass
                    else:
                        raise NoViableAltException(self)

                    pass

                elif la_ == 5:
                    self.state = 361
                    self.for_loop()
                    self.state = 369
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [1, 3, 5, 6, 10, 11, 12, 14, 15, 21, 22, 23, 25, 27, 28, 29, 30, 34, 37, 38, 47, 49, 50, 51]:
                        self.state = 365
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==1:
                            self.state = 362
                            self.match(MathParser.T__0)
                            self.state = 367
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        pass
                    elif token in [57]:
                        self.state = 368
                        self.match(MathParser.DELIM)
                        pass
                    else:
                        raise NoViableAltException(self)

                    pass

                elif la_ == 6:
                    self.state = 371
                    self.assign()
                    self.state = 378
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [1]:
                        self.state = 373 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while True:
                            self.state = 372
                            self.match(MathParser.T__0)
                            self.state = 375 
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            if not (_la==1):
                                break

                        pass
                    elif token in [57]:
                        self.state = 377
                        self.match(MathParser.DELIM)
                        pass
                    else:
                        raise NoViableAltException(self)

                    pass

                elif la_ == 7:
                    self.state = 380
                    self.instr()
                    pass


                self.state = 385
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 386
            self.match(MathParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_instrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ret_val = None # ExprContext

        def RETURN(self):
            return self.getToken(MathParser.RETURN, 0)

        def expr(self):
            return self.getTypedRuleContext(MathParser.ExprContext,0)


        def instr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathParser.InstrContext)
            else:
                return self.getTypedRuleContext(MathParser.InstrContext,i)


        def return_instr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathParser.Return_instrContext)
            else:
                return self.getTypedRuleContext(MathParser.Return_instrContext,i)


        def getRuleIndex(self):
            return MathParser.RULE_return_instr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturn_instr" ):
                listener.enterReturn_instr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturn_instr" ):
                listener.exitReturn_instr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_instr" ):
                return visitor.visitReturn_instr(self)
            else:
                return visitor.visitChildren(self)




    def return_instr(self):

        localctx = MathParser.Return_instrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_return_instr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 388
            self.match(MathParser.RETURN)

            self.state = 389
            localctx.ret_val = self.expr(0)
            self.state = 390
            self.match(MathParser.T__0)
            self.state = 395
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,62,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 393
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [3, 5, 10, 11, 23, 25, 27, 28, 29, 30, 34, 37, 38, 47, 49, 50, 51]:
                        self.state = 391
                        self.instr()
                        pass
                    elif token in [22]:
                        self.state = 392
                        self.return_instr()
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 397
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,62,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ScopeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def printf(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathParser.PrintfContext)
            else:
                return self.getTypedRuleContext(MathParser.PrintfContext,i)


        def return_instr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathParser.Return_instrContext)
            else:
                return self.getTypedRuleContext(MathParser.Return_instrContext,i)


        def if_cond(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathParser.If_condContext)
            else:
                return self.getTypedRuleContext(MathParser.If_condContext,i)


        def while_loop(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathParser.While_loopContext)
            else:
                return self.getTypedRuleContext(MathParser.While_loopContext,i)


        def for_loop(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathParser.For_loopContext)
            else:
                return self.getTypedRuleContext(MathParser.For_loopContext,i)


        def assign(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathParser.AssignContext)
            else:
                return self.getTypedRuleContext(MathParser.AssignContext,i)


        def break_instr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathParser.Break_instrContext)
            else:
                return self.getTypedRuleContext(MathParser.Break_instrContext,i)


        def cont_instr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathParser.Cont_instrContext)
            else:
                return self.getTypedRuleContext(MathParser.Cont_instrContext,i)


        def instr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathParser.InstrContext)
            else:
                return self.getTypedRuleContext(MathParser.InstrContext,i)


        def DELIM(self, i:int=None):
            if i is None:
                return self.getTokens(MathParser.DELIM)
            else:
                return self.getToken(MathParser.DELIM, i)

        def getRuleIndex(self):
            return MathParser.RULE_scope

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScope" ):
                listener.enterScope(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScope" ):
                listener.exitScope(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScope" ):
                return visitor.visitScope(self)
            else:
                return visitor.visitChildren(self)




    def scope(self):

        localctx = MathParser.ScopeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_scope)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 398
            self.match(MathParser.T__4)
            self.state = 453
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 4081818720787496) != 0:
                self.state = 451
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,73,self._ctx)
                if la_ == 1:
                    self.state = 399
                    self.printf()
                    self.state = 406
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [1]:
                        self.state = 401 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while True:
                            self.state = 400
                            self.match(MathParser.T__0)
                            self.state = 403 
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            if not (_la==1):
                                break

                        pass
                    elif token in [57]:
                        self.state = 405
                        self.match(MathParser.DELIM)
                        pass
                    else:
                        raise NoViableAltException(self)

                    pass

                elif la_ == 2:
                    self.state = 408
                    self.return_instr()
                    pass

                elif la_ == 3:
                    self.state = 409
                    self.if_cond()
                    self.state = 417
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [1, 3, 5, 6, 10, 11, 12, 14, 15, 16, 17, 21, 22, 23, 25, 27, 28, 29, 30, 34, 37, 38, 47, 49, 50, 51]:
                        self.state = 413
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==1:
                            self.state = 410
                            self.match(MathParser.T__0)
                            self.state = 415
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        pass
                    elif token in [57]:
                        self.state = 416
                        self.match(MathParser.DELIM)
                        pass
                    else:
                        raise NoViableAltException(self)

                    pass

                elif la_ == 4:
                    self.state = 419
                    self.while_loop()
                    self.state = 427
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [1, 3, 5, 6, 10, 11, 12, 14, 15, 16, 17, 21, 22, 23, 25, 27, 28, 29, 30, 34, 37, 38, 47, 49, 50, 51]:
                        self.state = 423
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==1:
                            self.state = 420
                            self.match(MathParser.T__0)
                            self.state = 425
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        pass
                    elif token in [57]:
                        self.state = 426
                        self.match(MathParser.DELIM)
                        pass
                    else:
                        raise NoViableAltException(self)

                    pass

                elif la_ == 5:
                    self.state = 429
                    self.for_loop()
                    self.state = 437
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [1, 3, 5, 6, 10, 11, 12, 14, 15, 16, 17, 21, 22, 23, 25, 27, 28, 29, 30, 34, 37, 38, 47, 49, 50, 51]:
                        self.state = 433
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==1:
                            self.state = 430
                            self.match(MathParser.T__0)
                            self.state = 435
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        pass
                    elif token in [57]:
                        self.state = 436
                        self.match(MathParser.DELIM)
                        pass
                    else:
                        raise NoViableAltException(self)

                    pass

                elif la_ == 6:
                    self.state = 439
                    self.assign()
                    self.state = 446
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [1]:
                        self.state = 441 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while True:
                            self.state = 440
                            self.match(MathParser.T__0)
                            self.state = 443 
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            if not (_la==1):
                                break

                        pass
                    elif token in [57]:
                        self.state = 445
                        self.match(MathParser.DELIM)
                        pass
                    else:
                        raise NoViableAltException(self)

                    pass

                elif la_ == 7:
                    self.state = 448
                    self.break_instr()
                    pass

                elif la_ == 8:
                    self.state = 449
                    self.cont_instr()
                    pass

                elif la_ == 9:
                    self.state = 450
                    self.instr()
                    pass


                self.state = 455
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 456
            self.match(MathParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Cont_instrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(MathParser.CONTINUE, 0)

        def DELIM(self):
            return self.getToken(MathParser.DELIM, 0)

        def instr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathParser.InstrContext)
            else:
                return self.getTypedRuleContext(MathParser.InstrContext,i)


        def getRuleIndex(self):
            return MathParser.RULE_cont_instr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCont_instr" ):
                listener.enterCont_instr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCont_instr" ):
                listener.exitCont_instr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCont_instr" ):
                return visitor.visitCont_instr(self)
            else:
                return visitor.visitChildren(self)




    def cont_instr(self):

        localctx = MathParser.Cont_instrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_cont_instr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 458
            self.match(MathParser.CONTINUE)
            self.state = 459
            _la = self._input.LA(1)
            if not(_la==1 or _la==57):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 463
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,75,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 460
                    self.instr() 
                self.state = 465
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,75,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_instrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(MathParser.BREAK, 0)

        def DELIM(self):
            return self.getToken(MathParser.DELIM, 0)

        def instr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathParser.InstrContext)
            else:
                return self.getTypedRuleContext(MathParser.InstrContext,i)


        def getRuleIndex(self):
            return MathParser.RULE_break_instr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBreak_instr" ):
                listener.enterBreak_instr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBreak_instr" ):
                listener.exitBreak_instr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_instr" ):
                return visitor.visitBreak_instr(self)
            else:
                return visitor.visitChildren(self)




    def break_instr(self):

        localctx = MathParser.Break_instrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_break_instr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 466
            self.match(MathParser.BREAK)
            self.state = 467
            _la = self._input.LA(1)
            if not(_la==1 or _la==57):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 471
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,76,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 468
                    self.instr() 
                self.state = 473
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,76,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.const = None # Token
            self.type_ = None # Token
            self.name = None # Token
            self.size = None # Token
            self._rtype = None # RtypeContext
            self.values = list() # of RtypeContexts

        def ASSIGN(self):
            return self.getToken(MathParser.ASSIGN, 0)

        def TYPE(self):
            return self.getToken(MathParser.TYPE, 0)

        def VAR_NAME(self):
            return self.getToken(MathParser.VAR_NAME, 0)

        def rtype(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathParser.RtypeContext)
            else:
                return self.getTypedRuleContext(MathParser.RtypeContext,i)


        def CONST(self):
            return self.getToken(MathParser.CONST, 0)

        def INT(self):
            return self.getToken(MathParser.INT, 0)

        def getRuleIndex(self):
            return MathParser.RULE_array_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray_decl" ):
                listener.enterArray_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray_decl" ):
                listener.exitArray_decl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_decl" ):
                return visitor.visitArray_decl(self)
            else:
                return visitor.visitChildren(self)




    def array_decl(self):

        localctx = MathParser.Array_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_array_decl)
        self._la = 0 # Token type
        try:
            self.state = 505
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,81,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 475
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==11:
                    self.state = 474
                    localctx.const = self.match(MathParser.CONST)


                self.state = 477
                localctx.type_ = self.match(MathParser.TYPE)
                self.state = 478
                localctx.name = self.match(MathParser.VAR_NAME)
                self.state = 479
                self.match(MathParser.T__6)
                self.state = 481
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==28:
                    self.state = 480
                    localctx.size = self.match(MathParser.INT)


                self.state = 483
                self.match(MathParser.T__7)
                self.state = 484
                self.match(MathParser.ASSIGN)
                self.state = 485
                self.match(MathParser.T__4)
                self.state = 491
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,79,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 486
                        localctx._rtype = self.rtype()
                        localctx.values.append(localctx._rtype)
                        self.state = 487
                        self.match(MathParser.T__1) 
                    self.state = 493
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,79,self._ctx)

                self.state = 494
                localctx._rtype = self.rtype()
                localctx.values.append(localctx._rtype)
                self.state = 495
                self.match(MathParser.T__5)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 498
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==11:
                    self.state = 497
                    localctx.const = self.match(MathParser.CONST)


                self.state = 500
                localctx.type_ = self.match(MathParser.TYPE)
                self.state = 501
                localctx.name = self.match(MathParser.VAR_NAME)
                self.state = 502
                self.match(MathParser.T__6)
                self.state = 503
                localctx.size = self.match(MathParser.INT)
                self.state = 504
                self.match(MathParser.T__7)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Incl_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.library = None # Token

        def INCLUDE(self):
            return self.getToken(MathParser.INCLUDE, 0)

        def LT(self):
            return self.getToken(MathParser.LT, 0)

        def GT(self):
            return self.getToken(MathParser.GT, 0)

        def VAR_NAME(self):
            return self.getToken(MathParser.VAR_NAME, 0)

        def getRuleIndex(self):
            return MathParser.RULE_incl_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIncl_stat" ):
                listener.enterIncl_stat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIncl_stat" ):
                listener.exitIncl_stat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIncl_stat" ):
                return visitor.visitIncl_stat(self)
            else:
                return visitor.visitChildren(self)




    def incl_stat(self):

        localctx = MathParser.Incl_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_incl_stat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 507
            self.match(MathParser.INCLUDE)
            self.state = 508
            self.match(MathParser.LT)
            self.state = 509
            localctx.library = self.match(MathParser.VAR_NAME)
            self.state = 510
            self.match(MathParser.T__8)
            self.state = 511
            self.match(MathParser.GT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_condContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.condition = None # CondContext

        def IF(self):
            return self.getToken(MathParser.IF, 0)

        def scope(self):
            return self.getTypedRuleContext(MathParser.ScopeContext,0)


        def cond(self):
            return self.getTypedRuleContext(MathParser.CondContext,0)


        def else_cond(self):
            return self.getTypedRuleContext(MathParser.Else_condContext,0)


        def getRuleIndex(self):
            return MathParser.RULE_if_cond

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_cond" ):
                listener.enterIf_cond(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_cond" ):
                listener.exitIf_cond(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_cond" ):
                return visitor.visitIf_cond(self)
            else:
                return visitor.visitChildren(self)




    def if_cond(self):

        localctx = MathParser.If_condContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_if_cond)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 513
            self.match(MathParser.IF)
            self.state = 514
            self.match(MathParser.T__2)
            self.state = 515
            localctx.condition = self.cond()
            self.state = 516
            self.match(MathParser.T__3)
            self.state = 517
            self.scope()
            self.state = 519
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 518
                self.else_cond()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_condContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(MathParser.ELSE, 0)

        def scope(self):
            return self.getTypedRuleContext(MathParser.ScopeContext,0)


        def getRuleIndex(self):
            return MathParser.RULE_else_cond

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElse_cond" ):
                listener.enterElse_cond(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElse_cond" ):
                listener.exitElse_cond(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_cond" ):
                return visitor.visitElse_cond(self)
            else:
                return visitor.visitChildren(self)




    def else_cond(self):

        localctx = MathParser.Else_condContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_else_cond)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 521
            self.match(MathParser.ELSE)
            self.state = 522
            self.scope()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_loopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.condition = None # CondContext

        def WHILE(self):
            return self.getToken(MathParser.WHILE, 0)

        def scope(self):
            return self.getTypedRuleContext(MathParser.ScopeContext,0)


        def cond(self):
            return self.getTypedRuleContext(MathParser.CondContext,0)


        def getRuleIndex(self):
            return MathParser.RULE_while_loop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile_loop" ):
                listener.enterWhile_loop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile_loop" ):
                listener.exitWhile_loop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_loop" ):
                return visitor.visitWhile_loop(self)
            else:
                return visitor.visitChildren(self)




    def while_loop(self):

        localctx = MathParser.While_loopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_while_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 524
            self.match(MathParser.WHILE)
            self.state = 525
            self.match(MathParser.T__2)
            self.state = 526
            localctx.condition = self.cond()
            self.state = 527
            self.match(MathParser.T__3)
            self.state = 528
            self.scope()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_loopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.initialization = None # InitContext
            self.condition = None # CondContext
            self.increment = None # IncrContext

        def FOR(self):
            return self.getToken(MathParser.FOR, 0)

        def scope(self):
            return self.getTypedRuleContext(MathParser.ScopeContext,0)


        def init(self):
            return self.getTypedRuleContext(MathParser.InitContext,0)


        def cond(self):
            return self.getTypedRuleContext(MathParser.CondContext,0)


        def incr(self):
            return self.getTypedRuleContext(MathParser.IncrContext,0)


        def getRuleIndex(self):
            return MathParser.RULE_for_loop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_loop" ):
                listener.enterFor_loop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_loop" ):
                listener.exitFor_loop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_loop" ):
                return visitor.visitFor_loop(self)
            else:
                return visitor.visitChildren(self)




    def for_loop(self):

        localctx = MathParser.For_loopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_for_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 530
            self.match(MathParser.FOR)
            self.state = 531
            self.match(MathParser.T__2)
            self.state = 532
            localctx.initialization = self.init()
            self.state = 533
            self.match(MathParser.T__0)
            self.state = 534
            localctx.condition = self.cond()
            self.state = 535
            self.match(MathParser.T__0)
            self.state = 536
            localctx.increment = self.incr()
            self.state = 537
            self.match(MathParser.T__3)
            self.state = 538
            self.scope()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MathParser.TYPE, 0)

        def lvar(self):
            return self.getTypedRuleContext(MathParser.LvarContext,0)


        def ASSIGN(self):
            return self.getToken(MathParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(MathParser.ExprContext,0)


        def assign(self):
            return self.getTypedRuleContext(MathParser.AssignContext,0)


        def getRuleIndex(self):
            return MathParser.RULE_init

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInit" ):
                listener.enterInit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInit" ):
                listener.exitInit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInit" ):
                return visitor.visitInit(self)
            else:
                return visitor.visitChildren(self)




    def init(self):

        localctx = MathParser.InitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_init)
        try:
            self.state = 546
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [25]:
                self.enterOuterAlt(localctx, 1)
                self.state = 540
                self.match(MathParser.TYPE)
                self.state = 541
                self.lvar()
                self.state = 542
                self.match(MathParser.ASSIGN)
                self.state = 543
                self.expr(0)
                pass
            elif token in [27, 34]:
                self.enterOuterAlt(localctx, 2)
                self.state = 545
                self.assign()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self):
            return self.getTypedRuleContext(MathParser.TermContext,0)


        def factor(self):
            return self.getTypedRuleContext(MathParser.FactorContext,0)


        def GEQ(self):
            return self.getToken(MathParser.GEQ, 0)

        def LEQ(self):
            return self.getToken(MathParser.LEQ, 0)

        def NEQ(self):
            return self.getToken(MathParser.NEQ, 0)

        def GT(self):
            return self.getToken(MathParser.GT, 0)

        def LT(self):
            return self.getToken(MathParser.LT, 0)

        def EQ(self):
            return self.getToken(MathParser.EQ, 0)

        def expr(self):
            return self.getTypedRuleContext(MathParser.ExprContext,0)


        def AND_OP(self):
            return self.getToken(MathParser.AND_OP, 0)

        def OR_OP(self):
            return self.getToken(MathParser.OR_OP, 0)

        def getRuleIndex(self):
            return MathParser.RULE_cond

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCond" ):
                listener.enterCond(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCond" ):
                listener.exitCond(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCond" ):
                return visitor.visitCond(self)
            else:
                return visitor.visitChildren(self)




    def cond(self):

        localctx = MathParser.CondContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_cond)
        self._la = 0 # Token type
        try:
            self.state = 561
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,84,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 548
                self.term(0)
                self.state = 549
                _la = self._input.LA(1)
                if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 23089744183296) != 0):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 550
                self.factor()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 552
                self.term(0)
                self.state = 553
                _la = self._input.LA(1)
                if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 11544872091648) != 0):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 554
                self.factor()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 556
                self.expr(0)
                self.state = 557
                _la = self._input.LA(1)
                if not(_la==45 or _la==46):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 558
                self.term(0)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 560
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IncrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INCR(self):
            return self.getToken(MathParser.INCR, 0)

        def rvar(self):
            return self.getTypedRuleContext(MathParser.RvarContext,0)


        def DECR(self):
            return self.getToken(MathParser.DECR, 0)

        def getRuleIndex(self):
            return MathParser.RULE_incr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIncr" ):
                listener.enterIncr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIncr" ):
                listener.exitIncr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIncr" ):
                return visitor.visitIncr(self)
            else:
                return visitor.visitChildren(self)




    def incr(self):

        localctx = MathParser.IncrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_incr)
        try:
            self.state = 573
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,85,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 563
                self.match(MathParser.INCR)
                self.state = 564
                self.rvar()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 565
                self.match(MathParser.DECR)
                self.state = 566
                self.rvar()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 567
                self.rvar()
                self.state = 568
                self.match(MathParser.INCR)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 570
                self.rvar()
                self.state = 571
                self.match(MathParser.DECR)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lvar(self):
            return self.getTypedRuleContext(MathParser.LvarContext,0)


        def ASSIGN(self):
            return self.getToken(MathParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(MathParser.ExprContext,0)


        def getRuleIndex(self):
            return MathParser.RULE_var_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar_decl" ):
                listener.enterVar_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar_decl" ):
                listener.exitVar_decl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl" ):
                return visitor.visitVar_decl(self)
            else:
                return visitor.visitChildren(self)




    def var_decl(self):

        localctx = MathParser.Var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_var_decl)
        try:
            self.state = 580
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,86,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 575
                self.lvar()
                self.state = 576
                self.match(MathParser.ASSIGN)
                self.state = 577
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 579
                self.lvar()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def rvar(self):
            return self.getTypedRuleContext(MathParser.RvarContext,0)


        def ASSIGN(self):
            return self.getToken(MathParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(MathParser.ExprContext,0)


        def deref(self):
            return self.getTypedRuleContext(MathParser.DerefContext,0)


        def array_el(self):
            return self.getTypedRuleContext(MathParser.Array_elContext,0)


        def getRuleIndex(self):
            return MathParser.RULE_assign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)




    def assign(self):

        localctx = MathParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_assign)
        try:
            self.state = 594
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,87,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 582
                self.rvar()
                self.state = 583
                self.match(MathParser.ASSIGN)
                self.state = 584
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 586
                self.deref()
                self.state = 587
                self.match(MathParser.ASSIGN)
                self.state = 588
                self.expr(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 590
                self.array_el()
                self.state = 591
                self.match(MathParser.ASSIGN)
                self.state = 592
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_elContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lvar(self):
            return self.getTypedRuleContext(MathParser.LvarContext,0)


        def INT(self):
            return self.getToken(MathParser.INT, 0)

        def getRuleIndex(self):
            return MathParser.RULE_array_el

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray_el" ):
                listener.enterArray_el(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray_el" ):
                listener.exitArray_el(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_el" ):
                return visitor.visitArray_el(self)
            else:
                return visitor.visitChildren(self)




    def array_el(self):

        localctx = MathParser.Array_elContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_array_el)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 596
            self.lvar()
            self.state = 597
            self.match(MathParser.T__6)
            self.state = 598
            self.match(MathParser.INT)
            self.state = 599
            self.match(MathParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DerefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STR(self):
            return self.getToken(MathParser.STR, 0)

        def deref(self):
            return self.getTypedRuleContext(MathParser.DerefContext,0)


        def rvar(self):
            return self.getTypedRuleContext(MathParser.RvarContext,0)


        def getRuleIndex(self):
            return MathParser.RULE_deref

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeref" ):
                listener.enterDeref(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeref" ):
                listener.exitDeref(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeref" ):
                return visitor.visitDeref(self)
            else:
                return visitor.visitChildren(self)




    def deref(self):

        localctx = MathParser.DerefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_deref)
        try:
            self.state = 605
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,88,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 601
                self.match(MathParser.STR)
                self.state = 602
                self.deref()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 603
                self.match(MathParser.STR)
                self.state = 604
                self.rvar()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LvarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._STR = None # Token
            self.ptr = list() # of Tokens
            self.name = None # Token

        def VAR_NAME(self):
            return self.getToken(MathParser.VAR_NAME, 0)

        def STR(self, i:int=None):
            if i is None:
                return self.getTokens(MathParser.STR)
            else:
                return self.getToken(MathParser.STR, i)

        def getRuleIndex(self):
            return MathParser.RULE_lvar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLvar" ):
                listener.enterLvar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLvar" ):
                listener.exitLvar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLvar" ):
                return visitor.visitLvar(self)
            else:
                return visitor.visitChildren(self)




    def lvar(self):

        localctx = MathParser.LvarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_lvar)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 610
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==34:
                self.state = 607
                localctx._STR = self.match(MathParser.STR)
                localctx.ptr.append(localctx._STR)
                self.state = 612
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 613
            localctx.name = self.match(MathParser.VAR_NAME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RvarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR_NAME(self):
            return self.getToken(MathParser.VAR_NAME, 0)

        def getRuleIndex(self):
            return MathParser.RULE_rvar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRvar" ):
                listener.enterRvar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRvar" ):
                listener.exitRvar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRvar" ):
                return visitor.visitRvar(self)
            else:
                return visitor.visitChildren(self)




    def rvar(self):

        localctx = MathParser.RvarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_rvar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 615
            self.match(MathParser.VAR_NAME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self):
            return self.getTypedRuleContext(MathParser.TermContext,0)


        def expr(self):
            return self.getTypedRuleContext(MathParser.ExprContext,0)


        def SUM(self):
            return self.getToken(MathParser.SUM, 0)

        def DIF(self):
            return self.getToken(MathParser.DIF, 0)

        def AND_OP(self):
            return self.getToken(MathParser.AND_OP, 0)

        def OR_OP(self):
            return self.getToken(MathParser.OR_OP, 0)

        def getRuleIndex(self):
            return MathParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MathParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 66
        self.enterRecursionRule(localctx, 66, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 618
            self.term(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 631
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,91,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 629
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,90,self._ctx)
                    if la_ == 1:
                        localctx = MathParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 620
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 621
                        self.match(MathParser.SUM)
                        self.state = 622
                        self.term(0)
                        pass

                    elif la_ == 2:
                        localctx = MathParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 623
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 624
                        self.match(MathParser.DIF)
                        self.state = 625
                        self.term(0)
                        pass

                    elif la_ == 3:
                        localctx = MathParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 626
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 627
                        _la = self._input.LA(1)
                        if not(_la==45 or _la==46):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 628
                        self.term(0)
                        pass

             
                self.state = 633
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,91,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self):
            return self.getTypedRuleContext(MathParser.FactorContext,0)


        def NOT_OP(self):
            return self.getToken(MathParser.NOT_OP, 0)

        def term(self):
            return self.getTypedRuleContext(MathParser.TermContext,0)


        def STR(self):
            return self.getToken(MathParser.STR, 0)

        def DIV(self):
            return self.getToken(MathParser.DIV, 0)

        def MOD(self):
            return self.getToken(MathParser.MOD, 0)

        def GT(self):
            return self.getToken(MathParser.GT, 0)

        def LT(self):
            return self.getToken(MathParser.LT, 0)

        def EQ(self):
            return self.getToken(MathParser.EQ, 0)

        def GEQ(self):
            return self.getToken(MathParser.GEQ, 0)

        def LEQ(self):
            return self.getToken(MathParser.LEQ, 0)

        def NEQ(self):
            return self.getToken(MathParser.NEQ, 0)

        def INCR(self):
            return self.getToken(MathParser.INCR, 0)

        def DECR(self):
            return self.getToken(MathParser.DECR, 0)

        def getRuleIndex(self):
            return MathParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)



    def term(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MathParser.TermContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 68
        self.enterRecursionRule(localctx, 68, self.RULE_term, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 638
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 10, 27, 28, 29, 30, 34, 37, 38, 49, 50, 51]:
                self.state = 635
                self.factor()
                pass
            elif token in [47]:
                self.state = 636
                self.match(MathParser.NOT_OP)
                self.state = 637
                self.factor()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 653
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,94,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 651
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,93,self._ctx)
                    if la_ == 1:
                        localctx = MathParser.TermContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 640
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 641
                        _la = self._input.LA(1)
                        if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 120259084288) != 0):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 642
                        self.factor()
                        pass

                    elif la_ == 2:
                        localctx = MathParser.TermContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 643
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 644
                        _la = self._input.LA(1)
                        if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 11544872091648) != 0):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 645
                        self.factor()
                        pass

                    elif la_ == 3:
                        localctx = MathParser.TermContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 646
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 647
                        _la = self._input.LA(1)
                        if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 23089744183296) != 0):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 648
                        self.factor()
                        pass

                    elif la_ == 4:
                        localctx = MathParser.TermContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 649
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 650
                        _la = self._input.LA(1)
                        if not(_la==50 or _la==51):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        pass

             
                self.state = 655
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,94,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primary(self):
            return self.getTypedRuleContext(MathParser.PrimaryContext,0)


        def DIF(self):
            return self.getToken(MathParser.DIF, 0)

        def factor(self):
            return self.getTypedRuleContext(MathParser.FactorContext,0)


        def SUM(self):
            return self.getToken(MathParser.SUM, 0)

        def INCR(self):
            return self.getToken(MathParser.INCR, 0)

        def DECR(self):
            return self.getToken(MathParser.DECR, 0)

        def getRuleIndex(self):
            return MathParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)




    def factor(self):

        localctx = MathParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_factor)
        self._la = 0 # Token type
        try:
            self.state = 663
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 10, 27, 28, 29, 30, 34, 49]:
                self.enterOuterAlt(localctx, 1)
                self.state = 656
                self.primary()
                pass
            elif token in [38]:
                self.enterOuterAlt(localctx, 2)
                self.state = 657
                self.match(MathParser.DIF)
                self.state = 658
                self.factor()
                pass
            elif token in [37]:
                self.enterOuterAlt(localctx, 3)
                self.state = 659
                self.match(MathParser.SUM)
                self.state = 660
                self.factor()
                pass
            elif token in [50, 51]:
                self.enterOuterAlt(localctx, 4)
                self.state = 661
                _la = self._input.LA(1)
                if not(_la==50 or _la==51):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 662
                self.factor()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def rvar(self):
            return self.getTypedRuleContext(MathParser.RvarContext,0)


        def rtype(self):
            return self.getTypedRuleContext(MathParser.RtypeContext,0)


        def ADDR(self):
            return self.getToken(MathParser.ADDR, 0)

        def deref(self):
            return self.getTypedRuleContext(MathParser.DerefContext,0)


        def expr(self):
            return self.getTypedRuleContext(MathParser.ExprContext,0)


        def CAST(self):
            return self.getToken(MathParser.CAST, 0)

        def primary(self):
            return self.getTypedRuleContext(MathParser.PrimaryContext,0)


        def func_call(self):
            return self.getTypedRuleContext(MathParser.Func_callContext,0)


        def getRuleIndex(self):
            return MathParser.RULE_primary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimary" ):
                listener.enterPrimary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimary" ):
                listener.exitPrimary(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimary" ):
                return visitor.visitPrimary(self)
            else:
                return visitor.visitChildren(self)




    def primary(self):

        localctx = MathParser.PrimaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_primary)
        try:
            self.state = 677
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,96,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 665
                self.rvar()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 666
                self.rtype()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 667
                self.match(MathParser.ADDR)
                self.state = 668
                self.rvar()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 669
                self.deref()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 670
                self.match(MathParser.T__2)
                self.state = 671
                self.expr(0)
                self.state = 672
                self.match(MathParser.T__3)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 674
                self.match(MathParser.CAST)
                self.state = 675
                self.primary()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 676
                self.func_call()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RtypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(MathParser.INT, 0)

        def FLOAT(self):
            return self.getToken(MathParser.FLOAT, 0)

        def CHAR(self):
            return self.getToken(MathParser.CHAR, 0)

        def getRuleIndex(self):
            return MathParser.RULE_rtype

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRtype" ):
                listener.enterRtype(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRtype" ):
                listener.exitRtype(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRtype" ):
                return visitor.visitRtype(self)
            else:
                return visitor.visitChildren(self)




    def rtype(self):

        localctx = MathParser.RtypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_rtype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 679
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 1879048192) != 0):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[33] = self.expr_sempred
        self._predicates[34] = self.term_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 1)
         

    def term_sempred(self, localctx:TermContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 1)
         




