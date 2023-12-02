class Solution:
    def numTilePossibilities(self, tiles: str) -> int:

        tile_dict =  {}
        for t in tiles :
            if t not in tile_dict :
                tile_dict[t] = 1
            else :
                tile_dict[t] += 1
        
        def dfs(tile_dict) :
            answer = 0
            
            for tile, cnt in tile_dict.items() :
                if cnt > 0 :
                    answer += 1
                    tile_dict[tile] -= 1
                    answer += dfs(tile_dict)
                    tile_dict[tile] += 1
            return answer
        
        return dfs(tile_dict)

