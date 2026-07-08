class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        output=[]
        index1,index2=0,len(numbers)-1
        while index1<index2:
            sum=numbers[index1]+numbers[index2]
            if sum==target:
                output=[numbers[index1],numbers[index2]]
                break
            elif sum<target:
                index1+=1
            else:
                index2-=1
        return output