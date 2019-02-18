#include <stdio.h>
int main()
{
int var=0,A,D;
float N;
scanf("%f%d%d",&N,&A,&D);
var=(N/2)*(2*A+(N-1)*D);
printf("%d\n",var);
return 0;
}
