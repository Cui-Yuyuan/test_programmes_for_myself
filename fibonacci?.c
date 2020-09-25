include<stdio.h>
 int main()
 {
 	long long int f1=1,f2=2;
 	int i;
 	for(i=1;i<=35;i++)
 	{
	 printf("%30lld %30lld",f1,f2);
	 if(i%2==0) printf("\n");
	 f1=f1+f2;
	 f2=f2+f1;}
   return 0;
//notice:
//the program cones from a book 
//just ignore what I said  
}
