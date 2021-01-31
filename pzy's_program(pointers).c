#include<stdio.h>
 int main(void)
 {
    u[5]={100,200,300,400,500};
    *ptr1,*ptr2,*ptr3;
    ptr1=u;
    ptr2=&u[2];
    ptr3=ptr1+4
    printf("ptrval,dereferencedptr,ptradd:");
    printf("ptr1=%p,*ptr1=%d,&ptr1=%p\n",ptr1,*ptr1,&ptr1);
    printf("add an interger to a pointer");
    printf("ptr1+4=%p,*(ptr1+4)=%d,ptr1+4,*(ptr1+4"));
    ptr1++;
    printf("\nvalues after ptr1++:");
    printf("ptr1=%p,*ptr1=%d,&ptr1=%p\n",ptr2,*ptr2,&ptr2);
    ptr2--;
    printf("\nvalues after ptr2--:");
    printf("ptr2=%p,*ptr2=%d,&ptr2=%p\n",ptr2,*ptr2,&ptr2);
    --ptr1;
    ++ptr2;
    //here is some problems so something has been removed
    printf("ptr2=%p,ptr1=%p,ptr2-ptr1=%td\n",ptr2,ptr1,ptr2-ptr1);
    printf("ptr3=%p,,ptr3-2=%p\n",ptr3,ptr3-2);
    return 0;
   }
