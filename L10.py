strg = input("Type any sentence: ")

class StrgUtl:
    def __init__(self,string):
        self.string = string

    def countWord(self):
        return len(self.string.split(" "))
    def findMostFrequentChar(self):
        char={}
        for i in strg:
            if i in char:
                char[i]=char[i]+1
            else:
                char[i]=1
        ans = max(char, key = char.get)
        print(ans)

def main():
        obj = StrgUtl(strg)
        print("Total Words: ", obj.countWord())
        print("Most Frequent Character: ", obj.findMostFrequentChar())

main()



