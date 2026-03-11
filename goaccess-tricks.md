## goaccess a terminal log parser


#### haproxy logs format

```bash
goaccess -f haproxy.log --log-format='%^]%^ %h:%^ [%d:%t.%^] %^/%^/%^/%^/%L/%^ %s %b %^"%r"' --date-format='%d/%b/%Y' --time-format='%H:%M:%S'
```


#### access keys

```bash
F1 or hMain help.
F5Redraw main window.
qQuit the program, current window or collapse active module
o or ENTERExpand selected module or open window
0-9 and Shift + 0Set selected module to active
jScroll down within expanded module
kScroll up within expanded module
cSet or change scheme color
^ fScroll forward one screen within active module
^ bScroll backward one screen within active module
TABIterate modules (forward)
SHIFT + TABIterate modules (backward)
sSort options for active module
/Search across all modules (regex allowed)
nFind position of the next occurrence
gMove to the first item or top of screen
Gmove to the last item or bottom of screen
```

