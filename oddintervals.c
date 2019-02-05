#include <stdio.h>

int main(void)
{
	int a,b,z;
	scanf("%d%d",&a,&b);
	for(z=a+1;z<=b;z++)
	{
	if(z%2!=0)
            printf("%d ",z);
	}
	return 0;
}
