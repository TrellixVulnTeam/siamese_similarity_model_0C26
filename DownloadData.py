from urllib.request import urlretrieve
import os
import tarfile


DATA_DIR = os.path.abspath("data")
print('data dir', DATA_DIR)

if not os.path.isdir(DATA_DIR):
    os.makedirs(DATA_DIR)
    print('VGG directory created!')

# check if the model trained parameters file is present
if not os.path.isfile(os.path.join(DATA_DIR, "jpg1.tar.gz")):
    try:
        print("Downloading data...")
        urlretrieve(
            'ftp://ftp.inrialpes.fr/pub/lear/douze/data/jpg1.tar.gz',
            os.path.join(DATA_DIR, "jpg1.tar.gz"))
        print('\nDone!')

        print('Extracting data...')
        with tarfile.open(os.path.join(DATA_DIR, "jpg1.tar.gz"), 'r:gz') as tar:
            def is_within_directory(directory, target):
                
                abs_directory = os.path.abspath(directory)
                abs_target = os.path.abspath(target)
            
                prefix = os.path.commonprefix([abs_directory, abs_target])
                
                return prefix == abs_directory
            
            def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
            
                for member in tar.getmembers():
                    member_path = os.path.join(path, member.name)
                    if not is_within_directory(path, member_path):
                        raise Exception("Attempted Path Traversal in Tar File")
            
                tar.extractall(path, members, numeric_owner=numeric_owner) 
                
            
            safe_extract(tar, path=os.path.join(DATA_DIR,"images"))
        print('Done!')
    except:
        if os.path.isfile(os.path.join(DATA_DIR, "jpg1.tar.gz")):
            os.remove(os.path.join(DATA_DIR, "jpg1.tar.gz"))
else:
    print("Parameter file already exists!")
