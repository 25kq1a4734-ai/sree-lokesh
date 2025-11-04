#include<stdio.h>
#include<conio.h>
void main()
{
int a=12,b=-100;
clrscr();
printf("%d",~b);

getch();
}