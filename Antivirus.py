import hashlib

#Set necessari varables

database = ''
virus = ''
database_num = int('48')

#Load hash database
        print('Loading HASH database')

        with open('AntivirusDabase\\Virus.txt') as file:
                for line in file:
                    database = database + line + ''
                print('Database ' + '0' + ' load')

        comptador=1
        
        for i in range(0, database_num):
            
            with open("AntivirusDabase\\Virus" + str(comptador) + '.txt') as file:
                for line in file:
                    database = database + line + ''
                print('Database ' + str(comptador) + ' load')
                
                comptador = comptador + 1
              

#Make funcion's

def getmd5file(archivo):
    try:
        hashmd5 = hashlib.md5()
        with open(archivo, "rb") as f:
            for bloque in iter(lambda: f.read(4096), b""):
                hashmd5.update(bloque)
        return hashmd5.hexdigest()
    except Exception as e:
        print("Error: %s" % (e))
        return ""
    except:
        print("Error desconocido")
        return ""
while True:    
    #Calculate the hash of the file
    file = input('Enter route of file ')
    HASH_file = getmd5file(file)

    if HASH_file == '':
        print('This file can\'t be loaded')
        input()
    else:
        print('Hash is ' + HASH_file)

        print('Checking HASH in database')

        if HASH_file in database:
            virus = True
        else:
            virus = False

        if virus == True:
            print('Is a virus')
        else:
            print('Is not a virus')
        input()
