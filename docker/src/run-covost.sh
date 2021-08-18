#!/bin/bash
COVOST_DATA_DIR=/data/covost
COVOST_WORK_DIR=~/covost

COVOST_DATA_URL="https://dl.fbaipublicfiles.com/covost/covost_v2.en_cy.tsv.tar.gz"

mkdir -p $COVOST_WORK_DIR
mkdir -p $COVOST_DATA_DIR

cd $COVOST_WORK_DIR

if [ ! -f $COVOST_WORK_DIR/data/covost_v2.en_cy.tsv ]
then
	echo "Downloading CoVOST English to Welsh translations dataset..."
	python3 /code/python/fetch.py $COVOST_DATA_URL $COVOST_WORK_DIR/data
fi

# Produce a filtered list of sentences from the original CoVOST dataset. 
cut -f2 $COVOST_WORK_DIR/data/covost_v2.en_cy.tsv | sort | uniq -u | python3 /code/python/filter.py > $COVOST_DATA_DIR/cy.txt || exit;
wc -l $COVOST_DATA_DIR/cy.txt

# do some reporting on any oov words found during filtering
sort filter.oov.log | uniq -c | sort -nr > en.oov
sort filter.oov.lex.cy.log | uniq -c | sort -nr > cy.lex.oov

# Create random samples for various human validators to read. 
# see https://github.com/common-voice/common-voice/blob/main/docs/SENTENCES.md#bulk-submission
#
HUMAN_VALIDATORS=2
for i in $(seq 1 $HUMAN_VALIDATORS)
do
       cat $COVOST_DATA_DIR/cy.txt | shuf -n 662 > $COVOST_DATA_DIR/cy.662.$i.txt
done

