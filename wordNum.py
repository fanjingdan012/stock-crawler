# coding=utf-8
import collections
import codecs


if __name__ == '__main__':
    # frequency = collections.Counter(text.split())
    # print(frequency)
    with codecs.open('./text.txt', 'r','utf-8') as f:
        text = f.read()
    frequency = collections.defaultdict(int)
    i = 0
    while i < text.__len__():
        word = text[i]
        print(word)
        print('\n')
        frequency[word] += 1
        i = i + 1
    print(frequency)