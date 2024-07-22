class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        people = list(zip(names, heights))

        people.sort(reverse=True, key=lambda x: x[1])

        sorted_names = [name for name, _ in people]

        return sorted_names
    