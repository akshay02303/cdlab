%{
    #include<stdio.h>
%}
%%
if|else|while|for|switch|break|return|int|char {printf("This is a keyword");}
[a-zA-Z_][a-zA-Z0-9]* {printf("This is an identifier");}
[0-9]+ {printf("This is a number");}
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
