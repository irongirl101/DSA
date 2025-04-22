#include <stdio.h> 

//bubble sort, time complexity o(n^2), with best case o(n)  

void bubble(int *arr, int n ){
    
    //printf("size %d", sizeof(arr));

    //printf("nume =  %zu\n", sizeof(*arr));
    //printf("den =  %zu\n", sizeof(arr[0]));


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


    printf("done\n");
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
/*
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

//insert = 4, then compare it against each number, other than itself. */
void insertion(int arr[],int n){
    for(int i = 0; i<n; i++){ 
        int current_value = arr[i]; 
        int j = i -1; 

        while (j >= 0 && arr[j] > current_value) {
            arr[j + 1] = arr[j];
            j--;
        }
        
        arr[j + 1] = current_value; 
    }
    for (int i = n-1; i >=0; i--)
    {
        printf("%d \n",arr[i]);
    }
    
}
int binary(int key,int arr[], int size){
    int low = 0; 
    int high = size-1; 

    while(low<=high){
        int mid = (low+high)/2; 

        if (arr[mid] == key){
            return arr[mid]; 
        }
        else if(mid>key){
            high = mid-1; 
        }
        else{
            low = mid+1; 
        }
    }   
    return -1; 
}

void counting(int arr[],int n){
    //gives me the largest number 
    int max = arr[0]; 
    for(int i = 0; i<n; i++){
        if(max<arr[i]){
            max = arr[i]; 
        }
    }
    int count_arr[max]; //creates an array of length of max 

    for(int i =0; i<=max; i++){
        count_arr[i] = 0; //creates array of only zeroes for the time being 
    }

    for(int i = 0; i<n; i++){//finds the total number of times each value comes 
        int pos = arr[i]; 
        count_arr[pos]+=1; 
        arr[i] = 0; 
    } 
    int index = 0;
    for (int i = 0; i <= max; i++) {
        while (count_arr[i] > 0) {
            arr[index++] = i;
            count_arr[i]--;
        }
    }
    for (int i = n-1; i >=0; i--)
    {
        printf("%d \n",arr[i]);
    }
}

int binary_Rec(int key, int arr[], int low, int high){
    if(low>=high){
        return -1; 
    }
    else{
        int mid = (low+high)/2; 
        if(mid == key){
            return 1; 
        }
        else if(mid>key){
            return binary_Rec(key,arr,low,mid-1);
        }
        else{
            return binary_Rec(key,arr,mid+1,high); 
        }

    }
}
/*
Difference bw selection sort and insertion sort 
Selection sort splits the array into two parts, one sorted and the other unsorted. 
It selects the smallest element from the unsorted array and then swaps it 

Insertion Sort inserts the element in its correct position -> using shifting and not swapping 
*/

void quicksort(){} //will come back to this 

//wwill come back 
void radixsort(int arr[],int size){
    //getting max value
    int max = arr[0]; 
    for(int i = 1; i<size;i++){
        if(arr[i]>max){
            max = arr[i]; 
        }
    }
    int exp = 1; 

    while((max/exp)>0){
        int radix[10][1] = {{},{},{},{},{},{},{},{},{},{}}; 
        for(int i = 0; i<size; i++){
            int ind = (i/exp)%10; 

        }
    }

}

int main(){
    int arr[10] = {2,3,4,5,1,2,0,3,1,2}; 
    int n = sizeof(arr)/sizeof(arr[0]); 

//    printf("nume =  %d\n", sizeof(arr));
//    printf("den =  %d\n", sizeof(arr[0]));

    counting(arr,n); 
    return 0; 
}




