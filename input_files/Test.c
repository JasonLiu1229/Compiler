int x = 3;
float y = 3.14;
printf(y); // 3.14
x++;
printf(x); // 4
int* ptr1 = &x;
*ptr1 = 5;
printf(*ptr1); // 5