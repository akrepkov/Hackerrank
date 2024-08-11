#This method has runtime error with big input
def merge_the_tools(string, k):
    if not string:
        return
#Take the first k characters as the current segment, and keep the rest for the next recursive call.
    part = string[:k]
    unique_part = ''
#Build a new string from the segment by adding characters only if they haven't been added yet.
    for char in part:
        if char not in unique_part:
            unique_part += char
    print(unique_part)
    merge_the_tools(string[k:], k)

if __name__ == '__main__':
    string = 'AAABCADDED'
    k = 5
    merge_the_tools(string, k)



def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        part = string[i:i+k]
        unique_part=''
        for char in part:
            if char not in unique_part:
                unique_part += char
        print(unique_part)

if __name__ == '__main__':
    string = 'AAABCADDED'
    k = 5
    merge_the_tools(string, k)


