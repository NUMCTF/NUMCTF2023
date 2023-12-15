#include <stdio.h>
#include <stdlib.h>

__attribute__((constructor)) void setup(){
	setbuf(stdin, NULL);
	setbuf(stdout, NULL);
	setbuf(stderr, NULL);
    __asm__("pop %rdi;ret;");
}

void make_pie(){
    char entrance[0xff];
    printf("What is your recipe?\n");
    gets(entrance);
    printf("Please wait for a moment\n");
    printf("Get ready your pie. This pie has:\n");
    printf(entrance);
    printf("\nIs it delicious\n");
    gets(entrance);
    printf("Thank you\n");
}

int main(){
    make_pie();
}