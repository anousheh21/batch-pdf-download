on run argv
    set selectedActiveTab to item 1 of argv

    tell application "Google Chrome"
        set selectedWindow to first window whose title of active tab is selectedActiveTab
        set selectedWindowUrls to URL of every tab of selectedWindow
    end tell

    set AppleScript's text item delimiters to linefeed
    set output to selectedWindowUrls as text
end run
