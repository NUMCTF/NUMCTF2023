#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void win() {
    system("/bin/sh");
}

void fusion(int length) {
    char buffer [128];
    short size = length;
    puts("Enter your Second person: ");
    fgets(buffer, size, stdin);
    buffer[strcspn(buffer, "\n")] = '\0';
    return;
}

int main() {
    int input_length = 128;
    char input_buffer[128];

    puts("Welcome to the Over Fusion challenge!\n");
    puts("Enter your first person: ");
    gets(input_buffer);
    input_buffer[strcspn(input_buffer, "\n")] = '\0';
    
    // puts(input_length);
    if (input_length > 128){
        puts("Fusion over failed!\n");
        exit(0);
    }

    fusion(input_length);

    puts("Fusion over completed!");
    exit(0);
}

__attribute__((constructor)) void setup(){
	setbuf(stdin, NULL);
	setbuf(stdout, NULL);
	setbuf(stderr, NULL);
}