
def checkForUpdates():

    CurrentProgramVersion = 10402

    print("Current Version: ",CurrentProgramVersion)

    import urllib.request
    url = "https://raw.githubusercontent.com/YitzchakMeltz/SassyOwl/main/Sagy%20Calculator/Desktop%20Program/SagyDesktopVersion.txt"
    file = urllib.request.urlopen(url)

    for line in file:
        decoded_line = line.decode("utf-8")
        
    decoded_line = decoded_line.replace(".","")
    print(int(decoded_line))

    if CurrentProgramVersion < 99999999:
    #if CurrentProgramVersion < int(decoded_line):
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

def downloadUpdate(downloadPath, dlg):
    import urllib.request
    from mainControl import mainControl

    filename = downloadPath + '\SagyCalculatorSetup.exe'

    print("Starting update download")

    url = "https://github.com/YitzchakMeltz/SassyOwl/blob/main/Sagy%20Calculator/Desktop%20Program/SagyCalculatorSetup.exe?raw=true"
    urllib.request.urlretrieve(url, filename, lambda blocknum, blocksize, totalsize: Handle_Progress(dlg, blocknum, blocksize, totalsize))

    print("Update download complete")

def Handle_Progress(dlg, blocknum, blocksize, totalsize):
        from mainControl import mainControl

        ## calculate the progress
        readed_data = blocknum * blocksize
 
        if totalsize > 0:
            download_percentage = readed_data * 100 / totalsize
            dlg.UpdatingDlgProgressBar.setValue(download_percentage)

        if (readed_data * 100 / totalsize) >  99:
            dlg.close()

def updateCalc(dlg):
    downloadPath = makeUpdateFolder()
    downloadUpdate(downloadPath, dlg)
    import os
    filename = os.path.join('C:\ProgramData\SasyOwl\SagyCalculator','Updates','SagyCalculatorSetup.exe')
    return True