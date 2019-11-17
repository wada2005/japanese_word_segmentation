import re
import sys
import MeCab
import argparse
from collections import defaultdict

tagger = MeCab.Tagger('')
pat = re.compile(r'[0-9０-９]')

def usage():
    print('usage: % word_segmentation.py --method=hoge --num=N indata outdata')
    print('options')
    print('  --method ngram or mecab ')
    print('  --num    ngram n, mecab 0:all 1:not all')
    sys.exit(0)

def eprint(text):
    sys.stderr.write(text + '\n')
    sys.stderr.flush()
    
def eprintf(text):
    sys.stderr.write(text)
    sys.stderr.flush()

def ngram(words, n):
    nn = [ words[idx:idx + n] for idx in range(len(words) - n + 1)]
    dic = defaultdict(int)
    for line in nn:
        dic[line] += 1
    line = ""
    for w, c in sorted(dic.items(), key=lambda x: -x[1]):
        line = line + w + ':' + str(c) + ' '
    return line[:-1] + "\n"

def morph(text, n):
    tagger.parse('')
    pr = tagger.parse(text)
    words = []
    for node in pr.split("\n"):
        word = ''
        if node == 'EOS':
            break
        an = node.split('\t',1)
        features = an[1].split(',')
        surface = features[0]
        base = features[6]

        if(base=="*"):
            word = an[0]
        else:
            word = base
        
        if n == 0:
            if ' ' in word:
                word = word.replace(' ', '_')
            #word = pat.sub('#', word)
            words.append(word)
        elif n == 1:
            if (features[0] == "BOS/EOS"):
                pass
            elif (features[1] == "空白"):
                pass
            elif (features[1] == "読点"):
                pass
            elif (features[1] == "句点"):
                pass
            elif (features[1] == "括弧開"):
                pass
            elif (features[1] == "括弧閉"):
                pass
            elif (word == ","):
                pass
            else:
                if ' ' in word:
                    word = word.replace(' ', '_')
                #word = pat.sub('#', word)
                words.append(word)
    return words

def parse_mecab(text, n):
    words = morph(text, n)
    freq = defaultdict(int)
    for word in words:
        freq[word] += 1
    line = ''
    for w, c in sorted(freq.items(), key=lambda x: -x[1]):
        line = line + w + ':' + str(c) + ' '
    return line[:-1] + "\n"

def process_ngram(infile, outfile, n):
    with open(infile, "r") as fi:
        with open(outfile, "w") as fo:
            for line in fi:
                wordcount = ngram(line.rstrip('\n'), n)
                fo.write(wordcount)

def process_mecab(infile, outfile, n):
    with open(infile, "r") as fi:
        with open(outfile, "w") as fo:
            for line in fi:
                wordcount = parse_mecab(line.rstrip('\n'), n)
                fo.write(wordcount)


def get_option():
    parser = argparse.ArgumentParser(description='segmentation')
    parser.add_argument('arg1')    # indata
    parser.add_argument('arg2')    # outdata
    parser.add_argument('-m', '--method',type=str, default="mecab", help='ngram or mecab') 
    parser.add_argument('-n', '--num', type=int, default=0, help='ngram N, mecab 0:all, 1:not')
    args = parser.parse_args()
    return args

def main() :
    args = get_option()
    eprint('Method = %s, N = %d' % (args.method, args.num))
    eprint('processing data ...')

    indata = args.arg1
    outdata = args.arg2

    if args.method == "ngram":
        process_ngram(indata, outdata, args.num)
    elif args.method == "mecab":
        process_mecab(indata, outdata, args.num)
    else:
        usage()

if __name__ == "__main__":
    main ()