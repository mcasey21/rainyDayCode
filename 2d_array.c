/*
Entering and displaying data in a 2-Dimensional array
*/

#include <stdio.h>

// Use symbolic names for the Rows and Cols
#define ROW 3
#define COL 2

int main()
{
 	int myarray[ROW][COL];
 	int i, j;
	int initialised_array[3][3] = {};


 	printf("Enter %d numbers\n", ROW * COL);
    
  	// Enter data i.e., whole numbers, into the array
 	for(i = 0; i < ROW; i++)
 	{
   		// Inner for that handles the Cols
   		for(j = 0; j < COL; j++)
   		{
     		// read in data
     		scanf("%d", & myarray[i][j]);

   		} // end inner for

 	} // end outer for


// Display the data entered into the array
 	for(i = 0; i < ROW; i++)
 	{
   		// Inner for that handles the Cols
   		for(j = 0; j < COL; j++)
   		{
     		// display the data
     		printf("\nmyarray[%d][%d] = %d", i, j, myarray[i][j]);

   		} // end inner for

 	} // end outer for

 	return 0;

} // end main()