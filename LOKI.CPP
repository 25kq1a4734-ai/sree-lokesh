#include<stdio.h>
#include<conio.h>
void main()
{
int a,b,c,sum,subtraction,multiply,division;
clrscr();
scanf("%d%d",&a,&b);
c=a+b;
printf("%d\n",c,sum);
scanf("%d%d",&a,&b);
c=a-b;
printf("%d\n",c,subtraction);
scanf("%d%d",&a,&b);
c=a*b;
printf("%d\n",c,multiply);
scanf("%d%d",&a,&b);
c=a/b;
printf("%d\n",c,division);
printf("%d%d%d%d",&sum,&subtraction,&multiply,&division);
getch();
}