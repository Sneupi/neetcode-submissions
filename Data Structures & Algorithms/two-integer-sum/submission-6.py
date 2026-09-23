class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen  = {}

        for i, n in enumerate(nums):
            
            if seen.get(n, None) is None:
                seen[n] = []

            seen[n].append(i)
        
        for n, n_list in seen.items():
            
            comp = seen.get(target - n, None)

            if comp is not None:
                if target - n != n:
                    return [n_list[0], comp[0]]
                elif len(n_list) > 1:
                    return [n_list[0], n_list[1]]
                else: 
                    continue
