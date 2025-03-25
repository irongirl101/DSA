#include <stdio.h> 

//bubble sort, time complexity o(n^2), with best case o(n)  

void bubble(int *arr, int n ){
    
    //printf("size %d", sizeof(arr));

    printf("nume =  %zu\n", sizeof(*arr));
    printf("den =  %zu\n", sizeof(arr[0]));


    for(int i = 0; i<n-1; i++ ){ //goes through the array ..
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

   for(int i = n-1 ; i>=0; i--){
        printf("%d \n", arr[i]); 
    } 

    
}

void search(int arr[], int n, int x){
    for(int i = 0; i<n; i++){
        if(arr[i]==x){
            printf("Found");
            break;
        }
        if (i==n-1 && arr[i]!=x){
            printf("Not found");
        }

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
        //this is used for swapping min element with the first element of the unsorted part 
         if (min != i) {
            int temp = arr[i];
            arr[i] = arr[min];
            arr[min] = temp;
        }    

    }

}

void map(int *input, int *output, int size, int (*callback)(int));

int incremenet(int x){
    return x+1;
}

int main(){
    int arr[6] = {4,7,2,1,3,5}; 
    int n = sizeof(arr)/sizeof(arr[0]); 
    int output[n]; 

//    printf("nume =  %d\n", sizeof(arr));
//    printf("den =  %d\n", sizeof(arr[0]));


    bubble(arr,n); 
    return 0; 
}