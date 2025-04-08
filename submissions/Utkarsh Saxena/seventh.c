#include<stdio.h>
int main(){
    char word[100]; //defining the variable/input user will store value in
    printf("Enter the secret word ");
    scanf("%s", word);// taking the input from the user

    for(int i=0; i<5; i++){  //using loop to print the word fo 'n; no. of required times
        printf("%s\n", word);
    }
    return 0;
}