%{
    /* program to check if the given number if hexadecimal or octal*/
    #include<stdio.h>
%}
oct [0][o][0-7]*
hex [0][x|X][0-9A-F]*
%%
{hex} {printf("This is a hexadecimal number");}
{oct} {printf("This is a octal number");}
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
