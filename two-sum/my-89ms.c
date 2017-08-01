/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target) {
    int i,j = 0;
    int number = 0;
    int *ret;
    ret = (int*)malloc(2*sizeof(int));
    for(i; i< numsSize; i++)
    {
        number = target - *(nums+i);
        for(j = i+1; j<numsSize; j++)
        {
            if ( *(nums +j) == number )
            {
                *ret = i;
                *(ret+1) = j;
                return ret;
            }
        }
    }
    return ret;
}
