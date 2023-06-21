class Solution:
    def candy(self, ratings: List[int]) -> int:

        # left to right
        n = len(ratings)

        candy_list = [0 for _ in range(n)]
        
        i, j = 0, 1
        while i < n-1 and j < n :
            if ratings[j-1] < ratings[j] :
                j += 1
            else :
                candy = 1
                for idx in range(i, j) :
                    candy_list[idx] = max(candy, candy_list[idx])
                    candy += 1
                
                i = j 
                j = i + 1

        candy = 1
        for idx in range(i, j) :
            candy_list[idx] = max(candy, candy_list[idx])
            candy += 1

        
        i, j = n-2, n-1
        while i >= 0 and j >= 1 :
            
            if ratings[i] > ratings[i+1] :
                i -= 1
            else :
                candy = 1
                for idx in range(j, i, -1) :
                    
                    candy_list[idx] = max(candy, candy_list[idx])
                    candy += 1
                
                j = i
                i = j - 1

            
        
        candy = 1

        for idx in range(j, i, -1) :
            candy_list[idx] = max(candy, candy_list[idx])
            candy += 1
        
        return sum(candy_list)






            

        





            

        
