#include <stdio.h>
#include <stdlib.h>
#include <math.h>

//Coded By B3mB4m


int triangular (int n){return  ((n*(n+1)/2));}			
int square	   (int n){return  (pow(n, 2));}					
int pentagonal (int n){return  (n*(3*n-1))/2;}			
int hexagonal  (int n){return  (n*(2*n-1));}				 
int heptagonal (int n){return  (n*(5*n-3))/2;}			
int octagonal  (int n){return  (n*(6*n-4))/2;}


int main(int argc, char const *argv[]){
	for (int n = 1; n < 10; ++n)
	{
		printf("triangular %d:%d\n", n,triangular( n));
		printf("square	   %d:%d\n", n,square( n));
		printf("pentagonal %d:%d\n", n,pentagonal( n));
		printf("hexagonal  %d:%d\n", n,hexagonal( n));
		printf("heptagonal %d:%d\n", n,heptagonal( n));
		printf("octagonal  %d:%d\n", n,octagonal( n));
	}

}
