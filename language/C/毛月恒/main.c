#include<stdio.h>
#include<stdlib.h>

int main ()
{
 int i,j,a[10000],n=0;
 for(i=0;i<10000;i++)
 a[i] = rand()%1000+1;
 for(i=0;i<10000;i++)
 {
 for(j=i+1;j<10000;j++)
 {
 if(a[i]>a[j])
 {
 int temp=a[i];
 a[i]=a[j];
 a[j]=temp;
 n++;
 }
 }
 if(i%15==0)
 printf("\n");
 printf("%d ",a[i]);
 }
 return 0;
}
