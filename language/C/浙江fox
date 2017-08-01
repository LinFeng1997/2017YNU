#include <stdio.h>
#include <stdlib.h>
#include <time.h> 

int main()

{ double start,finish,cost;
    start=clock();
  int len=10000;
  int i=0,nums[len];
   srand((unsigned) time(NULL)); 
   for (i=0; i<len; i++)
   {
     nums[i] = rand(); 
   }   
   
   int a,b,temp;
   for (a=0;a<len-1;a++)
   {
   	for (b=0;b<len-1-a;b++)
   	{
   		if (nums[b]>nums[b+1])
   		{
   			temp=nums[b];
   			nums[b]=nums[b+1];
   			nums[b+1]=temp;
		   }
	   }
   }
   
   for (i=0;i<len;i++)
   {
   	printf("%d\n",nums[i]);
   }
   finish=clock();
   cost=finish-start;
   printf("所花费的时间为：%.2f 毫秒\n",cost);

   return 0;
}
