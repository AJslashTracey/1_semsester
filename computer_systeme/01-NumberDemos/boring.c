#include <stdio.h>

int main(void)
{
  unsigned int plus_one = 1; 		// 32 bit - 00000001
  int minus_one = -1;			// 32 bit - 11111111

	
  if (plus_one < minus_one)
    printf("1 < -1");			// DAS wird ausgeführt!
  else
    printf("boring");			// NICHT das "boring"

  return 0;
}
