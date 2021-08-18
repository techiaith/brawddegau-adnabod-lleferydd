import os
import tarfile
import urllib.request
from urllib.parse import urlparse

from pathlib import Path
from tqdm import tqdm

class DownloadProgressBar(tqdm):
    def update_to(self, b=1, bsize=1, tsize=None):
        if tsize is not None:
            self.total = tsize
        self.update(b * bsize - self.n)


def download(data_file_url, output_dir):
    file_name=os.path.basename(urlparse(data_file_url).path)
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    output_file_path=os.path.join(output_dir, file_name)

    if not os.path.isfile(output_file_path):
        with DownloadProgressBar(unit='B', unit_scale=True, miniters=1, desc=data_file_url.split('/')[-1]) as t:
            urllib.request.urlretrieve(data_file_url, filename=output_file_path, reporthook=t.update_to)

    return output_file_path


def extract(targz_file_path):
    # extract.
    if targz_file_path.endswith(".tar.gz"):
        print ("Extracting...")
        model_dir = Path(targz_file_path).parent.absolute()
        tar = tarfile.open(targz_file_path, "r:gz")
        tar.extractall(model_dir)
        tar.close()

    #Path(output_file_path).unlink()
