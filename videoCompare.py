import datetime
import sys
import os
import pathlib
import cv2

helpString = ('\n(h)elp: display this menu \n'
'(e)xit: exit program \n'
'(s)can: scan selected directory for selected type of file\n'
'(d)ir: change directory to scan\n'
'(t)ype: change type of file to scan for\n')

dir = '.'       
type = 'mp4'    
comValid = ['help', 'exit', 'scan', 'dir', 'type']
recursionFlag=0
ABS_TIME = 0.001
ABS_SIZE = 10

def setDir(input):
    global dir
    global recursionFlag
    recursionFlag = 0
    if input[0]=='\"' and input[-1]=='\"':
        input = input[1:-1]
    dir = input
    
def setType(input):
    global type
    if input[0]=='.':
        input = input[1:]
    type = input

def scanDir(dir, type):
    files = []

    try:
        files = [f for f in pathlib.Path(dir).iterdir() if f.is_file() and str(f)[-len(type):]==type]
        dirs = [f for f in pathlib.Path(dir).iterdir() if not f.is_file()]
        if len(dirs)>0:
            global recursionFlag
            recursionFlag = 1
    except:
        print()
        print('Bad Directory')
        print()
        return
        
    deets=[]

    for d in dirs:
        scanDir(d, type)
        
    for f in files:
        try:
            data = cv2.VideoCapture(str(f))
            
            frames = data.get(cv2.CAP_PROP_FRAME_COUNT)
            fps = data.get(cv2.CAP_PROP_FPS)
            width  = int(data.get(cv2.CAP_PROP_FRAME_WIDTH))
            height = int(data.get(cv2.CAP_PROP_FRAME_HEIGHT))

            seconds = frames/fps

            deets = deets + [(seconds, width, height, str(f))]
        except:
            print(f"BAD FILE {f}")
    
    
    print()
    print('---{}'.format(dir))
    if len(deets)==0 and recursionFlag:
        print()
        print(f'No {type} Files Found')
        print()
        return
        

    deets.sort()

    similarFilesFlag=1
    

    print()
    for i in range(len(deets)-1):
        time, width, height, name = deets[i]
        size = os.stat(name).st_size
        timeN, widthN, heightN, nameN = deets[i+1]
        sizeN = os.stat(nameN).st_size
        
        if abs(timeN-time)<ABS_TIME and abs(size-sizeN)<ABS_SIZE:
            print()
            print(name.split('\\')[-1])
            print(datetime.timedelta(seconds=time))
            print(str(int(size/1024)) + 'KB')
            print()
            print(nameN.split('\\')[-1])
            print(datetime.timedelta(seconds=timeN))
            print(str(int(sizeN/1024)) + 'KB')
            print()
            print('---')
            print()
            similarFilesFlag=0
            
    if similarFilesFlag:
        print('No similar files found')
        print('---')     

setDir(input('Input directory to scan: '))
setType(input('Input type of file to scan: '))

print(helpString)

while(1):
    com = input('What would you like to do? (h for help): ')
    if com.lower() not in comValid and com.lower() not in [c[0] for c in comValid]:
        print('What?')
    elif com.lower() in ['e', 'exit']:
        exit()
    elif com.lower() in ['h', 'help']:
        print(helpString)
    elif com.lower() in ['d', 'dir']:
        print()
        setDir(input('Input directory to scan: '))
        print()          
    elif com.lower() in ['t', 'type']:
        print()
        setType(input('Input type of file to scan: '))
        print()
    elif com.lower() in ['s', 'scan']:
        scanDir(dir, type)