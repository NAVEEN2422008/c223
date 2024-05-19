import PyPDF2 as pd
filename=input('path to the file :')
filename=filename.strip()
file=open(filename,'rb')
pdfreader=pd.PdfReader(file)
tried=0
if not pdfreader.is_encrypted:
    print('The file is not password protected! You can successfully open it!')
else:
    worldlistfile=open('wordlist.txt','r',errors='ignore')
    body=worldlistfile.read().lower()
    word=body.split('\n')
    for i in range(len(word)):
        w=word[i]
        print('try to decode password by : {}'.format(w))
        result=pdfreader.decrypt(w)
        if result==1:
            print('success!! password is:'+w)
            break
        elif result==0:
            tried=tried+1
            print('try again')
            print('password tried :'+str(tried))
            continue