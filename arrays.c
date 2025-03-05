#include <stdio.h> 


//bubble sort 


int bubble(){
    int arr[] = {4,6,2,1,5,8}; 
     
    for(int i = 0; i<sizeof(arr)/sizeof(arr[0])-1; i++ ){ //goes through the array 
        for(int j=0; j<(sizeof(arr)/sizeof(arr[0]))-i-1; j++){
            if (arr[j]<arr[j+1])
            {
               int temp = arr[j]; 
               arr[j] = arr[j+1]; 
               arr[j+1] = temp; 
            }   

        }

    }
    for(int i = 0 ; i<sizeof(arr)/sizeof(arr[0]); i++){
        printf("%d \n", arr[i]); 
    }
    return 0; 
}

int main(){

    return 0; 
}