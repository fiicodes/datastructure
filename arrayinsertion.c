#include<stdio.h>

void display(int arr[],n)
{
    for(i=0;i<n;i++){
        printf(%d\n,arr[i]);
    }
}
int main(){
    int arr[100]={2,3,5,8,18};
    display(arr,5);
    return 0;

}
