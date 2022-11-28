%{
    /* checking if starting with a or not */
    #include<stdio.h>
%}
%%
[a|A][a-z0-9A-Z]* printf("Starting with a or A");
[a-zA-Z0-9]* printf("Not starting with a or A");
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