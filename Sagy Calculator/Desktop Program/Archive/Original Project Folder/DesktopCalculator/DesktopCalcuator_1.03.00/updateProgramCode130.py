def checkForUpdates():

    CurrentProgramVersion = 10305

    print("Current Version: ",CurrentProgramVersion)

    import urllib.request
    url = "https://raw.githubusercontent.com/YitzchakMeltz/SassyOwl/main/Sagy%20Calculator/Desktop%20Program/SagyDesktopVersion.txt"
    file = urllib.request.urlopen(url)

    for line in file:
        decoded_line = line.decode("utf-8")
        
    decoded_line = decoded_line.replace(".","")

    if CurrentProgramVersion < int(decoded_line):
        print("Update Availible")
        return True
    else:
        print("Program is up to date")
        return False

    return False

def makeUpdateFolder():
    import os

    pathname = os.path.join('C:\ProgramData\SasyOwl\SagyCalculator','Updates')
    print("Pathname for debugging: ",pathname)

    if not os.path.isdir(pathname):
        os.makedirs(pathname)

    else:
        filename = os.path.join('C:\ProgramData\SasyOwl\SagyCalculator','Updates','SagyCalculatorSetup.exe')
        if os.path.exists(filename):
            os.remove(filename)

    return pathname

def downloadUpdate(downloadPath):
    import urllib.request

    filename = downloadPath + '\SagyCalculatorSetup.exe'

    print("Starting update download")

    url = "https://github.com/YitzchakMeltz/SassyOwl/blob/main/Sagy%20Calculator/Desktop%20Program/SagyCalculatorSetup.exe?raw=true"
    urllib.request.urlretrieve(url, filename)

    print("Update download complete")

# is this neccesarry???
def runUpdateInstaller(filename):
    import os
    os.startfile(filename)
    return True

def updateCalc():
    downloadPath = makeUpdateFolder()
    downloadUpdate(downloadPath)
    import os
    filename = os.path.join('C:\ProgramData\SasyOwl\SagyCalculator','Updates','SagyCalculatorSetup.exe')
    return True

def openUpdateInstaller():
    import os,sys, subprocess
    #dir_path = os.path.dirname(os.path.realpath(__file__))
    #filename = os.path.join(dir_path,'ExternalUpdater1.3.0.exe')
    #print("Yitzchak: ",filename)
    #subprocess.call(filename)
    filename = os.path.join('C:\ProgramData\SasyOwl\SagyCalculator','Updates','SagyCalculatorSetup.exe')
    subprocess.call(filename)
    print("Hello, How are you?")