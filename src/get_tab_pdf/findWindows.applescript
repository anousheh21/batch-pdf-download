tell application "Google Chrome"
	set activeTabs to title of active tab of every window whose visible is true
end tell

set AppleScript's text item delimiters to linefeed
set output to activeTabs as text
