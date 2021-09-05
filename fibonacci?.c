include<stdio.h>
 int main()
 {
 	unsigned long long int f1=1,f2=2;
 	int i;
 	for(i=1;i<=35;i++)
 	{
	 printf("%30lld %30lld",f1,f2);
	 f1=f1+f2;
	 f2=f2+f1;}
   return 0;
//notice:
//here is just a possible way.i have written
//another programme which also works.
//the program comes from a book 
//just ignore what I said 
}
