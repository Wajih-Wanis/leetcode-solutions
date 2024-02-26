class Solution {
    public int removeDuplicates(int[] nums) {
       int lastUniqueNumber=0;
       for(int i=1;i<nums.length;i++){
           if(nums[lastUniqueNumber] != nums[i]){
               nums[lastUniqueNumber+1] = nums[i];
               lastUniqueNumber++;
           }
       }
    return lastUniqueNumber+1;
    }
}   
