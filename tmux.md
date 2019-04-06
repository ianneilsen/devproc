## tmux and screen


### cheat sheet

https://gist.github.com/MohamedAlaa/2961058
http://neophob.com/2007/04/gnu-screen-cheat-sheet/


#### create detached session foo	

	$ screen -S foo -d -m	
	$ tmux new -s foo -d

### list sessions	

	$ screen -list	
	$ tmux ls

#### Attach to a session	

	$ screen -r	
	$ tmux attach

#### Attach to session named foo	

	$ screen -r foo	
	$ tmux attach -t foo

#### re-attach a detached session	

	$ tmux attach
	$ tmux attach-session	
	$ screen-r

#### re-attach an attached session (detaching it from elsewhere)	

	$ tmux attach -d
	$ tmux attach-session -d	
	$ screen -dr

#### re-attach an attached session (keeping it attached elsewhere)	

	$ tmux attach
	$ tmux attach-session	
	$ screen -x

#### detach from currently attached session	

	^b d
	^b :detach	
	^a ^d
	^a :detach

#### rename-window to newname	

	^b , <newname>
	^b :rename-window <newn>	
	^a A <newname>

#### list windows	

	^b w	
	^a w

#### list windows in chooseable menu		

	^a "

#### go to window #	

	^b #	
	^a #

#### go to last-active window	

	^b l	
	^a ^a
	go to next window	
	^b n	
	^a n

#### go to previous window	

	^b p	
	^a p

#### see keybindings	

	^b ?	
	^a ?

#### list sessions	

	^b s
	tmux ls
	tmux list-sessions	
	screen -ls

#### toggle visual bell		

	no tmux
	screen $^a ^g

#### create another window	

	$ ^b c	
	^a c

#### exit current shell/window	

	^d	
	^d

#### split window/pane horizontally	

	^b "	
	^t
	 S

#### split window/pane vertically	

	^b %	
	^a |
	switch to other pane	
	^b o	
	^a <tab>

#### kill the current pane	

	^b x 
	(logout/^D)	

#### collapse the current pane/split (but leave processes running)		

	^a X

### cycle location of panes	

	^b ^o	

#### swap current pane with previous	

	^b {	

#### swap current pane with next	

	^b }	

#### show time	

	^b t	

#### show numeric values of panes	

	^b q	

#### toggle zoom-state of current pane (maximize/return current pane)	

	^b z	

#### break the current pane out of its window (to form new window)	

	^b !	

#### re-arrange current panels within same window (different layouts)	

	^b [space]	

#### Kill the current window (and all panes within)	

	^b killw [target-window]	 
