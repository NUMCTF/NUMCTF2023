#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/ptrace.h>

__attribute__((constructor)) void _INIT_0() {
    if (ptrace(PTRACE_TRACEME, 0, 1, 0) == -1) {
        printf("Welcome to the reverse engineering challenge!\n");
        exit(1);
    }
}
char flag[] = {0x5e,0x68,0x58,0x44,0x6c,0x4e,0x34,0x22,0x8,0x4,0x58,0x6c,0x1e,0x0,0x6c,0x52,0x7a,0x60,0x6,0x1e,0x2c,0x68,0x76,0x76,0x7e,0x6c,0x5e,0x36,0x3c,0x52,0x40,0xa,0x54,0x38,0xffffffc2};
char key[] = "aaaabaaacaaadaaaeaaafaaagaaahaaaiaaaja";

void FUN_00401277(char *input, char *key, int length) {
    for (int i = 0; i < length; i++) {
        input[i] = input[i] ^ key[i % strlen(key)];
        input[i] = (input[i] << 1) | (input[i] >> 7);
    }
}

void FUN_0040139e(char *input, char *key, int length) {
    for (int i = 0; i < length; i++) {
        input[i] = (input[i] >> 1) | (input[i] << 7);
        input[i] = input[i] ^ key[i % strlen(key)]%256;
    }
}

void FUN_0040135b(){
    FUN_0040139e(flag,key,sizeof(flag));
    printf("%s",flag);
}

int check(char *input, char *key, int length){
    for (int i = 0; i < length && i<sizeof(flag); i++) {
        input[i] = input[i] ^ key[i % strlen(key)];
        input[i] = (input[i] << 1) | (input[i] >> 7);
        if ((int)input[i]!=flag[i]) return 0;
    }
    return 1;
}

int main() {
    printf("Welcome to the reverse engineering challenge main!\n");
    return 0;
}