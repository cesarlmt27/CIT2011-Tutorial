import hashlib
import checkThreat

def getHash(path):
    algs =  ['MD5','SHA1', 'SHA256']
    res_hex = {
        'MD5': "",
        'SHA1': "",
        'SHA256': ""
    }
    
    for alg in algs:
        hash_obj = hashlib.new(alg)

        with open(path, 'rb') as archivo:
            for bloque in iter(lambda: archivo.read(4096), b''):
                hash_obj.update(bloque)
                
        res_hex[alg] = hash_obj.hexdigest()
  
    return res_hex


# esta funcion crea la info y formatea
def formatAndGetData(path):
    
    hashes = getHash(path)
    
    # Con este formato, podriamos usar la API SQL DE Spark para filtrar:
    # Ejemplos: - Todos los archivos .php que esten en la lista negra
    #           - Todos los archivos .js cuyo hash md5 esté en la lista negra, pero su hash sha256 no.
    data = {
        "path": path,
        "fileName": path[path.rfind("\\") + 1:path.rfind(".")] if path.rfind(".") != -1 else path[path.rfind("\\") + 1:],
        "ext": path[path.rfind(".") + 1:] if path.rfind(".") != -1 else "",
        "digest": hashes,
        "threat": checkThreat.isThreat(hashes)
    }
    return data



