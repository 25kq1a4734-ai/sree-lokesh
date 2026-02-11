#include<stdio.h>
#include<conio.h>
#include<stdlib.h>
struct node
{
int data;
struct node* next;
};
struct node* head;
void insert_node(int data)
{
struct node* newnode=(struct node*)malloc(sizeof(struct node));
newnode->data=data;
newnode->next=head;
head=newnode;
}
void reverse()
{
struct node*prev,*next,*current;
current=head;
while(current!=NULL)
{
next=current->next;
current->next=prev;
prev=current;
current=next;
}
head=prev;
}
void print()
{
struct node* p;
p=head;
while(p !=NULL)
{
printf("%d\n",p->data);
p=p->next;
}
printf("\n");
}
void main()
{
head=NULL;
insert_node(2);
insert_node(4);
insert_node(6);
clrscr();
printf("linked list before calling reverse\n");
print();
reverse();
printf("linked list after calling reverse\n");
print();
getch();
}
