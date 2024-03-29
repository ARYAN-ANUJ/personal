class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1=len(nums1)
        n2=len(nums2)
        n=n1+n2
        if (n1>n2):
            return self.findMedianSortedArrays(nums2,nums1)
        partition=(n1+n2+1)//2

        if n1==0:
            return (nums2[n2//2]+nums2[n2//2-1])/2 if n2%2==0 else nums2[n2//2]
        if n2==0:
            return (nums1[n1//2]+nums1[n1//2-1])/2  if n1%2==0 else nums1[n1//2]

        left=0
        right=n1
        while(left<=right):
            cut1=(left+right)//2
            cut2=partition-cut1

            l1= float('-inf') if cut1==0 else nums1[cut1-1];
            l2= float('-inf') if cut2==0 else nums2[cut2-1];

            r1= float('inf') if cut1>=n1 else nums1[cut1];
            r2= float('inf') if cut2>=n2 else nums2[cut2];
            
            if (l1<=r2 and l2<=r1):
                return (max(l1,l2)+min(r1,r2))/2 if n%2==0 else max(l1,l2)
            else:
                if (l1>r2):
                    right=cut1-1
                else:
                    left=cut1+1

        
        return 0.0