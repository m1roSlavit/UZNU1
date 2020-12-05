def getWordInStr(str):
    return [x.strip() for x in str[:-1].split(",")].count(self[0])
    # return arr.count(arr[0]) - 1

print(getWordInStr("asd, dfg, asd, gfgfg, asdfd, asdd, asd, asd   ."))