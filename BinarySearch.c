// binary search

// iterative implementation

#include<stdio.h>

int BinarySearch(int A[], int n, int x)
{
    int low = 0, high = n - 1;
    int mid = (low + high) / 2;
    if(x == A[mid]) return mid;  // found X, return (exit)
    else (x < A[mid]) high = mid - 1;
    else low = mid + 1;
}
int main()
{

}