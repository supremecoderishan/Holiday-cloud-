import os
import dropbox
from dropbox.files import WriteMode

class TransferData:
    def __init__(self,acces_token):
        self.acces_token = acces_token

    def upload_file(self,file_from, file_to):
        dbx = dropbox.Dropbox(self.acces_token)

        for root, dirs, files in os.walk (file_from):

            for filename in files:

                local_path = os.path.join(root, filename)

                relative_path = os.path.relpath(local_path,file_from)
                dropbox_path = os.path.join(file_to, relative_path)

                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))
def main():
    acces_token = 'sl.BLq5lNuD7FHoX5oDAScHzCprIQulHUtLtVqmBXhW6Phn7tFk15EBjSmx5oBbzgdRvmj4QKzt7_FkVIoLJ6oxdQo21VYiqWH3dt9yJLxpDq9qCNqX3xx7nIFGGigSuuIn-sON-lc'
    transferData= TransferData(acces_token)

    file_form = str(input(" Enter the folder path to transfer : -"))
    file_to = input("Enter the full path to upload to dropbox : -")

    transferData.upload_file(file_form,file_to)
    print("file has been been moved ")

    main()
