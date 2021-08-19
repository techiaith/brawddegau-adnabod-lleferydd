# A selection of sentences from the CoVoST corpus suitable for audio recording to be used to train Welsh Speech Recognition models

[Darllen y README yn Gymraeg](README.md)

The `cy.txt` file in this folder contains 101,535 out of the 232,037 unique Welsh sentences contained in version 2 of the CoVoST corpus [1].

Because CoVoST's Welsh sentences are machine translations of Common Voice's English sentences, 130,502 sentences were filtered that did not meet the following criteria:

 * short sentence, less than 15 words.
 * does not include numbers, acronyms and abbreviations.
 * all words are present in a Welsh language lexicon [2] or in a list of [20,000 additional words we have allowed](../../src/python/nlp/cy/oov_welsh.txt) 
 
CoVoST's Welsh sentences included, in our opinion, an excess of American English proper nouns that we considered less relevant for speech recognition to the Welsh language and the Welsh cultural context. Excluding them will allow us to add proper names that are more representative of Welsh language context.

We have followed [Mozilla's recommended method for bulk submissions](https://github.com/common-voice/common-voice/blob/main/docs/SENTENCES.md#bulk-submission) to validate the quality of our selection of 101,353 sentences. Files `cy.662.1.txt` and `cy.662.2.txt` have been reviewed by human editors who have confirmed only 5% of sentences from both files are problematic for recording.
 
It is important to note that this selection of Welsh sentences does not necessarily represent accurate, polished translations of the original English sentences, but that they have been judged to be suitable enough to serve as sentences for training speech recognition models where the exact meaning of the sentences is not such an important consideration. This should not be interpreted to mean that we believe that the quality of the CoVoST corpus is adequate for training any type of translation models.



# References

[1] - **CoVoST 2 and Massively Multilingual Speech-to-Text Translation.**<br/>Changhan Wang, Anne Wu, & Juan Pino. (2020).  arXiv preprint arXiv:2007.10310, 2020 - arxiv.org


[2] - **techiaith/lecsicon-cymraeg-bangor: Lecsicon Cymraeg Prifysgol Bangor // Bangor University Welsh Language Lexicon.**<br/>Gareth Watkins, Gruffudd Prys & Dewi Bryn Jones (2021).  https://doi.org/10.5281/zenodo.5211667.
