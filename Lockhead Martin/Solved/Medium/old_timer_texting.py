def convert(word):
    ans = ""
    phone_mapping = {
    'a': '2', 'b': '22', 'c': '222',
    'd': '3', 'e': '33', 'f': '333',
    'g': '4', 'h': '44', 'i': '444',
    'j': '5', 'k': '55', 'l': '555',
    'm': '6', 'n': '66', 'o': '666',
    'p': '7', 'q': '77', 'r': '777', 's': '7777',
    't': '8', 'u': '88', 'v': '888',
    'w': '9', 'x': '99', 'y': '999', 'z': '9999'
}
    for i in range(len(word)):
        if word[i].isalpha():
            if i == len(word)-1:
                ans += phone_mapping[word[i]]
            else:
                ans += phone_mapping[word[i]]+"-"
        else:
            if i == len(word)-1:
                ans += "0"
            else:
                ans += "0-" 
    return ans.strip()
for t in range(int(input())):
    word = input()
    print(convert(word))