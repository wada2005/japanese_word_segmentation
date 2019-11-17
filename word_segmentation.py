import sys
import getopt
import defaultdict

def usage():
    print('usage: % word_segmentation.py indata outdata')
    sys.exit(0)

def ngram(words, n):
    nn = list(zip(*(words[i:] for i in range(n))))
    dic = defaultdict(int)
    for line in nn:
        dic[line] += 1
    line = ""
    for k, v in dic.items():
        line = line + k + ":" + v + " "
    line = line + "\n"
    return line

def process_ngram(infile, outfile, n):
    with open(infile, "r") as fi:
        with open(outfile, "w") as fo:
            for line in fi:
                wordcount = ngram(line, n)
                fo. write(wordcount)

def main() :
    args = sys.argv 
    if len(args) == 3:
        indata = args[1]
        outdata = args[2]
    else:
        usage ()
    

if __name__ == "__main__":
    main ()