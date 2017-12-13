/* 
 * sel_sort.c -- Read an integer array, print it, then sort it and
 * print it. Uses the selection sort method.
 * Code obtained from: 
 * http://cis-linux1.temple.edu/~giorgio/cis71/code/selection.c.
 */

#include <stdio.h>

#define NMAX 10

/* It reads up to nmax integers and stores then in a; sentinel 
 * terminates input. */
int getIntArray(int nmax, int a[nmax], int sentinel);

/* n is the number of elements in the array a.
 * These values are printed out, five per line. */
void printIntArray(int n, int a[]);

/* It sorts in non-decreasing order the first N positions of A. It uses 
 * the selection sort method.
 */
void selectionSort(int n, int a[]);

int main(void) {
  int x[NMAX];
  int hmny;

  hmny = getIntArray(NMAX, x, 0);
  if (hmny==0)
    printf("This is the empty array!\n");
  else{
    printf("The array was: \n");
    printIntArray(hmny, x);
    selectionSort(hmny, x);
    printf("The sorted array is: \n");
    printIntArray(hmny, x);
  }
  return 0;
}

/* n is the number of elements in the array a.
 * These values are printed out, five per line. */
void printIntArray(int n, int a[n])
{
  int i;

  for (i=0; i<n; ){
    printf("\t%d ", a[i++]);
    if (i%5==0)
      printf("\n");
  }
  printf("\n");
}

/* It reads up to nmax integers and stores then in a; sentinel 
 * terminates input. */
int getIntArray(int nmax, int a[nmax], int sentinel)
{
  /*
  int n = 0;
  int temp;

  
  do {
    printf("Enter integer [%d to terminate] : ", sentinel);
    scanf("%d", &temp);
    if (temp==sentinel) break;
    if (n==nmax)
      printf("array is full\n");
    else 
      a[n++] = temp;
  }while (1);
  */

  a[0]=4;  a[1]=2;  a[2]=32;
  a[3]=26; a[4]=94; a[5]=53;
  a[6]=3;  a[7]=10; a[8]=24;
  a[9]=17; a[10]=60;
  return nmax;
}


/* It sorts in non-decreasing order the first N positions of A. It uses 
 * the selection sort method.
 */
void selectionSort(int n, int a[])
{
  int lcv;
  int rh;      /*Elements in interval rh..n-1 are in their final position*/
  int where;   /*Position where we have current maximum*/
  int temp;    /*Used for swapping*/
  
  for(rh=n-1;rh>0;rh--){
    /*Find position of largest element in range 0..rh*/
    where = 0;
    for (lcv=1;lcv<=rh;lcv++)
      if (a[lcv]>a[where])
	where = lcv;
    temp = a[where];
    a[where] = a[rh];
    a[rh] = temp;
  }
}
