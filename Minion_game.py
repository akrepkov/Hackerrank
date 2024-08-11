def minion_game(string):
# Count of non-empty substrings is n*(n+1)/2
# Number of substrings of length one is n 
# Number of substrings of length two is n-1 
# Number of substrings of length k is n-k+1 where 1 <= k <= n
# Total number of substrings of all lengths from 1 to n = 
# n + (n-1) + (n-2) + (n-3) + … 2 + 1 
# = n * (n + 1)/2
    vowels = "AEIOU"
    stuart_score = 0
    kevin_score = 0
    length = len(string)
    for i in range(length):
        if string[i] in vowels: #check if it start with vowel
            kevin_score += (length - i) #n + (n-1) + (n-2) + (n-3)
        else:
            stuart_score += (length - i) #n + (n-1) + (n-2) + (n-3)
    if kevin_score > stuart_score:
        print(f"Kevin {kevin_score}")
    elif stuart_score > kevin_score:
        print(f"Stuart {stuart_score}")
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)
