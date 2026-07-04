import subprocess

def rename():
    selectedWindowUrls = subprocess.run(
        ["osascript", "getUrls.applescript", "AppleScript Beginner Tutorial"],
        capture_output=True,
        text=True
    )

    urls = []

    for selectedWindowUrl in selectedWindowUrls.stdout.splitlines():
        urls.append(selectedWindowUrl)
    
    print(urls)



if __name__ == "__main__":
    rename()