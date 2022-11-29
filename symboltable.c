#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
int main() {
	char input[100];
	printf("Enter expression: ");
	scanf("%s", input);
	int n = strlen(input);
	printf("Given expression: %s\n", input);
	printf("size: %d\n", n);
	printf("Symbol\t\tAddress\t\tType\n");
	for(int i=0;i < n;i++) {
		char c = input[i];
		void *p = malloc(c);
		if(isalpha(toascii(c))) {
			printf("%c\t\t%d\t\tidentifier\n", c, p);
		} else {
			if(c == '+' || c == '-' || c == '*' || c == '=') {
				printf("%c\t\t%d\t\toperator\n", c, p);	
			}
		}
	}
	return 0;
}
