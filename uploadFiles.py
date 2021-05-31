from os import access
import dropbox

class TransferData:
    def __init__(self, token):
        self.token=token

    def dropFile(self, file_get, file_deposit):
        dbx = dropbox.Dropbox(self.token)

        f=open(file_get, 'rb')
        dbx.files_upload(f.read(), file_deposit)

def mainRoute():
    token='b5SdnNd892AAAAAAAAAAAe72wyG_fQLjCllx9K8phBmQ6DqyRTvPqBojyW2bTw8b'
    MoveData=TransferData(token)

    file_get= input("Enter the file path to transfer: ")
    file_deposit= input("enter the complete path to upload to dropbox: ")  

    MoveData.dropFile(file_get, file_deposit)
    print("Done, Your file has been moved!")
        