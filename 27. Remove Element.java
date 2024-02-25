/* This solution is not adviced at all as it is so primitive and forceful. Will post a python update for this which is more optimal */
class Solution {
    public int removeElement(int[] nums, int val) {
        int k = nums.length ; 
        int i;
        int j;
        for(i=0;i<nums.length;i++){
            if(nums[i]==val){
                k--;
            }
        }
        if((nums.length==0)||(k==0)){
            return 0;
        }
        j=nums.length-1;
        i=0;
        while(i<k){
            if((nums[j]==val)&&(nums[i]!=val)){
                j--;
                i++;
                System.out.println("Boucle 1");
            }
            else if((nums[j]!=val)&&(nums[i]!=val)){
                i++;
                System.out.println("Boucle 2");
            }
            else if((nums[j]==val)&&(nums[i]==val)){
                j--;
                System.out.println("Boucle 3");
            }
            else if((nums[j]!=val)&&(nums[i]==val)){
                nums[i]=nums[j];
                i++;
                j--;
                System.out.println("Boucle 4");
            }
        }
        return k;
    }

   
}