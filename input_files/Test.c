int x = 1;
float y = 3.14;
printf(y);
x++;
printf(x);
int* ptr1 = &x;
*ptr1 = 5;
printf(x);