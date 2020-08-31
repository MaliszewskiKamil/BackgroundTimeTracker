import Xlib
import Xlib.display
import time

run = True
i = 1

data = {
    "Window" : None,
    "Time" : None
}

while run:

    try:
        time.sleep(1)
        
        display = Xlib.display.Display()
        root = display.screen().root
        windowID = root.get_full_property(display.intern_atom('_NET_ACTIVE_WINDOW'), Xlib.X.AnyPropertyType).value[0]
        window = display.create_resource_object('window', windowID)
        currentWindow = window.get_wm_class()
        print window.get_wm_class()
        data["Window"] = str(window.get_wm_class())
        data["Time"] = data[str(window.get_wm_class())]["Time"]+1
        
        print(data)
        previousWindow = window.get_wm_class()

        

        i = i+1
        if i>10:
            run = False
        
    except KeyboardInterrupt:
        run = False
