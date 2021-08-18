import sys
import download_manager

#DATA_URL_COVOST="https://dl.fbaipublicfiles.com/covost/covost_v2.en_cy.tsv.tar.gz"
#DATA_URL_CV_7="http://techiaith.cymru/corpws/CommonVoice/cy/7.0/cv-corpus-7.0-2021-07-21-cy.tar.gz"


#tgz_file_path = download_manager.download(DATA_URL_COVOST, "/data/covost/en-cy")
#download_manager.extract(tgz_file_path)
#tgz_file_path = download_manager.download(DATA_URL_CV_7, "/data/commonvoice/datasets/cy/7.0")
#download_manager.extract(tgz_file_path)

url=sys.argv[1]
data_dir=sys.argv[2]

tgz_file_path = download_manager.download(url, data_dir)
download_manager.extract(tgz_file_path)

