import webbrowser
print("Make sure your file's visibility "+'in Google Drive is set to "Anyone with the link"')
input_link = input('Enter your sharing URL: ')
input_link = input_link[32:]
end = input_link.index('/')
ID = input_link[:end]
download_link = 'https://drive.google.com/uc?export=download&id='+ID
print('This Your Direct Download Link : ',download_link)
ok = False
while not(ok) :
    prompt = input('You Wanna Download The File Right Now ?  Y/N : ')
    ok = prompt =='Y' or prompt =='N' or prompt =='n' or prompt =='y'

if prompt == 'Y' or prompt == 'y'  :
    webbrowser.open(download_link)
    
else :
    print('thank u for your time <3 ')

