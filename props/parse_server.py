#!/usr/bin/env python
#coding:utf8
import sys

from bottle import run, get, request
from props.applications.run import load_berkeley
from props.applications.run import parseSentences
from visualizations.brat_visualizer import BratVisualizer

try:
    PORT=int(sys.argv[1])
except:
    PORT=8081

@get('/gparse')
def gparse():
    print "in gparse"
    sent = request.GET.get('text','').strip()
    b = BratVisualizer()
    print sent
    sents = sent.strip().replace(". ",".\n").replace("? ","?\n").replace("! ","!\n").split("\n")
    sent = sents[0]
    gs = parseSentences(sent)
    g,tree = gs[0]
    
    ret = b.to_html(g)
       
    ret = ret.replace('PROPOSITIONS_STUB', '<br>'.join([str(prop) for prop in g.getPropositions('html')]))
    print "returning...." 
    return ret

load_berkeley()
run(host='',port=PORT)
