#Link - https://leetcode.com/problems/valid-parentheses
def isValid(self, s: str) -> bool:
    char_list = list(s)
    if len(char_list) % 2 != 0:
        return False
    # print(char_list)
    open_bracket = []
    bracket_pair = {}
    bracket_pair[')'] = '('
    bracket_pair['}'] = '{'
    bracket_pair[']'] = '['
    for char in char_list:
        if (char == '(' or char == '{' or char == '['):
            open_bracket.append(char)
        else:
            if len(open_bracket) != 0:
                if bracket_pair.get(char) == open_bracket.pop():
                    print('reached here')
                else:
                    return False
            else:
                return False
    if len(open_bracket) == 0:
        return True
    else:
        return False