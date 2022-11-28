%{
    /* program to identify vowels and consonants */
    #include<stdio.h>
    int vowels_count = 0, consonants_count = 0;
    char vowels[100], consonants[100];
    int i = 0;
%}
%%
[aeiouAEIOU] {vowels[vowels_count] = yytext[0]; vowels_count++;}
[a-zA-Z] {consonants[consonants_count] = yytext[0]; consonants_count++;}
[\n] return 0;
%% 
int main()
{
    printf("Enter any string: ");
    yylex();
    printf("Vowels count: %d\n", vowels_count);
    printf("Consonants count: %d\n", consonants_count);
    printf("Vowels present are: ");
    for (i=0; i<vowels_count; i++) printf("%c", vowels[i]);
    printf("\nConsonants present are:");
    for (i=0; i<consonants_count; i++) printf("%c", consonants[i]);
    return 0;
}
int yywrap()
{
    return 1;
}