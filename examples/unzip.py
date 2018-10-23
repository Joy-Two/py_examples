import sys
import zipfile

if __name__=="__main__":
    zip_ref = zipfile.ZipFile(sys.argv[1], 'r')
    print(sys.argv[1])
    zip_ref.extractall(sys.argv[1].replace('.zip',''))
    zip_ref.close()