class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        ans = []
        min_index_sum = float('inf')

        res_to_index = {restaurant:index for index, restaurant in enumerate(list2)}

        for id1, res in enumerate(list1):
            if res in res_to_index:
                id2 = res_to_index[res]
                curr_sum = id1 + id2

                if curr_sum < min_index_sum:
                    min_index_sum = curr_sum
                    ans = [res]
                elif curr_sum == min_index_sum:
                    ans.append(res)
        
        return ans
        