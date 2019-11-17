import sys
import getopt
from collections import defaultdict

def usage():
    print('usage: % word_segmentation.py indata outdata')
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
    for k, v in dic.items():
        line = line + k + ":" + str(v) + " "
    line = line + "\n"
    return line

def process_ngram(infile, outfile, n):
    with open(infile, "r") as fi:
        with open(outfile, "w") as fo:
            for line in fi:
                wordcount = ngram(line.rstrip('\n'), n)
                fo. write(wordcount)

def main() :
    shortopts = "M:N"
    longopts = ['method=', 'ngram_n=']
    M = "ngram"
    N = 2

    try:
        opts, args = getopt.getopt(sys.argv[1:], shortopts, longopts)
    except getopt.GetoptError:
        usage()
    
    for o, a in opts:
        if o in ('-M', '--method'):
            M = a
        elif o in ('-N', '--ngram_n'):
            N = int(a)
        elif o in ('-h', '--help'):
            usage()
        else:
            assert False, "unknown option"

    if len(args) == 2:
        indata = args[0]
        outdata = args[1]
    else:
        usage ()
    
    eprint('Method = %s, Ngram = %d' % (M, N))
    eprint('processing data ...')

    process_ngram(indata, outdata, N)


if __name__ == "__main__":
    main ()