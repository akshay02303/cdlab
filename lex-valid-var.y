%{
#include<stdio.h>
int valid=1;
%}
%token digit letter

%%
start: letter s
s: letter s
 | digit s
 |
 ;
%%
int yyerror() {
	valid = 0;
	printf("It ain't an identifier\n");

	return 0;
}
int main() {
	printf("Enter an identifier: ");
	yyparse();

	if(valid) {
		printf("It is a valid identifier\n");
	}


	return 0;
}

