class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        #Floyd's algorithm states that a slow pointer starting 
        #from the intersection of slow pointer and previous fast pointer
        #moving against another slow pointer starting from the beginning
        #will intersect at the point where the loop starts
        
        slow, fast = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if(slow == fast):
                break

        slow2 = 0

        while True:
            slow = nums[slow]
            slow2 = nums[slow2]

            if(slow == slow2):
                return slow