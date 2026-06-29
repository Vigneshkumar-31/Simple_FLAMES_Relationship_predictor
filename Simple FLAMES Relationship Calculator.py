# Simple FLAMES Relationship Calculator

def remove_common_letters(name1, name2):
    name1 = list(name1.replace(" ", "").lower())
    name2 = list(name2.replace(" ", "").lower())

    for letter in name1[:]:
        if letter in name2:
            name1.remove(letter)
            name2.remove(letter)

    return len(name1) + len(name2)


def flames_result(count):
    flames = ["F", "L", "A", "M", "E", "S"]

    while len(flames) > 1:
        split_index = (count % len(flames)) - 1

        if split_index >= 0:
            right = flames[split_index + 1:]
            left = flames[:split_index]
            flames = right + left
        else:
            flames = flames[:len(flames) - 1]

    return flames[0]


def relationship_meaning(letter):
    meanings = {
        "F": "Friends",
        "L": "Love",
        "A": "Affection",
        "M": "Marriage",
        "E": "Enemies",
        "S": "Siblings"
    }

    return meanings[letter]



name1 = input("Enter first name: ")
name2 = input("Enter second name: ")

count = remove_common_letters(name1, name2)
result_letter = flames_result(count)
result = relationship_meaning(result_letter)

print("\nFLAMES Result:", result)