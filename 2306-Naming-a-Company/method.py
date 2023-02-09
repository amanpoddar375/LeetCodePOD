class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        name_dict = defaultdict(set)
        result = 0
        for idea in ideas:
            first_letter = idea[0]
            rest_of_name = idea[1:]
            name_dict[first_letter].add(rest_of_name)
        sorted_names = sorted(name_dict.items())
        for name1 in sorted_names:
            for name2 in sorted_names:
                if name2[0] >= name1[0]:
                    break
                common_names = len(name1[1] & name2[1])
                result += ((len(name1[1]) - common_names) * (len(name2[1]) - common_names))
        
        return result * 2
