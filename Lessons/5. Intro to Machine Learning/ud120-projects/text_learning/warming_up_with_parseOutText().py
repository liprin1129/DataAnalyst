#sys.path.append("../tools/")

#from parse_out_email_text import parseOutText

from nltk.stem.snowball import SnowballStemmer
import string

#print(" ".join(SnowballStemmer.languages))

def parseOutText(f):
    f.seek(0) # go back to beginning of file (annoying)

    all_text = f.read()
    content = all_text.split("X-FileName:")

    words = ""
    if len(content) > 1:
        ## remove punctuation
        text_string = content[1].translate(string.maketrans("", ""), string.punctuation)

        #words = text_string

        from nltk.stem import SnowballStemmer
        
        stemmer = SnowballStemmer("english")

        #for word in text_string.split(" "):
            #print "{0} -> {1}".format(word, stemmer.stem(word))
            #words = words + " " + stemmer.stem(word)

        words = text_string.split(" ")
        singles = [stemmer.stem(word) for word in words]
        words = " ".join(singles)
        
    return words

def main():
    ff = open("test_email.txt", "r")
    text = parseOutText(ff)
    print text
    ff.close()
if __name__ == '__main__':
    main()
