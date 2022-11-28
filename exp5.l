%{
    /* program to capitalize the given comment */
    #include<stdio.h>
    #include<ctype.h>
    int k = 0;
    void display(char *);
%}
letter ([a-zA-Z0-9]|[+\-*%;=])
comment [//]
%%
{comment} {k=1; printf("%c", yytext[0]);}
{letter} {if (k==1) display(yytext); else printf("%c", yytext[0]);}
[\n] {k=0;}
%%
int main()
{
    yylex();
    return 0;
}
void display(char *s) 
{
    printf("%c", toupper(s[0]));
}
int yywrap()
{
    return 1;
}
