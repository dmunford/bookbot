def sort_dict(dict):
    dict_list = []
    for char, count in dict.items():
        dict_list.append({"name": char, "count": count})
    dict_list.sort(reverse=True, key=lambda x: x["count"])
    return dict_list

def report(word_count, chars):
    print('--- Begin report of books/frankenstein.txt ---')
    print(f'{word_count} words found in the document')
    chars = sort_dict(chars)
    for char in chars:
        print(f"The '{char["name"]}' character appears {char["count"]} times")

def main():
    words = 0
    chars = {}
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        for line in file_contents.split("\n"):
            print(line)
            for word in line.split():
                words += 1
                for char in word:
                    if char.isalpha():
                        chars[char.lower()] = chars.get(char.lower(), 0) + 1
    report(words, chars)
    
if __name__ == "__main__":
    main()
    