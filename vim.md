## VIM

find n replace string vim

#### Good reads
https://vim.rtorr.com/

https://www.google.com/search?q=vim+go+to+end+of+line&ie=utf-8&oe=utf-8&client=firefox-b-ab

http://vim.wikia.com/wiki/Search_and_replace

https://spin.atomicobject.com/2016/04/19/vim-commands-cheat-sheet/

https://alvinalexander.com/linux/vi-vim-editor-end-of-line

## Basic movement commands for vim:

	e 
Move to the end of a word.

	w 
Move forward to the beginning of a word.

	3w 
Move forward three words.

	W 
Move forward a WORD (any non-whitespace characters).

	b 
Move backward to the beginning of a word.

	3b 
Move backward three words.

	$ 
Move to the end of the line.
	
	0 
Move to the beginning of the line.

	^ 
Move to the first non-blank character of the line.

	) 
Jump forward one sentence.

	( 
Jump backward one sentence.

	} 
Jump forward one paragraph.

	{ 
Jump backward one paragraph.:

	j
Jump forward one line.

	k 
Jump backward one line.

	H 
Jump to the top of the screen.

	M 
Jump to the middle of the screen.

	L 
Jump to the bottom of the screen.

	10<PageUp> or 10<CTRL-B>
Move 10 pages up.

	5<PageDown> or 5<CTRL-F>
Move 5 pages down.

	G 
Jump to end of file.

	1G 
Jump to beginning of file (same as gg).

	50G 
Jump to line 50.

	mx 
Set mark x at the current cursor position.

	'x 
Jump to the beginning of the line of mark x.

	`x 
Jump to the cursor position of mark x.

	''
Return to the line where the cursor was before the latest jump.

	(Two single quotes.)
	``
Return to the cursor position before the latest jump (undo the jump).
(Two back ticks. This is above the Tab key on some keyboards.)

	'. 
Jump to the last-changed line.

	 % 
Jump to corresponding item, e.g. from an open brace to its matching closing brace. See Moving to matching braces for more.


Move around
-------------
H = move to top
M = move to middle
L = move to end

$ = move to bottom
0 = 
A = move to end of line and insert
b = backward on word
w = forward by word

arrow keys, pg up, pg dn, end, begin, home

Delete
-------------

x = del
X = del <<-
dw = delete word
dd = del line
dd10 = del next 10 lines
