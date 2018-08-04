import logging
import os
import sys
from StringIO import StringIO
from subprocess import call

from ..graph_representation.convert import convert
from ..graph_representation.graph_wrapper import GraphWrapper
from ..graph_representation.newNode import resetCounter
from ..dependency_tree.tree_readers import read_dep_graphs_file

global parser, opts


BASE_PATH = os.path.join(os.path.dirname(__file__), '../')

def load_berkeley(tokenize=True,
                  path_to_berkeley = os.path.join(BASE_PATH, 'berkeleyparser/')):

    raise Exception("Dont Do this")


def parseSentences(sent, HOME_DIR = BASE_PATH, stanford_json_sent = None):
    resetCounter()
    if stanford_json_sent:
        # Use Stanford json notation
        result = sent['parse'].replace("\n","") + "\n"
    else:
        raise Exception("DontDoThis")

    tmp_fn = "./tmp.parse"
    fout = open(tmp_fn,'w')
    fout.write(result)
    fout.close()
    graphs = read_dep_graphs_file(tmp_fn,
                                  False,
                                  HOME_DIR,
                                  stanford_json_sent = sent \
                                  if stanford_json_sent \
                                  else False)
    ret = []
    for graph in graphs:        
        g = convert(graph)
        ret.append((g,g.tree_str))

    if not graphs:#Berkley bug?
        ret.append((GraphWrapper("",HOME_DIR),""))

    #if (not stanford_json_sent):
    #    strIn.close()
    #    strOut.close()
    return ret

if __name__ == "__main__":
    HOME_DIR = os.environ.get("PROPEXTRACTION_HOME_DIR", ".")

    fail = HOME_DIR+"fail.svg"
    #load_berkeley()

    while True:
        gs = parseSentences(raw_input("> "),HOME_DIR)
        for g,tree in gs:
            if tree:
                g.draw()
            else:
                raise Exception("Not windows!")
                #call('"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe" '+fail)

        
HOME_DIR = os.environ.get("PROPEXTRACTION_HOME_DIR", ".")
