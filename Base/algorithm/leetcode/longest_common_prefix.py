
""" class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str: """


def longestCommonPrefix(strs):
    prefix = ""

    if len(strs) == 0:
        return prefix

    for i in range(len(min(strs))):

        if all(a[i] == strs[0][i] for a in strs):
            prefix += strs[0][i]
        else:
            break
    
    return prefix


print(longestCommonPrefix(["flower", "flower", "flower", "flower"]))
print(longestCommonPrefix(["flowerz", "flowz", "flightz"]))
print(longestCommonPrefix(["cir", "car"]))
print(longestCommonPrefix(["d", "cbc", "c", "ca"]))
print(longestCommonPrefix(["acc", "aaa", "aaba"]))
print(longestCommonPrefix(["a", "aca", "accb", "b"]))
