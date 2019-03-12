## Good scripts

 Have script run itself in a virtual terminal

     $ tty >/dev/null || { urxvt -e /bin/sh -c "tty >/tmp/proc$$; while test x; do sleep 1; done" & while test ! -f /tmp/proc$$; do sleep .1; done; FN=$(cat /tmp/proc$$); rm /tmp/proc$$; exec >$FN 2>$FN <$FN; }

— by openiduser111 on March 9, 2018, 2:56 a.m.
Explanation

    We begin by testing if the script is not in a terminal with tty.
    If it is not we start a terminal that runs tty and saves it to a filename. $$ was set by the original script and is its PID. That is opened in the background using & and then the original script waits for the filename to appear, then reads and removes it.
    Finally, the main command is a special syntax of the bash builtin command exec that contains nothing but redirections (of stdout, stderr, and stdin) so they will apply to every command in the rest of the script file.


	
#### Have script run itself in a virtual terminal

    $ tty >/dev/null || { urxvt -hold -e "$0" "$@" & exit; }

— by openiduser111 on March 6, 2014, 3:18 a.m.
Explanation

This can be the first line of a script that will be clicked from a graphical user interface in X to make it open up a virtual terminal to display output. If a terminal is already open it will run in the current terminal. It assumes urxvt and uses the hold option to keep from closing, both of which could be substituted for such as rxvt or add read at the end of the script.

    It's a single line if statement that checks the exit code of tty which prints the current terminal name usually nothing under X.
    The curly braces are needed for grouping.
    A space is required after the opening brace { and a semicolon is required before the closing brace }.
    Replacing what would be a semicolon, the ampersand & forks the terminal command to a second process and the launching script exits right away.
    -e feeds to the terminal application the expression of $0which holds the path of the script itself and $@, the entire set of quoted arguments.

Limitations

If the script is large, say several gigabytes and the system tries to make two copies of the script, twice the size of RAM or memory will be needed for loading it.

    rxvt -e will kill any subprocesses at the end
	
#### Big CSV > batches > JSON array > CURL POST data with sleep

    $ cat post-list.csv | split -l 30 - --filter='jq -R . | jq --slurp -c .' | xargs -d "\n" -I % sh -c 'curl -H "Content-Type: application/json" -X POST -d '"'"'{"type":1,"entries":%}'"'"' http://127.0.0.1:8080/purge-something && sleep 30'

— by pratham2003 on March 7, 2018, 12:12 p.m.
Explanation

post-list.csv contains list of URLs in my example.

    split -l 30 Split by 30 lines

    - Use stdin as input for split

    --filter Couldn't find a way to easily pipe to stdout from split, hence --filter

    jq -R . From the jq manual - Don’t parse the input as JSON. Instead, each line of text is passed to the filter as a string

    jq --slurp -c . From the jq manual - Instead of running the filter for each JSON object in the input, read the entire input stream into a large array and run the filter just once. -c makes it easier to pipe and use it in the xargs that follows.

    xargs -d "\n" -I % sh -c Execute a command for each array. Use "\n" as delimiter. Use % as a placeholder in the command that follows.

    Single quotes inside sh -c ' ... ' are escaped as '"'"' single-double-single-double-single. You can do whatever you need to inside sh -c ' ... && sleep 123'

Limitations

You need jq installed, for example in Debian / Ubuntu:

    apt-get install jq`

See also https://stedolan.github.io/jq/manual/

I suspect the input file (cat post-list.csv) may not contain double or single quotes but haven't tested it.

