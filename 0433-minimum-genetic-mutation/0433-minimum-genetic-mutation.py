class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:

        def available_list(gene) :
            avl_list = []
            for avail in bank :
                cnt = 0
                for av, g in zip(avail, gene) :
                    if av != g :
                        cnt += 1
                    if cnt > 1 :
                        break
                if cnt == 1 :
                    avl_list.append(avail)

            return avl_list

        visited = {b : 0 for b in bank}

        cnt = 0
        if not bank :
            return -1

        queue = collections.deque([[startGene, cnt]])
        
        while queue :
            gene, cnt = queue.popleft()
            if gene == endGene :
                return cnt
            avl_w_one_mutation = available_list(gene)

            for avl in avl_w_one_mutation :
                if not visited[avl] :
                    visited[avl] = 1
                    queue.append([avl, cnt + 1])

        return -1
        