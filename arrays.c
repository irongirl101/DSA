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

   for(int i = n+1 ; i>=0; i--){
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

//{4,1,2,3}
//i = 0 current value = 4 
//4>1, {1,4,2,3}
//4>2  {1,2,4,3}
//4>3  {1,2,3,4}

//{4,2,1,5,3}
//i = 0, current value = 4 
// j = 0
//4>2 {2,4,1,5,3}
//j = 2 (j!=4)
//4>1 {2,1,4,5,3}
//j = 4 (j!=4)
//4<5 
//{2,1,4,5,3}

//i = 1, current value = 1
//j = 0 
//2>1 {1,2,4,5,3} 
//j = 1 

// i = 2, current value = 4 
//j = 3
//4<5 pass {1,2,4,5,3}
// j = 4 
//4>3 {1,2,3,5,4}

//i = 3, current value = 5 
// j = 4 
//5>3 {1,2,3,4,5}

//logic : 2 loops, one that goes through the array (changed or not), and swap if current value > arr[j] and skip if current value <= arr[j]

//insert = 4, then compare it against each number, other than itself. 
void insertion(int arr[],int n){
    for(int i = 0; i<n; i++){
        int insert = i; 
        int current_value = arr[i]; 
        for(int j = 0; j<n; j++){
            if(current_value>arr[j]){
                int temp = arr[j]; 
                arr[j] = arr[i]; 
                arr[i] = temp;


            }
        }
    }
    for (int i = n+1; i >=0; i--)
    {
        printf("%d \n",arr[i]);
    }
    

}


int main(){
    int arr[6] = {4,7,2,1,3,5}; 
    int n = sizeof(arr)/sizeof(arr[0]); 

//    printf("nume =  %d\n", sizeof(arr));
//    printf("den =  %d\n", sizeof(arr[0]));


    insertion(arr,n); 
    return 0; 
}



