#include <stdio.h>

int main(void)
{
	int a,b,even;
	scanf("%d%d",&a,&b);
	for(even=a+1;even<=b-1;even++)
	{
	if(even%2==0)
            printf("%d ",even);
	}
	return 0;
}
