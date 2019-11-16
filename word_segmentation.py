import getopt
import sys

def usage():
    print('usage: % word_segmentation.py indata outdata')
    sys.exit(0)

def ngram(text, n):
    



def main() :
    args = sys.argv 
    if len(args) == 3:
        indata = args[1]
        outdata = args[2]
    else:
        usage ()
    

if __name__ == "__main__":
    main ()