def detectCapitalUse(word):
    
    rule1 = True
    for char in word:
        if char != char.upper():
            rule1 = False
            break
    if rule1:
        return True

    
    rule2 = True
    for char in word:
        if char != char.lower():
            rule2 = False
            break
    if rule2:
        return True

    
    rule3 = True
    if word[0] != word[0].upper():
        rule3 = False
    for char in word[1:]:
        if char != char.lower():
            rule3 = False
            break
    if rule3:
        return True

    return False

print(detectCapitalUse("BmW"))  
