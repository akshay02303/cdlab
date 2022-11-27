%{
#include<stdio.h>
%}
%token NUMBER
%left '+' '-'
%left '*' '/'
%left '(' ')'
%%
ArithmeticExpression: e {
					printf("result is %d\n", $$);
					return 0;
					}
e: e'+'e {$$=$1+$3;}
 | e'-'e {$$=$1-$3;}
 | e'*'e {$$=$1*$3;}
 | e'/'e {$$=$1/$3;}
 | e'('e {$$=$2;}
 | NUMBER {$$=$1;}
 ;
%%

int main() {
	printf("Enter any arithmetic expression: ");
	yyparse();

	return 0;
}

void yyerror() {
	printf("Enter valid expression!!!\n");
}

