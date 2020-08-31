import wnck

x = None

if wnck is not None:
    screen = wnck.screen_get_default()
    print(screen)
    window = screen.get_active_window()
    print("window")
    print(window)

