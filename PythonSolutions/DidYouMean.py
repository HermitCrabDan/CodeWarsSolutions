#https://www.codewars.com/kata/5259510fc76e59579e0009d4
class Dictionary:
    def __init__(self,words):
        self.words=words
    def levenshtein(self,term,word):
        cm = []
        for i in range(len(word)+1):
            t = []
            for j in range(len(term)+1):
                if i == 0:
                    t.insert(j,j)
                elif j == 0:
                    t.insert(j,i)
                else:
                    t.insert(j,0)
            cm.insert(i,t)
        for i in range(len(word)):
            for j in range(len(term)):
                x1 = cm[i][j+1] + 1
                x2 = cm[i+1][j] + 1
                x3 = cm[i][j] + 1
                if word[i] == term[j]:
                    x3 -= 1
                cm[i+1][j+1] = min(x1,x2,x3)
        return cm[len(word)][len(term)]
    def find_most_similar(self,term):
        scores = []
        for i in range(len(self.words)):
            word = self.words[i]
            score = self.levenshtein(term,word)
            scores.insert(i, score)
        return self.words[scores.index(min(scores))]