import dropbox

class TransferData:
    def __init__(self,access_token):
        self.access_token=access_token

    def upload_file(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)

        f=open(file_from,'rb')
        dbx.files_upload(f.read(),file_to)

def main():
    access_token='sl.BGLJdlC444mpNhDXcDXKQ53vNNMbzIStUzrZcvA0hD7XQAdsNmqsFCowxaJMzgDiXho4-z7ioUdIZywqjAiXjVsIVzbVD9aAByxpy5JaxyTd09nnLA-yczDXczmczY3NuBdGLB7W0CoS'
    transferData=TransferData(access_token)

    file_from=input("Enter The File Path To Transfer: ")
    file_to=input("Enter The Full Path To Upload Dropbox: ")

    transferData.upload_file(file_from,file_to)
    print("File Has Moved")

main()
        