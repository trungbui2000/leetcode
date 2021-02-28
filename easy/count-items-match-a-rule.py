# Count items matching a rule

def countMatches(items, ruleKey, ruleValue) -> int:
    if len(items) == 0:
        return 0
    output = 0
    for i in range(0, len(items)):
        if (ruleKey == "type" and ruleValue == items[i][0] or ruleKey == "color" and ruleValue == items[i][1] or ruleKey == "name" and ruleValue == items[i][2]):
            output += 1
    return output

print(countMatches([["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], "color", "silver"))