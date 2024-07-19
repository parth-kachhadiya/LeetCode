class Solution:
    def intersect(self, nums1, nums2):
        repeters = set(nums1) & set(nums2)

        if not repeters:
            return []
        else:
            mapper = {value :[nums1.count(value),nums2.count(value)]  for value in repeters}
            print(type(mapper))
            output = []
            for a, b in mapper.items():
                if b[0] == b[1]:
                    n_of_repeting = b[0]
                else:
                    n_of_repeting = min(b)

                for _ in range(n_of_repeting):
                    output.append(a)

            return output