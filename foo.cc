
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

void bar(int k)
{
    if(k > 3)
    {
        printf("Greater\n");
    }
    else if(k > 4)
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

void baz(int k)
{
    if(k > 3)
    {
        printf("Greater\n");
    }
    else if(k < 2 || k < 1)
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

