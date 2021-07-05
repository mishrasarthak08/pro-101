import dropbox
import os
from dropbox.files import WriteMode

class Transferdata:
    def __init__(self,access_token):
        self.access_token = access_token

    def uploadfile(self,source,destination):
        dbx = dropbox.Dropbox(self.access_token)
        for root,folder,files in os.walk(source):
            for i in files:
                localpath = os.path.join(root,i) 
                relativepath = os.path.relpath(localpath,source)
                dropboxpath = os.path.join(destination,relativepath)

                f = open(localpath , "rb")   
                dbx.files_upload(f.read() , dropboxpath,mode = WriteMode("overwrite"))

def main():
    access_token = "DchsX-ktqsoAAAAAAAAAARUvSDUQoqXpzi89BUTTOWOEzbqQ_RUBa1px_9HBD6L5"
    filetransfer = Transferdata(access_token)

    source = str(input("enter your Source : - ")) 
    destination = input("enter the destination : - ")  

    filetransfer.uploadfile(source,destination)
    print("file has been moved!")

main()                     