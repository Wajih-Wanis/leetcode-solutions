/*This is my first ever leetcode problem *-* 
 * As I was a beginner with no big idea I just proceeded with the simple thought of adding the two arrays into one array and
 * then sorting it. Which is not optimal at all. Thus I might redo another submission for this problem soon.
 */
class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int j;
        int i=0;
        int k=0;
        boolean status = true;
        int [] result = new int[m+n];
        for(i=0;i<m;i++){
            result[k]=nums1[i];
            k++;
           // System.out.println(result[k]);
        }
        for(j=0;j<n;j++){
            result[k]=nums2[j];
            k++;
          //  System.out.println(result[k]);
        }
        while(status){
            status=false;
            for(k=1;k<m+n;k++){
                if(result[k-1]>result[k]){
                    j=result[k-1];
                    result[k-1]=result[k];
                    result[k]=j;
                    status=true;
                }
            }
        }
        for(k=0;k<m+n;k++){
                System.out.println(result[k]);
                nums1[k]=result[k];
                }

}}