import os

strs = ["flower", "flow", "floght"]


longestPrefix = ""        
if len(strs) == 0:
    print(longestPrefix)
    os.sys.exit()
curCharIdx = 0
for c in strs[0]:
    for idx in range(1, len(strs)):
        if len(strs[idx]) == curCharIdx:
            print(longestPrefix)
            os.sys.exit()
        if strs[idx][curCharIdx] != c:
            os.sys.exit()
    curCharIdx += 1
    longestPrefix = longestPrefix + c

print(longestPrefix)