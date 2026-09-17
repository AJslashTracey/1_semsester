#include <iostream>
using namespace std;

int addIntegers(int a, int b) {
  return a + b;
}




int main()
{
	int x;
	
	float a = 3.1415;
	int b = 30000;
	int c = 50000;

cin >> x; // Wait for user input
cout << "Example [x^2 >= 0], x = " << a << " : " << a*a << endl << endl;

cin >> x; // Wait for user input
cout << "Example [x^2 >= 0], x = " << b << " : " << b*b << endl << endl;

cin >> x; // Wait for user input
cout << "Example [x^2 >= 0], x = " << c << " : " << c*c << endl << endl;










  float d = 1e20;
  float e = -1e20;
  float f = 3.1415;

cin >> x; // Wait for user input
cout << "Example 2 [(d + e) + f]: " << (d + e) + f << endl << endl;


cin >> x; // Wait for user input
cout << "Example 2 [d + (e + f)]: " << d + (e + f) << endl << endl;








int puzzle = 0;

cin >> x; // Wait for user input
cout << "Example 3 [(x+1) > x], x = " << a << " ; (x+1) = " << (a+1) << endl;
cin >> x; // Wait for user input
cout << "Example 3 [(x+1) > x], x = " << b << " ; (x+1) = " << (b+1) << endl;

cout << endl << "Enter your result for the puzzle!" << endl;
cin >> puzzle; // Wait for user input
cout << "Example 3 [(x+1) > x], x = " << puzzle << " ; (x+1) = " << (puzzle+1) << endl;


// The following examples were not discussed in class.

  float h = 3.1415;
  float i = 0.085;
  
  int j = addIntegers(h, i);
  
// cin >> x; // Wait for user input
// cout << "Example 4: " << j << endl << endl;
  
  int k = 3.8;
  int l = 4.1;

  float m = (float) addIntegers(k, l);
  float n = addIntegers(k, l);
  
// cin >> x; // Wait for user input
// cout << "Example 5a: " << m << endl;
// cin >> x; // Wait for user input
// cout << "Example 5b: " << n << endl;

  return 0;
}
