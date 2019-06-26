
#include <stdio.h>


void foo(int k)
{
    if(k > 3)
    {
        printf("Greater\n");
    }
    else if(k <= 3)
    {
        printf("Less");
    }
    else
    {
        printf("Neither");
    }
    if(false) {
        printf("Logic failure.\n");
    }
}

