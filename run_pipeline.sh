#!/bin/sh
# Usage:
#     run_pipeline <raw input file>
# Run the Stanford parser over raw sentences file (one per line)
# Following by an invokation of PropS over the json output
# Note:
#   * This assumes that CORENLP_HOME points to the corenlp home directory (containing all jars)
#   * We use the Stanford dependency format (not Universal Dependencies)
#   * We use the makeCopulaHead flag
#   * We assume the input file is split by sentences.
#     This is indicated in stanford_parser.props
#     (See https://github.com/stanfordnlp/CoreNLP/issues/415)
set -e
# temporary hack
export CORENLP_HOME=/Users/prasad/packages/stanford-corenlp-full-2018-02-27
# Run Stanford parser
java -cp "$CORENLP_HOME/*" -Xmx2g edu.stanford.nlp.pipeline.StanfordCoreNLP \
    -annotators tokenize,ssplit,pos,parse \
    -file $1 \
    -props stanford_parser.props \
    -outputFormat json \
    -parse.originalDependencies -parse.flags " -makeCopulaHead"

# Run PropS on output
# (Stanford outputs to ${1}.json)
# TODO: Stanford doesn't seem to allow printing to standard output, so direct piping wasn't possible
cat ${1}.json | python props/applications/parse_props.py -t --oie --corenlp-json-input
