%{
    #include<stdio.h>
%}
    keyword int|char|bool|float|void|for|do|while|if|else|return|void
%%
    {keyword}       {printf("%s is a Keyword\n",yytext);}
    [0-9]*          {printf("%s is a Number\n",yytext);}
    "+"|"-"|"*"|"/" {printf("%s is an Operator\n",yytext);}
    "cc"            {printf("%s is a Complier Construction\n",yytext);}
    [a-zA-Z]+[0-9]* {printf("%s is an Identifier\n",yytext);}
%%  
main()
{
    printf("Enter String: \n");
    yylex();
}
int yywrap(){
    return 1;
}
