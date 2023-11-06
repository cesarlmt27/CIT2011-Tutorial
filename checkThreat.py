def isThreat(hashes):
    i = 0
    forbidden = [" ", "#", "", "\n"]
    
    # La idea seria que se le envien las fuentes de IOCs al servidor Spark para simular un flujo de datos
    IOCS_SOURCE = './source.txt'
    

    with open(IOCS_SOURCE, 'r', encoding="utf8") as archivo:
     for linea in archivo:
         
        cur_IOC = linea[:linea.find(';')]
        
        # estos son los 3 hashes(md5, sha1 y sha256) del archivo
        for hash in hashes:
           if hashes[hash] == cur_IOC:
               return True
    
    return False     
         
isThreat("")