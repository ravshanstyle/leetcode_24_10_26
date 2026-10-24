//#include <stdio.h>
int minOperations(int* nums, int numsSize, int k) {
    int sum = 0;
    for(int i = 0; i < numsSize; i++){
        sum += nums[i];
    }
    int s = sum / k;
    return sum - s*k;
}