%{
    /* program to find complete real precision */
    #include<stdio.h>
    int count = 0;
%}
%%
[.] continue;
[0-9] count++;
[\n] printf("precision is %d\n", count);
%%
int main()
{
    yylex();
    return 0;
}
int yywrap()
{
    return 1;
}
