import re
from itertools import permutations

# 设置密文
from pycipher import Vigenere
from ngram_score import ngram_score
path = 'cipher3.txt'
with open(path, "r") as f:
    ciphertext = f.read()
    ciphertext = re.sub(r'[^A-Z]', '', ciphertext.upper())
    f.close()

#加载字典
print('正在加载字典....')
qgram = ngram_score('quadgrams.txt')
tgram = ngram_score('trigrams.txt')
print("success")
# 设置列表最大长度
N = 100
# 设置字母表
Alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


class OptativeStore(object):
    def __init__(self, store_length=1000):
        self.store = []
        self.store_length = store_length

    def append(self, item):
        self.store.append(item)
        self.store.sort(reverse=True)
        self.store = self.store[:self.store_length]

    def __getitem__(self, K):
        return self.store[K]

    def __len__(self):
        return len(self.store)


def ProcessTriGram(KLEN):

    oTable = OptativeStore(N)
    for i in permutations(Alphabet, 3):
        partkey = ''.join(i)
        fullkey = partkey + 'A' * (KLEN - 3)
        plaintext = Vigenere(fullkey).decipher(ciphertext)
        score = 0
        for j in range(0, len(plaintext), KLEN):
            score += tgram.score(plaintext[j:j + 3])
        oTable.append((score, partkey,  plaintext[:30]))
    return oTable


def SolveVirginia(KLEN):

    assert(KLEN > 2)
    best = ProcessTriGram(KLEN)
    nextbest = OptativeStore(N)
    for i in range(0, KLEN - 3):
        # print(i)
        for j in range(N):
            for k in Alphabet:
                partkey = best[j][1] + k
                # print(KLEN,len(partkey))
                fullkey = partkey + ('A' * (KLEN - len(partkey)))
                # print(fullkey)
                plaintext = Vigenere(fullkey).decipher(ciphertext)
                score = 0
                for l in range(0, len(ciphertext), KLEN):
                    score += qgram.score(plaintext[l:l + KLEN])
                nextbest.append((score, partkey, plaintext[:30]))
        best = nextbest
        nextbest = OptativeStore(N)
    return best

def hack_2():
    for i in range(3, 20):
        bestkey = SolveVirginia(i)[0][1]
        plaintext = Vigenere(bestkey).decipher(ciphertext)
        bestscore = qgram.score(plaintext)
        print("key length is %2d : %4d %20s %s" %
              (i, bestscore, bestkey, plaintext))