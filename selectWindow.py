from simple_term_menu import TerminalMenu
import subprocess

def selectWindow():
    activeTabs = subprocess.run(
        ["osascript", "findWindows.applescript"],
        capture_output=True,
        text=True
    )

    windows = []

    for activeTab in activeTabs.stdout.splitlines():
        windows.append(activeTab)

    menu = TerminalMenu(windows)
    selectedIndex = menu.show()
    selectedWindow = windows[selectedIndex]

    print(selectedWindow)


if __name__ == "__main__":
    selectWindow()
