class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        
        bank_dict = collections.defaultdict(list)

        def compare(gene1, gene2) :
            cnt = 0
            for l1, l2 in zip(gene1, gene2) :
                if l1 != l2 :
                    cnt += 1
                    if cnt > 1 :
                        return False
            return cnt == 1

        for b in bank + [startGene] :
            for compare_gene in bank :
                if compare(b, compare_gene) :
                    bank_dict[b].append(compare_gene)

        cnt = 0
        queue = collections.deque([[startGene, cnt]])
        visited = {b : 0 for b in bank}

        # print(bank_dict)
        while queue :
            trgGene, cnt = queue.popleft()
            if trgGene == endGene :
                return cnt
            for mutated in bank_dict[trgGene] :
                if not visited[mutated] :
                    visited[mutated] = 1
                    queue.append([mutated, cnt + 1])

        return -1


        # if not bank :
        #     return -1

        # def available_list(gene) :
        #     avl_list = []
        #     for avail in bank :
        #         cnt = 0
        #         for av, g in zip(avail, gene) :
        #             if av != g :
        #                 cnt += 1
        #             if cnt > 1 :
        #                 break
        #         if cnt == 1 :
        #             avl_list.append(avail)

        #     return avl_list

        # visited = {b : 0 for b in bank}

        # cnt = 0
        

        # queue = collections.deque([[startGene, cnt]])
        
        # while queue :
        #     gene, cnt = queue.popleft()
        #     if gene == endGene :
        #         return cnt
        #     avl_w_one_mutation = available_list(gene)

        #     for avl in avl_w_one_mutation :
        #         if not visited[avl] :
        #             visited[avl] = 1
        #             queue.append([avl, cnt + 1])

        # return -1
        