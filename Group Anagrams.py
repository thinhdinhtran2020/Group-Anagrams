class Solution:
    def groupAnagrams(self, strs):
        hub = {}
        for word in strs:
            sorted_str = ''.join(sorted(word))
            if sorted_str not in hub:
                hub[sorted_str] = []
            hub[sorted_str].append(word)           
        return list(hub.values())    
    
def main():
    solution = Solution()
    print(solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
main()
