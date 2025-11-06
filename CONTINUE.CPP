#include<stdio.h>
#include<conio.h>
void main()
{
int i=0;
clrscr();
while(i>1)
{
i++;
if(i==3)
{
continue;
}
printf("%d\n",i);
}
getch();
}