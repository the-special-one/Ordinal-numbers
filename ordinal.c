#include <stdio.h>

char *ordinal(int n){
    if (n==11 || n==12 || n==13)
        return("th");
    if (n%10==1)
        return("st");
    if (n%10==2)
        return("nd");
    if (n%10==3)
        return("rd");
    return("th");    
}

void main(){
    int n, c;
    printf("Nombre de rangs à afficher \n");
    scanf("%d", &n);
    for(c=1; c<=n; c++)
        printf("%d%s \t %d%s \t %d%s \n",
                c, ordinal(c),
                c+20, ordinal(c+20),
                c+40, ordinal(c+40)
                );
}