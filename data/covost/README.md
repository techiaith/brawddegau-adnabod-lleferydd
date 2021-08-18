# Detholiad o frawddegau o gorpws CoVoST sy'n addas ar gyfer recordio sain i'w defnyddio i hyfforddi modelau Adnabod Lleferydd Cymraeg

[Read this README in English](README_en.md)

Mae'r ffeil `cy.txt` yn y ffolder hon yn cynnwys 101,535 o'r 232,037 o frawddegau Cymraeg unigryw sydd wedi'u cynnwys yn fersiwn 2 o'r corpws CoVoST [1].

Oherwydd bod brawddegau Cymraeg CoVoST yn gyfieithiadau peirianyddol o frawddegau Saesneg Common Voice, eithrwyd 130,502 o frawddegau nad ydynt yn cwrdd â'r meini prawf canlynol:

 * brawddeg byr, llai na 15 gair. 
 * ddim yn cynnwys rhifau, acronymau a talfyriadau.
 * pob gair yn lecsicon y Gymraeg [2] neu mewn rhestr o tua [20,000 air rydym wedi caniatáu yn ychwanegol](../../src/python/nlp/cy/oov_welsh.txt)  
 
 Roedd brawddegau Cymraeg CoVoST hefyd yn cynnwys, yn ein barn ni, gormodedd o enwau priod o Saesneg America yr oeddem yn eu hystyried yn llai perthnasol ar gyfer adnabod lleferydd i'r Gymraeg a'r cyd-destun diwylliannol Cymreig. Bydd eu heithrio yn ein galluogi i ychwanegu enwau priod sy'n fwy cynrychioladol o'r cyd-destun Cymreig a geir yn y Gymraeg.

Rydym wedi dilyn [dull argymhellir gan Mozilla ar gyfer cyflwyniadau swmp](https://github.com/common-voice/common-voice/blob/main/docs/SENTENCES.md#bulk-submission) i ddilysu ansawdd ein ddetholiad o 101,353 frawddeg. Mae ffeiliau `cy.662.1.txt` a ` cy.662.2.txt` wedi'u hadolygu gan olygyddion dynol sydd wedi cadarnhau bod 5% o frawddegau o'r ddau ffeil yn broblemus ar gyfer recordio.

Mae'n bwysig nodi nad yw'r casgliad hwn o frawddegau Cymraeg o reidrwydd yn cynrychioli cyfieithiadau cywir, graenus o'r brawddegau Saesneg gwreiddiol, ond eu bod yn hytrach wedi'u barnu'n ddigon addas ar gyfer gweithredu fel brawddegau hyfforddi ar gyfer hyfforddi modelau adnabod lleferydd lle nad yw union ystyr y brawddegau yn ystyriaeth mor bwysig. Nid ddylid dehongli hyn i olgyu ein bod yn credu bod safon corpws CoVoST yn ddigonol ar gyfer hyfforddi unrhyw fath o fodelau cyfieithu.


# Cyfeiriadau

[1] - **CoVoST 2 and Massively Multilingual Speech-to-Text Translation.**<br/>Changhan Wang, Anne Wu, & Juan Pino. (2020).  arXiv preprint arXiv:2007.10310, 2020 - arxiv.org


[2] - **techiaith/lecsicon-cymraeg-bangor: Lecsicon Cymraeg Prifysgol Bangor // Bangor University Welsh Language Lexicon.**<br/>Gareth Watkins, Gruffudd Prys & Dewi Bryn Jones (2021).  https://doi.org/10.5281/zenodo.5211667.
