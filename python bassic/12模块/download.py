#!/usr/bin/env python3
import os
import os.path
import requests

def download(url):
    '''
    Download the file from the specified URL and save it to the
    current directory
    
    :arg url:The URL to download the file
    '''
    req = requests.get(url)
    #First ,check if there are any files
    if req.status_code == 404:
        print("No such file found at %s" % url)
        return
    filename = url.split('/')[-1]
    with open(filename,'wb') as fobj:
        fobj.write(reqi.content)
    print("Download over.")

if __name__ == '__main__':
    url = input('Enter a URL:')
    download(url)
