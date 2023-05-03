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
        4,1,59,681,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
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
        1,1,3,1,153,8,1,3,1,155,8,1,1,2,3,2,158,8,2,1,2,1,2,1,2,1,2,5,2,
        164,8,2,10,2,12,2,167,9,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,5,
        3,178,8,3,10,3,12,3,181,9,3,1,3,3,3,184,8,3,1,3,1,3,1,3,1,3,1,3,
        3,3,191,8,3,1,3,1,3,3,3,195,8,3,1,4,1,4,1,4,3,4,200,8,4,1,5,1,5,
        1,5,1,5,1,5,3,5,207,8,5,1,5,1,5,1,5,5,5,212,8,5,10,5,12,5,215,9,
        5,1,5,3,5,218,8,5,1,5,1,5,1,5,1,6,1,6,1,6,5,6,226,8,6,10,6,12,6,
        229,9,6,1,7,3,7,232,8,7,1,7,1,7,3,7,236,8,7,1,7,5,7,239,8,7,10,7,
        12,7,242,9,7,1,7,1,7,1,7,3,7,247,8,7,1,7,3,7,250,8,7,1,7,1,7,5,7,
        254,8,7,10,7,12,7,257,9,7,1,7,3,7,260,8,7,1,7,1,7,1,7,3,7,265,8,
        7,3,7,267,8,7,1,8,3,8,270,8,8,1,8,1,8,3,8,274,8,8,1,8,5,8,277,8,
        8,10,8,12,8,280,9,8,1,8,1,8,1,8,3,8,285,8,8,1,8,1,8,1,8,1,9,3,9,
        291,8,9,1,9,1,9,3,9,295,8,9,1,9,5,9,298,8,9,10,9,12,9,301,9,9,1,
        9,1,9,1,9,3,9,306,8,9,1,9,1,9,1,10,1,10,1,10,4,10,313,8,10,11,10,
        12,10,314,1,11,1,11,1,11,1,11,3,11,321,8,11,1,12,1,12,1,12,3,12,
        326,8,12,1,12,1,12,1,13,1,13,1,13,4,13,333,8,13,11,13,12,13,334,
        1,13,3,13,338,8,13,1,13,1,13,1,13,5,13,343,8,13,10,13,12,13,346,
        9,13,1,13,3,13,349,8,13,1,13,1,13,5,13,353,8,13,10,13,12,13,356,
        9,13,1,13,3,13,359,8,13,1,13,1,13,5,13,363,8,13,10,13,12,13,366,
        9,13,1,13,3,13,369,8,13,1,13,1,13,4,13,373,8,13,11,13,12,13,374,
        1,13,3,13,378,8,13,1,13,5,13,381,8,13,10,13,12,13,384,9,13,1,13,
        1,13,1,14,1,14,1,14,1,14,1,14,5,14,393,8,14,10,14,12,14,396,9,14,
        1,15,1,15,1,15,4,15,401,8,15,11,15,12,15,402,1,15,3,15,406,8,15,
        1,15,1,15,1,15,5,15,411,8,15,10,15,12,15,414,9,15,1,15,3,15,417,
        8,15,1,15,1,15,5,15,421,8,15,10,15,12,15,424,9,15,1,15,3,15,427,
        8,15,1,15,1,15,5,15,431,8,15,10,15,12,15,434,9,15,1,15,3,15,437,
        8,15,1,15,1,15,4,15,441,8,15,11,15,12,15,442,1,15,3,15,446,8,15,
        1,15,1,15,1,15,5,15,451,8,15,10,15,12,15,454,9,15,1,15,1,15,1,16,
        1,16,1,16,5,16,461,8,16,10,16,12,16,464,9,16,1,17,1,17,1,17,5,17,
        469,8,17,10,17,12,17,472,9,17,1,18,3,18,475,8,18,1,18,1,18,1,18,
        1,18,3,18,481,8,18,1,18,1,18,1,18,1,18,1,18,1,18,5,18,489,8,18,10,
        18,12,18,492,9,18,1,18,1,18,1,18,1,18,3,18,498,8,18,1,18,1,18,1,
        18,1,18,1,18,3,18,505,8,18,1,19,1,19,1,19,1,19,1,19,1,19,1,20,1,
        20,1,20,1,20,1,20,1,20,3,20,519,8,20,1,21,1,21,1,21,1,22,1,22,1,
        22,1,22,1,22,1,22,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,
        23,1,24,1,24,1,24,1,24,1,24,1,24,3,24,546,8,24,1,25,1,25,1,25,1,
        25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,3,25,561,8,25,1,
        26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,3,26,573,8,26,1,
        27,1,27,1,27,1,27,1,27,3,27,580,8,27,1,28,1,28,1,28,1,28,1,28,1,
        28,1,28,1,28,1,28,1,28,1,28,1,28,3,28,594,8,28,1,29,1,29,1,29,1,
        29,1,29,1,30,1,30,1,30,1,30,3,30,605,8,30,1,31,5,31,608,8,31,10,
        31,12,31,611,9,31,1,31,1,31,1,32,1,32,1,33,1,33,1,33,1,33,1,33,1,
        33,1,33,1,33,1,33,1,33,1,33,1,33,5,33,629,8,33,10,33,12,33,632,9,
        33,1,34,1,34,1,34,1,34,3,34,638,8,34,1,34,1,34,1,34,1,34,1,34,1,
        34,1,34,1,34,1,34,1,34,1,34,5,34,651,8,34,10,34,12,34,654,9,34,1,
        35,1,35,1,35,1,35,1,35,1,35,1,35,3,35,663,8,35,1,36,1,36,1,36,1,
        36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,3,36,677,8,36,1,37,1,
        37,1,37,1,314,2,66,68,38,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,
        30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,
        74,0,7,2,0,1,1,57,57,3,0,40,40,42,42,44,44,3,0,39,39,41,41,43,43,
        1,0,45,46,1,0,34,36,1,0,50,51,1,0,28,30,773,0,79,1,0,0,0,2,154,1,
        0,0,0,4,157,1,0,0,0,6,194,1,0,0,0,8,199,1,0,0,0,10,201,1,0,0,0,12,
        222,1,0,0,0,14,266,1,0,0,0,16,269,1,0,0,0,18,290,1,0,0,0,20,309,
        1,0,0,0,22,320,1,0,0,0,24,322,1,0,0,0,26,329,1,0,0,0,28,387,1,0,
        0,0,30,397,1,0,0,0,32,457,1,0,0,0,34,465,1,0,0,0,36,504,1,0,0,0,
        38,506,1,0,0,0,40,512,1,0,0,0,42,520,1,0,0,0,44,523,1,0,0,0,46,529,
        1,0,0,0,48,545,1,0,0,0,50,560,1,0,0,0,52,572,1,0,0,0,54,579,1,0,
        0,0,56,593,1,0,0,0,58,595,1,0,0,0,60,604,1,0,0,0,62,609,1,0,0,0,
        64,614,1,0,0,0,66,616,1,0,0,0,68,637,1,0,0,0,70,662,1,0,0,0,72,676,
        1,0,0,0,74,678,1,0,0,0,76,78,3,38,19,0,77,76,1,0,0,0,78,81,1,0,0,
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
        115,1,0,0,0,117,155,1,0,0,0,118,125,3,36,18,0,119,121,5,1,0,0,120,
        119,1,0,0,0,121,122,1,0,0,0,122,120,1,0,0,0,122,123,1,0,0,0,123,
        126,1,0,0,0,124,126,5,57,0,0,125,120,1,0,0,0,125,124,1,0,0,0,126,
        155,1,0,0,0,127,134,3,66,33,0,128,130,5,1,0,0,129,128,1,0,0,0,130,
        131,1,0,0,0,131,129,1,0,0,0,131,132,1,0,0,0,132,135,1,0,0,0,133,
        135,5,57,0,0,134,129,1,0,0,0,134,133,1,0,0,0,135,155,1,0,0,0,136,
        143,3,10,5,0,137,139,5,1,0,0,138,137,1,0,0,0,139,140,1,0,0,0,140,
        138,1,0,0,0,140,141,1,0,0,0,141,144,1,0,0,0,142,144,5,57,0,0,143,
        138,1,0,0,0,143,142,1,0,0,0,144,155,1,0,0,0,145,152,3,56,28,0,146,
        148,5,1,0,0,147,146,1,0,0,0,148,149,1,0,0,0,149,147,1,0,0,0,149,
        150,1,0,0,0,150,153,1,0,0,0,151,153,5,57,0,0,152,147,1,0,0,0,152,
        151,1,0,0,0,153,155,1,0,0,0,154,109,1,0,0,0,154,118,1,0,0,0,154,
        127,1,0,0,0,154,136,1,0,0,0,154,145,1,0,0,0,155,3,1,0,0,0,156,158,
        5,11,0,0,157,156,1,0,0,0,157,158,1,0,0,0,158,159,1,0,0,0,159,165,
        5,25,0,0,160,161,3,54,27,0,161,162,5,2,0,0,162,164,1,0,0,0,163,160,
        1,0,0,0,164,167,1,0,0,0,165,163,1,0,0,0,165,166,1,0,0,0,166,168,
        1,0,0,0,167,165,1,0,0,0,168,169,3,54,27,0,169,5,1,0,0,0,170,171,
        5,21,0,0,171,172,5,3,0,0,172,183,5,31,0,0,173,179,5,2,0,0,174,175,
        3,8,4,0,175,176,5,2,0,0,176,178,1,0,0,0,177,174,1,0,0,0,178,181,
        1,0,0,0,179,177,1,0,0,0,179,180,1,0,0,0,180,182,1,0,0,0,181,179,
        1,0,0,0,182,184,3,8,4,0,183,173,1,0,0,0,183,184,1,0,0,0,184,185,
        1,0,0,0,185,195,5,4,0,0,186,187,5,21,0,0,187,190,5,3,0,0,188,191,
        3,64,32,0,189,191,3,74,37,0,190,188,1,0,0,0,190,189,1,0,0,0,191,
        192,1,0,0,0,192,193,5,4,0,0,193,195,1,0,0,0,194,170,1,0,0,0,194,
        186,1,0,0,0,195,7,1,0,0,0,196,200,3,64,32,0,197,200,3,74,37,0,198,
        200,5,31,0,0,199,196,1,0,0,0,199,197,1,0,0,0,199,198,1,0,0,0,200,
        9,1,0,0,0,201,202,5,23,0,0,202,203,5,3,0,0,203,204,5,31,0,0,204,
        213,5,2,0,0,205,207,5,49,0,0,206,205,1,0,0,0,206,207,1,0,0,0,207,
        208,1,0,0,0,208,209,3,64,32,0,209,210,5,2,0,0,210,212,1,0,0,0,211,
        206,1,0,0,0,212,215,1,0,0,0,213,211,1,0,0,0,213,214,1,0,0,0,214,
        217,1,0,0,0,215,213,1,0,0,0,216,218,5,49,0,0,217,216,1,0,0,0,217,
        218,1,0,0,0,218,219,1,0,0,0,219,220,3,64,32,0,220,221,5,4,0,0,221,
        11,1,0,0,0,222,227,3,14,7,0,223,224,5,2,0,0,224,226,3,14,7,0,225,
        223,1,0,0,0,226,229,1,0,0,0,227,225,1,0,0,0,227,228,1,0,0,0,228,
        13,1,0,0,0,229,227,1,0,0,0,230,232,5,11,0,0,231,230,1,0,0,0,231,
        232,1,0,0,0,232,233,1,0,0,0,233,235,5,25,0,0,234,236,5,49,0,0,235,
        234,1,0,0,0,235,236,1,0,0,0,236,240,1,0,0,0,237,239,5,34,0,0,238,
        237,1,0,0,0,239,242,1,0,0,0,240,238,1,0,0,0,240,241,1,0,0,0,241,
        243,1,0,0,0,242,240,1,0,0,0,243,246,5,27,0,0,244,245,5,48,0,0,245,
        247,3,66,33,0,246,244,1,0,0,0,246,247,1,0,0,0,247,267,1,0,0,0,248,
        250,5,11,0,0,249,248,1,0,0,0,249,250,1,0,0,0,250,251,1,0,0,0,251,
        255,5,25,0,0,252,254,5,34,0,0,253,252,1,0,0,0,254,257,1,0,0,0,255,
        253,1,0,0,0,255,256,1,0,0,0,256,259,1,0,0,0,257,255,1,0,0,0,258,
        260,5,49,0,0,259,258,1,0,0,0,259,260,1,0,0,0,260,261,1,0,0,0,261,
        264,5,27,0,0,262,263,5,48,0,0,263,265,3,66,33,0,264,262,1,0,0,0,
        264,265,1,0,0,0,265,267,1,0,0,0,266,231,1,0,0,0,266,249,1,0,0,0,
        267,15,1,0,0,0,268,270,5,11,0,0,269,268,1,0,0,0,269,270,1,0,0,0,
        270,273,1,0,0,0,271,274,5,25,0,0,272,274,5,26,0,0,273,271,1,0,0,
        0,273,272,1,0,0,0,274,278,1,0,0,0,275,277,5,34,0,0,276,275,1,0,0,
        0,277,280,1,0,0,0,278,276,1,0,0,0,278,279,1,0,0,0,279,281,1,0,0,
        0,280,278,1,0,0,0,281,282,5,27,0,0,282,284,5,3,0,0,283,285,3,12,
        6,0,284,283,1,0,0,0,284,285,1,0,0,0,285,286,1,0,0,0,286,287,5,4,
        0,0,287,288,3,26,13,0,288,17,1,0,0,0,289,291,5,11,0,0,290,289,1,
        0,0,0,290,291,1,0,0,0,291,294,1,0,0,0,292,295,5,25,0,0,293,295,5,
        26,0,0,294,292,1,0,0,0,294,293,1,0,0,0,295,299,1,0,0,0,296,298,5,
        34,0,0,297,296,1,0,0,0,298,301,1,0,0,0,299,297,1,0,0,0,299,300,1,
        0,0,0,300,302,1,0,0,0,301,299,1,0,0,0,302,303,5,27,0,0,303,305,5,
        3,0,0,304,306,3,12,6,0,305,304,1,0,0,0,305,306,1,0,0,0,306,307,1,
        0,0,0,307,308,5,4,0,0,308,19,1,0,0,0,309,312,3,22,11,0,310,311,5,
        2,0,0,311,313,3,22,11,0,312,310,1,0,0,0,313,314,1,0,0,0,314,315,
        1,0,0,0,314,312,1,0,0,0,315,21,1,0,0,0,316,321,3,64,32,0,317,321,
        3,60,30,0,318,321,3,24,12,0,319,321,3,74,37,0,320,316,1,0,0,0,320,
        317,1,0,0,0,320,318,1,0,0,0,320,319,1,0,0,0,321,23,1,0,0,0,322,323,
        5,27,0,0,323,325,5,3,0,0,324,326,3,20,10,0,325,324,1,0,0,0,325,326,
        1,0,0,0,326,327,1,0,0,0,327,328,5,4,0,0,328,25,1,0,0,0,329,382,5,
        5,0,0,330,337,3,6,3,0,331,333,5,1,0,0,332,331,1,0,0,0,333,334,1,
        0,0,0,334,332,1,0,0,0,334,335,1,0,0,0,335,338,1,0,0,0,336,338,5,
        57,0,0,337,332,1,0,0,0,337,336,1,0,0,0,338,381,1,0,0,0,339,381,3,
        28,14,0,340,348,3,40,20,0,341,343,5,1,0,0,342,341,1,0,0,0,343,346,
        1,0,0,0,344,342,1,0,0,0,344,345,1,0,0,0,345,349,1,0,0,0,346,344,
        1,0,0,0,347,349,5,57,0,0,348,344,1,0,0,0,348,347,1,0,0,0,349,381,
        1,0,0,0,350,358,3,44,22,0,351,353,5,1,0,0,352,351,1,0,0,0,353,356,
        1,0,0,0,354,352,1,0,0,0,354,355,1,0,0,0,355,359,1,0,0,0,356,354,
        1,0,0,0,357,359,5,57,0,0,358,354,1,0,0,0,358,357,1,0,0,0,359,381,
        1,0,0,0,360,368,3,46,23,0,361,363,5,1,0,0,362,361,1,0,0,0,363,366,
        1,0,0,0,364,362,1,0,0,0,364,365,1,0,0,0,365,369,1,0,0,0,366,364,
        1,0,0,0,367,369,5,57,0,0,368,364,1,0,0,0,368,367,1,0,0,0,369,381,
        1,0,0,0,370,377,3,56,28,0,371,373,5,1,0,0,372,371,1,0,0,0,373,374,
        1,0,0,0,374,372,1,0,0,0,374,375,1,0,0,0,375,378,1,0,0,0,376,378,
        5,57,0,0,377,372,1,0,0,0,377,376,1,0,0,0,378,381,1,0,0,0,379,381,
        3,2,1,0,380,330,1,0,0,0,380,339,1,0,0,0,380,340,1,0,0,0,380,350,
        1,0,0,0,380,360,1,0,0,0,380,370,1,0,0,0,380,379,1,0,0,0,381,384,
        1,0,0,0,382,380,1,0,0,0,382,383,1,0,0,0,383,385,1,0,0,0,384,382,
        1,0,0,0,385,386,5,6,0,0,386,27,1,0,0,0,387,388,5,22,0,0,388,389,
        3,66,33,0,389,394,5,1,0,0,390,393,3,2,1,0,391,393,3,28,14,0,392,
        390,1,0,0,0,392,391,1,0,0,0,393,396,1,0,0,0,394,392,1,0,0,0,394,
        395,1,0,0,0,395,29,1,0,0,0,396,394,1,0,0,0,397,452,5,5,0,0,398,405,
        3,6,3,0,399,401,5,1,0,0,400,399,1,0,0,0,401,402,1,0,0,0,402,400,
        1,0,0,0,402,403,1,0,0,0,403,406,1,0,0,0,404,406,5,57,0,0,405,400,
        1,0,0,0,405,404,1,0,0,0,406,451,1,0,0,0,407,451,3,28,14,0,408,416,
        3,40,20,0,409,411,5,1,0,0,410,409,1,0,0,0,411,414,1,0,0,0,412,410,
        1,0,0,0,412,413,1,0,0,0,413,417,1,0,0,0,414,412,1,0,0,0,415,417,
        5,57,0,0,416,412,1,0,0,0,416,415,1,0,0,0,417,451,1,0,0,0,418,426,
        3,44,22,0,419,421,5,1,0,0,420,419,1,0,0,0,421,424,1,0,0,0,422,420,
        1,0,0,0,422,423,1,0,0,0,423,427,1,0,0,0,424,422,1,0,0,0,425,427,
        5,57,0,0,426,422,1,0,0,0,426,425,1,0,0,0,427,451,1,0,0,0,428,436,
        3,46,23,0,429,431,5,1,0,0,430,429,1,0,0,0,431,434,1,0,0,0,432,430,
        1,0,0,0,432,433,1,0,0,0,433,437,1,0,0,0,434,432,1,0,0,0,435,437,
        5,57,0,0,436,432,1,0,0,0,436,435,1,0,0,0,437,451,1,0,0,0,438,445,
        3,56,28,0,439,441,5,1,0,0,440,439,1,0,0,0,441,442,1,0,0,0,442,440,
        1,0,0,0,442,443,1,0,0,0,443,446,1,0,0,0,444,446,5,57,0,0,445,440,
        1,0,0,0,445,444,1,0,0,0,446,451,1,0,0,0,447,451,3,34,17,0,448,451,
        3,32,16,0,449,451,3,2,1,0,450,398,1,0,0,0,450,407,1,0,0,0,450,408,
        1,0,0,0,450,418,1,0,0,0,450,428,1,0,0,0,450,438,1,0,0,0,450,447,
        1,0,0,0,450,448,1,0,0,0,450,449,1,0,0,0,451,454,1,0,0,0,452,450,
        1,0,0,0,452,453,1,0,0,0,453,455,1,0,0,0,454,452,1,0,0,0,455,456,
        5,6,0,0,456,31,1,0,0,0,457,458,5,17,0,0,458,462,7,0,0,0,459,461,
        3,2,1,0,460,459,1,0,0,0,461,464,1,0,0,0,462,460,1,0,0,0,462,463,
        1,0,0,0,463,33,1,0,0,0,464,462,1,0,0,0,465,466,5,16,0,0,466,470,
        7,0,0,0,467,469,3,2,1,0,468,467,1,0,0,0,469,472,1,0,0,0,470,468,
        1,0,0,0,470,471,1,0,0,0,471,35,1,0,0,0,472,470,1,0,0,0,473,475,5,
        11,0,0,474,473,1,0,0,0,474,475,1,0,0,0,475,476,1,0,0,0,476,477,5,
        25,0,0,477,478,5,27,0,0,478,480,5,7,0,0,479,481,5,28,0,0,480,479,
        1,0,0,0,480,481,1,0,0,0,481,482,1,0,0,0,482,483,5,8,0,0,483,484,
        5,48,0,0,484,490,5,5,0,0,485,486,3,74,37,0,486,487,5,2,0,0,487,489,
        1,0,0,0,488,485,1,0,0,0,489,492,1,0,0,0,490,488,1,0,0,0,490,491,
        1,0,0,0,491,493,1,0,0,0,492,490,1,0,0,0,493,494,3,74,37,0,494,495,
        5,6,0,0,495,505,1,0,0,0,496,498,5,11,0,0,497,496,1,0,0,0,497,498,
        1,0,0,0,498,499,1,0,0,0,499,500,5,25,0,0,500,501,5,27,0,0,501,502,
        5,7,0,0,502,503,5,28,0,0,503,505,5,8,0,0,504,474,1,0,0,0,504,497,
        1,0,0,0,505,37,1,0,0,0,506,507,5,24,0,0,507,508,5,39,0,0,508,509,
        5,27,0,0,509,510,5,9,0,0,510,511,5,41,0,0,511,39,1,0,0,0,512,513,
        5,12,0,0,513,514,5,3,0,0,514,515,3,50,25,0,515,516,5,4,0,0,516,518,
        3,30,15,0,517,519,3,42,21,0,518,517,1,0,0,0,518,519,1,0,0,0,519,
        41,1,0,0,0,520,521,5,13,0,0,521,522,3,30,15,0,522,43,1,0,0,0,523,
        524,5,15,0,0,524,525,5,3,0,0,525,526,3,50,25,0,526,527,5,4,0,0,527,
        528,3,30,15,0,528,45,1,0,0,0,529,530,5,14,0,0,530,531,5,3,0,0,531,
        532,3,48,24,0,532,533,5,1,0,0,533,534,3,50,25,0,534,535,5,1,0,0,
        535,536,3,52,26,0,536,537,5,4,0,0,537,538,3,30,15,0,538,47,1,0,0,
        0,539,540,5,25,0,0,540,541,3,62,31,0,541,542,5,48,0,0,542,543,3,
        66,33,0,543,546,1,0,0,0,544,546,3,56,28,0,545,539,1,0,0,0,545,544,
        1,0,0,0,546,49,1,0,0,0,547,548,3,68,34,0,548,549,7,1,0,0,549,550,
        3,70,35,0,550,561,1,0,0,0,551,552,3,68,34,0,552,553,7,2,0,0,553,
        554,3,70,35,0,554,561,1,0,0,0,555,556,3,66,33,0,556,557,7,3,0,0,
        557,558,3,68,34,0,558,561,1,0,0,0,559,561,3,66,33,0,560,547,1,0,
        0,0,560,551,1,0,0,0,560,555,1,0,0,0,560,559,1,0,0,0,561,51,1,0,0,
        0,562,563,5,50,0,0,563,573,3,64,32,0,564,565,5,51,0,0,565,573,3,
        64,32,0,566,567,3,64,32,0,567,568,5,50,0,0,568,573,1,0,0,0,569,570,
        3,64,32,0,570,571,5,51,0,0,571,573,1,0,0,0,572,562,1,0,0,0,572,564,
        1,0,0,0,572,566,1,0,0,0,572,569,1,0,0,0,573,53,1,0,0,0,574,575,3,
        62,31,0,575,576,5,48,0,0,576,577,3,66,33,0,577,580,1,0,0,0,578,580,
        3,62,31,0,579,574,1,0,0,0,579,578,1,0,0,0,580,55,1,0,0,0,581,582,
        3,64,32,0,582,583,5,48,0,0,583,584,3,66,33,0,584,594,1,0,0,0,585,
        586,3,60,30,0,586,587,5,48,0,0,587,588,3,66,33,0,588,594,1,0,0,0,
        589,590,3,58,29,0,590,591,5,48,0,0,591,592,3,66,33,0,592,594,1,0,
        0,0,593,581,1,0,0,0,593,585,1,0,0,0,593,589,1,0,0,0,594,57,1,0,0,
        0,595,596,3,62,31,0,596,597,5,7,0,0,597,598,5,28,0,0,598,599,5,8,
        0,0,599,59,1,0,0,0,600,601,5,34,0,0,601,605,3,60,30,0,602,603,5,
        34,0,0,603,605,3,64,32,0,604,600,1,0,0,0,604,602,1,0,0,0,605,61,
        1,0,0,0,606,608,5,34,0,0,607,606,1,0,0,0,608,611,1,0,0,0,609,607,
        1,0,0,0,609,610,1,0,0,0,610,612,1,0,0,0,611,609,1,0,0,0,612,613,
        5,27,0,0,613,63,1,0,0,0,614,615,5,27,0,0,615,65,1,0,0,0,616,617,
        6,33,-1,0,617,618,3,68,34,0,618,630,1,0,0,0,619,620,10,3,0,0,620,
        621,5,37,0,0,621,629,3,68,34,0,622,623,10,2,0,0,623,624,5,38,0,0,
        624,629,3,68,34,0,625,626,10,1,0,0,626,627,7,3,0,0,627,629,3,68,
        34,0,628,619,1,0,0,0,628,622,1,0,0,0,628,625,1,0,0,0,629,632,1,0,
        0,0,630,628,1,0,0,0,630,631,1,0,0,0,631,67,1,0,0,0,632,630,1,0,0,
        0,633,634,6,34,-1,0,634,638,3,70,35,0,635,636,5,47,0,0,636,638,3,
        70,35,0,637,633,1,0,0,0,637,635,1,0,0,0,638,652,1,0,0,0,639,640,
        10,5,0,0,640,641,7,4,0,0,641,651,3,70,35,0,642,643,10,4,0,0,643,
        644,7,2,0,0,644,651,3,70,35,0,645,646,10,3,0,0,646,647,7,1,0,0,647,
        651,3,70,35,0,648,649,10,1,0,0,649,651,7,5,0,0,650,639,1,0,0,0,650,
        642,1,0,0,0,650,645,1,0,0,0,650,648,1,0,0,0,651,654,1,0,0,0,652,
        650,1,0,0,0,652,653,1,0,0,0,653,69,1,0,0,0,654,652,1,0,0,0,655,663,
        3,72,36,0,656,657,5,38,0,0,657,663,3,70,35,0,658,659,5,37,0,0,659,
        663,3,70,35,0,660,661,7,5,0,0,661,663,3,70,35,0,662,655,1,0,0,0,
        662,656,1,0,0,0,662,658,1,0,0,0,662,660,1,0,0,0,663,71,1,0,0,0,664,
        677,3,64,32,0,665,677,3,74,37,0,666,667,5,49,0,0,667,677,3,64,32,
        0,668,677,3,60,30,0,669,670,5,3,0,0,670,671,3,66,33,0,671,672,5,
        4,0,0,672,677,1,0,0,0,673,674,5,10,0,0,674,677,3,72,36,0,675,677,
        3,24,12,0,676,664,1,0,0,0,676,665,1,0,0,0,676,666,1,0,0,0,676,668,
        1,0,0,0,676,669,1,0,0,0,676,673,1,0,0,0,676,675,1,0,0,0,677,73,1,
        0,0,0,678,679,7,6,0,0,679,75,1,0,0,0,97,79,87,91,97,100,102,104,
        113,116,122,125,131,134,140,143,149,152,154,157,165,179,183,190,
        194,199,206,213,217,227,231,235,240,246,249,255,259,264,266,269,
        273,278,284,290,294,299,305,314,320,325,334,337,344,348,354,358,
        364,368,374,377,380,382,392,394,402,405,412,416,422,426,432,436,
        442,445,450,452,462,470,474,480,490,497,504,518,545,560,572,579,
        593,604,609,628,630,637,650,652,662,676
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
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 4081818781355016) != 0:
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
                    if token in [-1, 1, 3, 10, 11, 23, 25, 26, 27, 28, 29, 30, 34, 37, 38, 47, 49, 50, 51]:
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
            self.state = 154
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
            self.state = 157
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 156
                self.match(MathParser.CONST)


            self.state = 159
            self.match(MathParser.TYPE)
            self.state = 165
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 160
                    self.var_decl()
                    self.state = 161
                    self.match(MathParser.T__1) 
                self.state = 167
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

            self.state = 168
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
            self.state = 194
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 170
                self.match(MathParser.PRINTF)
                self.state = 171
                self.match(MathParser.T__2)
                self.state = 172
                localctx.format_string = self.match(MathParser.FORMAT_STRING)
                self.state = 183
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==2:
                    self.state = 173
                    self.match(MathParser.T__1)
                    self.state = 179
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt==1:
                            self.state = 174
                            localctx._printf_arg = self.printf_arg()
                            localctx.vars_.append(localctx._printf_arg)
                            self.state = 175
                            self.match(MathParser.T__1) 
                        self.state = 181
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

                    self.state = 182
                    localctx._printf_arg = self.printf_arg()
                    localctx.vars_.append(localctx._printf_arg)


                self.state = 185
                self.match(MathParser.T__3)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 186
                self.match(MathParser.PRINTF)
                self.state = 187
                self.match(MathParser.T__2)
                self.state = 190
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [27]:
                    self.state = 188
                    self.rvar()
                    pass
                elif token in [28, 29, 30]:
                    self.state = 189
                    self.rtype()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 192
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
            self.state = 199
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [27]:
                self.enterOuterAlt(localctx, 1)
                self.state = 196
                self.rvar()
                pass
            elif token in [28, 29, 30]:
                self.enterOuterAlt(localctx, 2)
                self.state = 197
                self.rtype()
                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 3)
                self.state = 198
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
            self.state = 201
            self.match(MathParser.SCANF)
            self.state = 202
            self.match(MathParser.T__2)
            self.state = 203
            localctx.format_string = self.match(MathParser.FORMAT_STRING)
            self.state = 204
            self.match(MathParser.T__1)
            self.state = 213
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 206
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==49:
                        self.state = 205
                        self.match(MathParser.ADDR)


                    self.state = 208
                    localctx._rvar = self.rvar()
                    localctx.vars_.append(localctx._rvar)
                    self.state = 209
                    self.match(MathParser.T__1) 
                self.state = 215
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

            self.state = 217
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==49:
                self.state = 216
                self.match(MathParser.ADDR)


            self.state = 219
            localctx._rvar = self.rvar()
            localctx.vars_.append(localctx._rvar)
            self.state = 220
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
            self.state = 222
            localctx._param_declr = self.param_declr()
            localctx.params.append(localctx._param_declr)
            self.state = 227
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 223
                self.match(MathParser.T__1)
                self.state = 224
                localctx._param_declr = self.param_declr()
                localctx.params.append(localctx._param_declr)
                self.state = 229
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
            self.state = 266
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 231
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==11:
                    self.state = 230
                    localctx.const = self.match(MathParser.CONST)


                self.state = 233
                localctx.type_ = self.match(MathParser.TYPE)
                self.state = 235
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==49:
                    self.state = 234
                    localctx.reference = self.match(MathParser.ADDR)


                self.state = 240
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==34:
                    self.state = 237
                    localctx._STR = self.match(MathParser.STR)
                    localctx.ptr.append(localctx._STR)
                    self.state = 242
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 243
                localctx.var = self.match(MathParser.VAR_NAME)
                self.state = 246
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==48:
                    self.state = 244
                    self.match(MathParser.ASSIGN)
                    self.state = 245
                    localctx.default = self.expr(0)


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 249
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==11:
                    self.state = 248
                    localctx.const = self.match(MathParser.CONST)


                self.state = 251
                localctx.type_ = self.match(MathParser.TYPE)
                self.state = 255
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==34:
                    self.state = 252
                    localctx._STR = self.match(MathParser.STR)
                    localctx.ptr.append(localctx._STR)
                    self.state = 257
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 259
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==49:
                    self.state = 258
                    localctx.reference = self.match(MathParser.ADDR)


                self.state = 261
                localctx.var = self.match(MathParser.VAR_NAME)
                self.state = 264
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==48:
                    self.state = 262
                    self.match(MathParser.ASSIGN)
                    self.state = 263
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
            self.state = 269
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 268
                localctx.const = self.match(MathParser.CONST)


            self.state = 273
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [25]:
                self.state = 271
                localctx.type_ = self.match(MathParser.TYPE)
                pass
            elif token in [26]:
                self.state = 272
                localctx.type_ = self.match(MathParser.VOID)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 278
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==34:
                self.state = 275
                localctx._STR = self.match(MathParser.STR)
                localctx.ptr.append(localctx._STR)
                self.state = 280
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 281
            localctx.name = self.match(MathParser.VAR_NAME)
            self.state = 282
            self.match(MathParser.T__2)
            self.state = 284
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11 or _la==25:
                self.state = 283
                localctx.params = self.param_list()


            self.state = 286
            self.match(MathParser.T__3)
            self.state = 287
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
            self.state = 290
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 289
                localctx.const = self.match(MathParser.CONST)


            self.state = 294
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [25]:
                self.state = 292
                localctx.type_ = self.match(MathParser.TYPE)
                pass
            elif token in [26]:
                self.state = 293
                localctx.type_ = self.match(MathParser.VOID)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 299
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==34:
                self.state = 296
                localctx._STR = self.match(MathParser.STR)
                localctx.ptr.append(localctx._STR)
                self.state = 301
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 302
            localctx.name = self.match(MathParser.VAR_NAME)
            self.state = 303
            self.match(MathParser.T__2)
            self.state = 305
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11 or _la==25:
                self.state = 304
                localctx.params = self.param_list()


            self.state = 307
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
            self.state = 309
            localctx._func_arg = self.func_arg()
            localctx.args.append(localctx._func_arg)
            self.state = 312 
            self._errHandler.sync(self)
            _alt = 1+1
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1+1:
                    self.state = 310
                    self.match(MathParser.T__1)
                    self.state = 311
                    localctx._func_arg = self.func_arg()
                    localctx.args.append(localctx._func_arg)

                else:
                    raise NoViableAltException(self)
                self.state = 314 
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
            self.state = 320
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 316
                self.rvar()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 317
                self.deref()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 318
                self.func_call()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 319
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
            self.state = 322
            localctx.name = self.match(MathParser.VAR_NAME)
            self.state = 323
            self.match(MathParser.T__2)
            self.state = 325
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 19193135104) != 0:
                self.state = 324
                localctx.args = self.arg_list()


            self.state = 327
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
            self.state = 329
            self.match(MathParser.T__4)
            self.state = 382
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 4081818720590856) != 0:
                self.state = 380
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,59,self._ctx)
                if la_ == 1:
                    self.state = 330
                    self.printf()
                    self.state = 337
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [1]:
                        self.state = 332 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while True:
                            self.state = 331
                            self.match(MathParser.T__0)
                            self.state = 334 
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            if not (_la==1):
                                break

                        pass
                    elif token in [57]:
                        self.state = 336
                        self.match(MathParser.DELIM)
                        pass
                    else:
                        raise NoViableAltException(self)

                    pass

                elif la_ == 2:
                    self.state = 339
                    self.return_instr()
                    pass

                elif la_ == 3:
                    self.state = 340
                    self.if_cond()
                    self.state = 348
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [1, 3, 6, 10, 11, 12, 14, 15, 21, 22, 23, 25, 27, 28, 29, 30, 34, 37, 38, 47, 49, 50, 51]:
                        self.state = 344
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==1:
                            self.state = 341
                            self.match(MathParser.T__0)
                            self.state = 346
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        pass
                    elif token in [57]:
                        self.state = 347
                        self.match(MathParser.DELIM)
                        pass
                    else:
                        raise NoViableAltException(self)

                    pass

                elif la_ == 4:
                    self.state = 350
                    self.while_loop()
                    self.state = 358
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [1, 3, 6, 10, 11, 12, 14, 15, 21, 22, 23, 25, 27, 28, 29, 30, 34, 37, 38, 47, 49, 50, 51]:
                        self.state = 354
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==1:
                            self.state = 351
                            self.match(MathParser.T__0)
                            self.state = 356
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        pass
                    elif token in [57]:
                        self.state = 357
                        self.match(MathParser.DELIM)
                        pass
                    else:
                        raise NoViableAltException(self)

                    pass

                elif la_ == 5:
                    self.state = 360
                    self.for_loop()
                    self.state = 368
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [1, 3, 6, 10, 11, 12, 14, 15, 21, 22, 23, 25, 27, 28, 29, 30, 34, 37, 38, 47, 49, 50, 51]:
                        self.state = 364
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==1:
                            self.state = 361
                            self.match(MathParser.T__0)
                            self.state = 366
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        pass
                    elif token in [57]:
                        self.state = 367
                        self.match(MathParser.DELIM)
                        pass
                    else:
                        raise NoViableAltException(self)

                    pass

                elif la_ == 6:
                    self.state = 370
                    self.assign()
                    self.state = 377
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [1]:
                        self.state = 372 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while True:
                            self.state = 371
                            self.match(MathParser.T__0)
                            self.state = 374 
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            if not (_la==1):
                                break

                        pass
                    elif token in [57]:
                        self.state = 376
                        self.match(MathParser.DELIM)
                        pass
                    else:
                        raise NoViableAltException(self)

                    pass

                elif la_ == 7:
                    self.state = 379
                    self.instr()
                    pass


                self.state = 384
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 385
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
            self.state = 387
            self.match(MathParser.RETURN)

            self.state = 388
            self.expr(0)
            self.state = 389
            self.match(MathParser.T__0)
            self.state = 394
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,62,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 392
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [3, 10, 11, 23, 25, 27, 28, 29, 30, 34, 37, 38, 47, 49, 50, 51]:
                        self.state = 390
                        self.instr()
                        pass
                    elif token in [22]:
                        self.state = 391
                        self.return_instr()
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 396
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
            self.state = 397
            self.match(MathParser.T__4)
            self.state = 452
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 4081818720787464) != 0:
                self.state = 450
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,73,self._ctx)
                if la_ == 1:
                    self.state = 398
                    self.printf()
                    self.state = 405
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [1]:
                        self.state = 400 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while True:
                            self.state = 399
                            self.match(MathParser.T__0)
                            self.state = 402 
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            if not (_la==1):
                                break

                        pass
                    elif token in [57]:
                        self.state = 404
                        self.match(MathParser.DELIM)
                        pass
                    else:
                        raise NoViableAltException(self)

                    pass

                elif la_ == 2:
                    self.state = 407
                    self.return_instr()
                    pass

                elif la_ == 3:
                    self.state = 408
                    self.if_cond()
                    self.state = 416
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [1, 3, 6, 10, 11, 12, 14, 15, 16, 17, 21, 22, 23, 25, 27, 28, 29, 30, 34, 37, 38, 47, 49, 50, 51]:
                        self.state = 412
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==1:
                            self.state = 409
                            self.match(MathParser.T__0)
                            self.state = 414
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        pass
                    elif token in [57]:
                        self.state = 415
                        self.match(MathParser.DELIM)
                        pass
                    else:
                        raise NoViableAltException(self)

                    pass

                elif la_ == 4:
                    self.state = 418
                    self.while_loop()
                    self.state = 426
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [1, 3, 6, 10, 11, 12, 14, 15, 16, 17, 21, 22, 23, 25, 27, 28, 29, 30, 34, 37, 38, 47, 49, 50, 51]:
                        self.state = 422
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==1:
                            self.state = 419
                            self.match(MathParser.T__0)
                            self.state = 424
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        pass
                    elif token in [57]:
                        self.state = 425
                        self.match(MathParser.DELIM)
                        pass
                    else:
                        raise NoViableAltException(self)

                    pass

                elif la_ == 5:
                    self.state = 428
                    self.for_loop()
                    self.state = 436
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [1, 3, 6, 10, 11, 12, 14, 15, 16, 17, 21, 22, 23, 25, 27, 28, 29, 30, 34, 37, 38, 47, 49, 50, 51]:
                        self.state = 432
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==1:
                            self.state = 429
                            self.match(MathParser.T__0)
                            self.state = 434
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        pass
                    elif token in [57]:
                        self.state = 435
                        self.match(MathParser.DELIM)
                        pass
                    else:
                        raise NoViableAltException(self)

                    pass

                elif la_ == 6:
                    self.state = 438
                    self.assign()
                    self.state = 445
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [1]:
                        self.state = 440 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while True:
                            self.state = 439
                            self.match(MathParser.T__0)
                            self.state = 442 
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            if not (_la==1):
                                break

                        pass
                    elif token in [57]:
                        self.state = 444
                        self.match(MathParser.DELIM)
                        pass
                    else:
                        raise NoViableAltException(self)

                    pass

                elif la_ == 7:
                    self.state = 447
                    self.break_instr()
                    pass

                elif la_ == 8:
                    self.state = 448
                    self.cont_instr()
                    pass

                elif la_ == 9:
                    self.state = 449
                    self.instr()
                    pass


                self.state = 454
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 455
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
            self.state = 457
            self.match(MathParser.CONTINUE)
            self.state = 458
            _la = self._input.LA(1)
            if not(_la==1 or _la==57):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 462
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,75,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 459
                    self.instr() 
                self.state = 464
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
            self.state = 465
            self.match(MathParser.BREAK)
            self.state = 466
            _la = self._input.LA(1)
            if not(_la==1 or _la==57):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 470
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,76,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 467
                    self.instr() 
                self.state = 472
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
            self.state = 504
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,81,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 474
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==11:
                    self.state = 473
                    localctx.const = self.match(MathParser.CONST)


                self.state = 476
                localctx.type_ = self.match(MathParser.TYPE)
                self.state = 477
                localctx.name = self.match(MathParser.VAR_NAME)
                self.state = 478
                self.match(MathParser.T__6)
                self.state = 480
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==28:
                    self.state = 479
                    localctx.size = self.match(MathParser.INT)


                self.state = 482
                self.match(MathParser.T__7)
                self.state = 483
                self.match(MathParser.ASSIGN)
                self.state = 484
                self.match(MathParser.T__4)
                self.state = 490
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,79,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 485
                        localctx._rtype = self.rtype()
                        localctx.values.append(localctx._rtype)
                        self.state = 486
                        self.match(MathParser.T__1) 
                    self.state = 492
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,79,self._ctx)

                self.state = 493
                localctx._rtype = self.rtype()
                localctx.values.append(localctx._rtype)
                self.state = 494
                self.match(MathParser.T__5)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 497
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==11:
                    self.state = 496
                    localctx.const = self.match(MathParser.CONST)


                self.state = 499
                localctx.type_ = self.match(MathParser.TYPE)
                self.state = 500
                localctx.name = self.match(MathParser.VAR_NAME)
                self.state = 501
                self.match(MathParser.T__6)
                self.state = 502
                localctx.size = self.match(MathParser.INT)
                self.state = 503
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
            self.state = 506
            self.match(MathParser.INCLUDE)
            self.state = 507
            self.match(MathParser.LT)
            self.state = 508
            localctx.library = self.match(MathParser.VAR_NAME)
            self.state = 509
            self.match(MathParser.T__8)
            self.state = 510
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
            self.state = 512
            self.match(MathParser.IF)
            self.state = 513
            self.match(MathParser.T__2)
            self.state = 514
            localctx.condition = self.cond()
            self.state = 515
            self.match(MathParser.T__3)
            self.state = 516
            self.scope()
            self.state = 518
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 517
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
            self.state = 520
            self.match(MathParser.ELSE)
            self.state = 521
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
            self.state = 523
            self.match(MathParser.WHILE)
            self.state = 524
            self.match(MathParser.T__2)
            self.state = 525
            localctx.condition = self.cond()
            self.state = 526
            self.match(MathParser.T__3)
            self.state = 527
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
            self.state = 529
            self.match(MathParser.FOR)
            self.state = 530
            self.match(MathParser.T__2)
            self.state = 531
            localctx.initialization = self.init()
            self.state = 532
            self.match(MathParser.T__0)
            self.state = 533
            localctx.condition = self.cond()
            self.state = 534
            self.match(MathParser.T__0)
            self.state = 535
            localctx.increment = self.incr()
            self.state = 536
            self.match(MathParser.T__3)
            self.state = 537
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
            self.state = 545
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [25]:
                self.enterOuterAlt(localctx, 1)
                self.state = 539
                self.match(MathParser.TYPE)
                self.state = 540
                self.lvar()
                self.state = 541
                self.match(MathParser.ASSIGN)
                self.state = 542
                self.expr(0)
                pass
            elif token in [27, 34]:
                self.enterOuterAlt(localctx, 2)
                self.state = 544
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
            self.state = 560
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,84,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 547
                self.term(0)
                self.state = 548
                _la = self._input.LA(1)
                if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 23089744183296) != 0):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 549
                self.factor()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 551
                self.term(0)
                self.state = 552
                _la = self._input.LA(1)
                if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 11544872091648) != 0):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 553
                self.factor()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 555
                self.expr(0)
                self.state = 556
                _la = self._input.LA(1)
                if not(_la==45 or _la==46):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 557
                self.term(0)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 559
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
            self.state = 572
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,85,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 562
                self.match(MathParser.INCR)
                self.state = 563
                self.rvar()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 564
                self.match(MathParser.DECR)
                self.state = 565
                self.rvar()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 566
                self.rvar()
                self.state = 567
                self.match(MathParser.INCR)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 569
                self.rvar()
                self.state = 570
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
            self.state = 579
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,86,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 574
                self.lvar()
                self.state = 575
                self.match(MathParser.ASSIGN)
                self.state = 576
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 578
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
            self.state = 593
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,87,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 581
                self.rvar()
                self.state = 582
                self.match(MathParser.ASSIGN)
                self.state = 583
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 585
                self.deref()
                self.state = 586
                self.match(MathParser.ASSIGN)
                self.state = 587
                self.expr(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 589
                self.array_el()
                self.state = 590
                self.match(MathParser.ASSIGN)
                self.state = 591
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
            self.state = 595
            self.lvar()
            self.state = 596
            self.match(MathParser.T__6)
            self.state = 597
            self.match(MathParser.INT)
            self.state = 598
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
            self.state = 604
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,88,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 600
                self.match(MathParser.STR)
                self.state = 601
                self.deref()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 602
                self.match(MathParser.STR)
                self.state = 603
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
            self.state = 609
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==34:
                self.state = 606
                localctx._STR = self.match(MathParser.STR)
                localctx.ptr.append(localctx._STR)
                self.state = 611
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 612
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
            self.state = 614
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
            self.state = 617
            self.term(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 630
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,91,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 628
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,90,self._ctx)
                    if la_ == 1:
                        localctx = MathParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 619
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 620
                        self.match(MathParser.SUM)
                        self.state = 621
                        self.term(0)
                        pass

                    elif la_ == 2:
                        localctx = MathParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 622
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 623
                        self.match(MathParser.DIF)
                        self.state = 624
                        self.term(0)
                        pass

                    elif la_ == 3:
                        localctx = MathParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 625
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 626
                        _la = self._input.LA(1)
                        if not(_la==45 or _la==46):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 627
                        self.term(0)
                        pass

             
                self.state = 632
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
            self.state = 637
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 10, 27, 28, 29, 30, 34, 37, 38, 49, 50, 51]:
                self.state = 634
                self.factor()
                pass
            elif token in [47]:
                self.state = 635
                self.match(MathParser.NOT_OP)
                self.state = 636
                self.factor()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 652
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,94,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 650
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,93,self._ctx)
                    if la_ == 1:
                        localctx = MathParser.TermContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 639
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 640
                        _la = self._input.LA(1)
                        if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 120259084288) != 0):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 641
                        self.factor()
                        pass

                    elif la_ == 2:
                        localctx = MathParser.TermContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 642
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 643
                        _la = self._input.LA(1)
                        if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 11544872091648) != 0):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 644
                        self.factor()
                        pass

                    elif la_ == 3:
                        localctx = MathParser.TermContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 645
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 646
                        _la = self._input.LA(1)
                        if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 23089744183296) != 0):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 647
                        self.factor()
                        pass

                    elif la_ == 4:
                        localctx = MathParser.TermContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 648
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 649
                        _la = self._input.LA(1)
                        if not(_la==50 or _la==51):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        pass

             
                self.state = 654
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
            self.state = 662
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 10, 27, 28, 29, 30, 34, 49]:
                self.enterOuterAlt(localctx, 1)
                self.state = 655
                self.primary()
                pass
            elif token in [38]:
                self.enterOuterAlt(localctx, 2)
                self.state = 656
                self.match(MathParser.DIF)
                self.state = 657
                self.factor()
                pass
            elif token in [37]:
                self.enterOuterAlt(localctx, 3)
                self.state = 658
                self.match(MathParser.SUM)
                self.state = 659
                self.factor()
                pass
            elif token in [50, 51]:
                self.enterOuterAlt(localctx, 4)
                self.state = 660
                _la = self._input.LA(1)
                if not(_la==50 or _la==51):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 661
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
            self.state = 676
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,96,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 664
                self.rvar()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 665
                self.rtype()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 666
                self.match(MathParser.ADDR)
                self.state = 667
                self.rvar()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 668
                self.deref()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 669
                self.match(MathParser.T__2)
                self.state = 670
                self.expr(0)
                self.state = 671
                self.match(MathParser.T__3)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 673
                self.match(MathParser.CAST)
                self.state = 674
                self.primary()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 675
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
            self.state = 678
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
         




