class Solution:
    def hIndex(self, citations: List[int]) -> int:

        citations = sorted(citations)
        
        num_paper = len(citations)
        for num_cite in citations : 
            
            if num_paper <= num_cite :
                break
            num_paper -= 1 

        return num_paper