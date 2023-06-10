#include <stdio.h>

int main()
{
    char result = 'S';
    int vet[8];
    for(int i = 0; i < 8; i++) {
        scanf("%d", &vet[i]);
        if( vet[i] == 9){
           result = 'F';
        }
    }
    
    printf("%c\n", result);
    

    return 0;
}
