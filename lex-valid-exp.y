%{
#include<stdio.h>
#include<stdlib.h>
%}
%token NUMBER ID
%left '*' '/'
%left '+' '-'
%%
expr: expr'-'expr
	| expr'+'expr
	| expr'*'expr
	| expr'/'expr
	| '-' NUMBER
	| '-' ID
	| '('expr')'
	| NUMBER
	| ID 
	;
%%

int main() {
	printf("enter the expression: \n");
	yyparse();
	printf("Expression is valid\n");
	exit(0);
}

int yyerror() {
	printf("Expression is invalid\n");
	exit(0);
}

