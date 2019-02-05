#include <stdio.h>

int main(void)
{
	int a,b,odd;
	scanf("%d%d",&a,&b);
	for(odd=a+1;odd<=b;odd++)
	{
	if(odd%2!=0)
            printf("%d ",odd);
	}
	return 0;
}
