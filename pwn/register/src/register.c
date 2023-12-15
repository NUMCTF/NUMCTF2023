#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <stdio.h>
#include <sys/types.h>

__attribute__((constructor)) void setup(){
	setbuf(stdin, NULL);
	setbuf(stdout, NULL);
	setbuf(stderr, NULL);
}

struct User {
    char Username[50];
    char Password[30];
    void (*displayInfo)();
};

struct User users[30];
int numUsers = 0;  // Variable to keep track of the number of registered users
void win(){
    system("/bin/sh");
}

void displayUserInfo() {
    printf("Welcome\n");
}

void action() {
    printf("1. Login\n");
    printf("2. Register\n");
    printf("3. Exit\n");
}

int findUser(const char *username) {
    for (int i = 0; i < numUsers; ++i) {
        if (strcmp(users[i].Username, username) == 0) {
            return i;  // Return the index of the user if found
        }
    }
    return -1;  // Return -1 if the user is not found
}

void login(struct User *user) {
     char temp[70];

    printf("Enter username: ");
    scanf("%s", temp);
    strcpy(user->Username,temp);

    int userIndex = findUser(user->Username);

    if (userIndex != -1) {
        printf("Enter password: ");
        scanf("%s", temp);

        if (strcmp(users[userIndex].Password, user->Password) == 0) {
            printf("Login successful!\n");
            users[userIndex].displayInfo();

        } else {
            printf("Incorrect password. Login failed.\n");
        }
    } else {
        printf("User not found. Please register.\n");
    }
}

void registerUser(struct User *user) {
    if (numUsers < 30) {
        printf("Enter username: ");
        char temp[50];
        user->displayInfo = &displayUserInfo;
        scanf("%s", &temp);

        strcpy(user->Username,temp);
        
        printf("Enter password: ");
        scanf("%s", &temp);
        strcpy(user->Password,temp);
        
        users[numUsers] = *user;
        // users[numUsers].displayInfo = displayUserInfo;

        users[numUsers].displayInfo();

        printf("Registration successful!\n");

        numUsers++;
    } else {
        printf("Maximum number of users reached. Cannot register more users.\n");
    }
}

int main() {
    printf("Welcome to the User Registration and Login System\n");

    int choice;
    struct User *user;
    user = malloc(sizeof(struct User));
    do {
        action();
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                login(user);
                break;
            case 2:
                registerUser(user);
                break;
            case 3:
                printf("Exiting the system. Goodbye!\n");
                break;
            default:
                printf("Invalid choice. Please enter a valid option.\n");
        }

    } while (choice != 3);

    return 0;
}
