import subprocess
from pathlib import Path

def getUrls(selectedWindow):
    parentDir = Path(__file__).resolve().parent

    selectedWindowUrls = subprocess.run(
        ["osascript", str(parentDir / "getUrls.applescript"), selectedWindow],
        capture_output=True,
        text=True
    )

    urls = []

    for selectedWindowUrl in selectedWindowUrls.stdout.splitlines():
        urls.append(selectedWindowUrl)
    
    return urls



if __name__ == "__main__":
    selectedWindow = "AppleScript Beginner Tutorial"
    urls = getUrls(selectedWindow)
    print(urls)