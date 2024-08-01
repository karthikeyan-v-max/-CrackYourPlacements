class Solution:
    def multiply_two_lists(self, first, second):
        # Code here
        l1 , l2 = first , second
        items1 = 0
        items2 = 0
        res = 0
        mod = 1000000007
        
        while l1:
            items1 = (items1*10) + l1.data
            items1 = items1%mod
            l1 = l1.next
            
        while l2:
            items2 = (items2*10) + l2.data
            items2 = items2%mod
            l2 = l2.next
            
        res = (items1 * items2) % mod
        return res