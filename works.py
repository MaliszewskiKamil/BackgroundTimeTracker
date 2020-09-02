import Xlib
import Xlib.display
import time

import pandas as pd


run = True

i=0
second = 1

dataDict = {'Window Name': '', 'Time Spent': 0}

window = ['']
timeSpent = [0]
dataSet = list(zip(window, timeSpent))

df = pd.DataFrame(data = dataSet, columns=['Window Name', 'Time Spent'])


while run:

    try:
        time.sleep(1)
        
        display = Xlib.display.Display()
        root = display.screen().root
        windowID = root.get_full_property(display.intern_atom('_NET_ACTIVE_WINDOW'), Xlib.X.AnyPropertyType).value[0]
        window = display.create_resource_object('window', windowID)
        currentWindow = str(window.get_wm_class())
        
        previousWindow = window.get_wm_class()

        currentData = {'Window Name': currentWindow, 'Time Spent': second}
        index = 1
        for windowName in df['Window Name']:
            print('WindowName: ', windowName)
            if  currentWindow in df.values:
                print("changing value")
                print('Wind: ', windowName, " Curr: ", str(currentWindow))
                oldValue = df.loc[index, 'Time Spent']
                print('Old Value: ' ,oldValue)
                newValue = oldValue+second
                print('new Value: ', newValue)
                df._set_value(index, 'Time Spent', newValue)
                break
            else:
                print("Appending")
                currentDataSeries = pd.Series(currentData)
                df = df.append(currentDataSeries, ignore_index=True)
                break
            index += 1




        i = i+1
        if i>10:
            print(df)
            run = False
        
    except KeyboardInterrupt:
        run = False
