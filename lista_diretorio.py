import os,glob

list = []

def lista(raiz,caminho="/"):
    #guarda temporariamente
    arq = open("/tmp/diretorio","w")

    if(os.path.isdir(raiz+caminho)):
        os.chdir(raiz+caminho)
        for arquivo in glob.glob("*"):
            if(os.path.isdir(raiz+caminho+arquivo)):                
                lista(raiz+caminho+arquivo)
                list.append(raiz+caminho+arquivo)
                #print(raiz+caminho+arquivo)                
            else:
                    list.append(raiz+caminho+arquivo)
                    #lista(raiz+caminho+arquivo)
                    #print(raiz+caminho+arquivo)                
    else:        
        lista(raiz+caminho+arquivo)
        list.append(raiz+caminho+arquivo)
            
    return list
    
def main():    
    for list in lista("/home"):
        try:
            print(list)
        except Exception as e:
            pass

main()
