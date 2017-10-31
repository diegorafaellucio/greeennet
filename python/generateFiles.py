import sys,os
from shutil import copyfile

root = "/home/diego/Experimentos/"
path = os.path.join(root, "spectrograms/")
txtPath = os.path.join(root,"Txts/")
experimentsPath = os.path.join(root,"Tests/")

if not os.path.exists(txtPath):
    os.makedirs(txtPath)

if not os.path.exists(experimentsPath):
    os.makedirs(experimentsPath)

for currentPath,directories,files in os.walk(path):
    for directory in directories:
        for fold,foldDirectories,foldFiles in os.walk(os.path.join(currentPath,directory)):
            foldOutputFile = open(os.path.join(txtPath,directory+".txt"),"w")
            #print os.path.join(txtPath,directory+".txt")
            for foldFile in foldFiles:
                fileSplited = foldFile.split("-")
                foldOutputFile.write(os.path.join(fold,foldFile)+" "+fileSplited[0]+"\n") 
            foldOutputFile.close() 


for txtPath,txtDirectories,txtFiles in os.walk(txtPath):
    for txtFile in txtFiles:
        foldName = txtFile.split(".")[0]
        foldPath = os.path.join(experimentsPath,foldName)
        foldDataPath = os.path.join(experimentsPath,foldName,"data")
        trainPath = os.path.join(foldPath,"train")
        valPath = os.path.join(foldPath,"val")

        if not os.path.exists(foldDataPath):
            os.makedirs(foldDataPath)

        if not os.path.exists(foldPath):
            os.makedirs(foldPath)

        

        foldFile = open(os.path.join(txtPath,txtFile), "r") 
        content = foldFile.read()
        foldFileContent = ""
        lines = content.split("\n")
        for line in lines:
            if line != "":
                print line
                filePath = line.split(" ")[0]
                classId = line.split(" ")[1]
                fileName = filePath.split("/")[6]
                #print filePath 
                #print os.path.join(valPath,fileName)
                #copyfile(filePath, os.path.join(valPath,fileName))
                foldFileContent += os.path.join(filePath)+ " " +str(int(classId)-1) +"\n"
        foldFile.close()

        testfile = open(os.path.join(foldPath,"val.txt"), "w") 
        testfile.write(foldFileContent)
        testfile.close()

        
        trainfile = open(os.path.join(foldPath,"train.txt"), "w") 

        for txtFile2 in txtFiles:

            if txtFile != txtFile2:

                foldFile = open(os.path.join(txtPath,txtFile2), "r") 
                content = foldFile.read()
                foldFileContent = ""
                lines = content.split("\n")
                for line in lines:
                    if line != "":
                        print line
                        filePath = line.split(" ")[0]
                        classId = line.split(" ")[1]
                        fileName = filePath.split("/")[6]
                        #print filePath 
                        #print os.path.join(valPath,fileName)
                        #copyfile(filePath, os.path.join(trainPath,fileName))
                        foldFileContent += os.path.join(filePath)+ " " +str(int(classId)-1) +"\n"
                foldFile.close()


                trainfile.write(foldFileContent)

        trainfile.close()
