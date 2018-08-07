import json
from .run import parseSentences
FILE_NAME = "/Users/prasad/code/others/props/turnipsInc.txt.json"


if __name__ == "__main__":
    with open(FILE_NAME) as inF:
        l = "".join(inF.readlines())
        j = json.loads(l)
        sents = j['sentences']
        gs = [parseSentences(s,'.',True) for s in sents]
        ps = [gsi[0] for gsi in gs]
        gg = [p[0] for p in ps]

        mu = [ggi.getPropositions("html") for ggi in gg]
        x = 3
        y = 4
    print "Done: 1",len(gs)