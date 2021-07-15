def lengthOfLongestSubstring(s: str) -> int:
    if len(s) == 0: return 0
    if len(s) == 1: return 1
    
    max_length = 0
    temp_list = []
    for i in range(len(s)):
        if s[i] not in temp_list:
            temp_list.append(s[i])
            if len(temp_list) > max_length:
                max_length = len(temp_list)
        
        elif s[i] in temp_list:
            control = True
            temp2_list = []

            for j in range(len(temp_list) - 1, -1, -1):
                if temp_list[j] == s[i]:
                    break

                temp2_list.insert(0, temp_list[j])

            temp_list = temp2_list
            temp_list.append(s[i])
    
    print(temp_list)
    return max_length

val = lengthOfLongestSubstring("dvdf")
print(val)