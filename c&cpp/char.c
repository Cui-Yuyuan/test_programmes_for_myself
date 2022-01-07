#include<stdio.h>
 int main(void)
 {
    unsigned char i;
    for(i=0;i<=255;i++)
        printf("%d:%c;%x:%c;%o:%c",i,i,i,i,i,i);
    return 0;
    }
