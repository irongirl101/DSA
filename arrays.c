#include <stdio.h> 


//bubble sort, time complexity o(n^2), with best case o(n)  

void bubble(int arr[], int n ){
    
    for(int i = 0; i<n-1; i++ ){ //goes through the array 
        for(int j=0; j<n-i-1; j++){
            if (arr[j]<arr[j+1])
            {
               int temp = arr[j]; 
               arr[j] = arr[j+1]; 
               arr[j+1] = temp; 
            }   

        }

    }
    for(int i = 0 ; i<n; i++){
        printf("%d \n", arr[i]); 
    }
    
}

void selection(int arr[], int n){
    for(int i = 0; i<n-1; i++){
        int min = i ; 
        for(int j = i+1; j<n; j++){
            if(arr[j]<arr[min]){
                min = j; 
            }
        }
        int value = arr

    }

}

int main(){
    int arr[6] = {4,7,2,1,3,5}; 
    int n = sizeof(arr)/sizeof(arr[0]); 
    bubble(arr,n); 
    return 0; 
}