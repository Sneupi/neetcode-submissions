class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        ana = {}

        for s in strs: 

            a = ''.join(sorted(s))

            if ana.get(a, None) is None:
                ana[a] = []
            
            ana[a].append(s)
        
        return [v for k, v in ana.items()]