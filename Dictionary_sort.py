if __name__ == '__main__':
    s = 'aabbbccde'
    dict = {}
    for n in s:
        keys = dict.keys()
        if n in keys:
            dict[n] +=1
        else:
            dict[n] = 1
    res = sorted(dict.items(), key = lambda item:(-item[1], item[0]))
    for key, value in res[:3]:
        print (f"{key} {value}")
