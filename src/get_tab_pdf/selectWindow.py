from pathlib import Path
from simple_term_menu import TerminalMenu
import subprocess

def selectWindow():
    parentDir = Path(__file__).resolve().parent

    activeTabs = subprocess.run(
        ["osascript", str(parentDir / "findWindows.applescript")],
        capture_output=True,
        text=True
    )

    windows = []

    for activeTab in activeTabs.stdout.splitlines():
        windows.append(activeTab)

    menu = TerminalMenu(windows)
    selectedIndex = menu.show()
    selectedWindow = windows[selectedIndex]

    return selectedWindow


if __name__ == "__main__":
    selectedWindow = selectWindow()
    print(selectedWindow)
