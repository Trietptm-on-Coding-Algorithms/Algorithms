#include <iostream>
#include <math.h>


using namespace std;
//Coded By B3mB4m
int main(){
     int x = 45;
     int cache = 0;

     for (int i = 0; i < 20; ++i)
     {
     	while (x !=0) {
   		  cache = cache + pow(x%10, 2);
          x = (int) x/10;
	    }
	    cout << cache << endl;
	    x = cache;
	    cache = 0;
     }

}
