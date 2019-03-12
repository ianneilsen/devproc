## mv - aka move command

#### Good Links


	$mv old-file-name  new-file-name

	mv -f

#### Interacive renaming - If you implement or change the mv cmd to always go interactive, this sometimes can help stop malicious scripts.

	mv -i

	mv -bf

#### Rename multiple files/dir

	mv *.txt *.dat

#### quick move = less typing

This does a rename of the directory as opposed to saying - move this file/dir to this file/dir.
Nice shortcut

	mv file_name{,extraName}

Examples

	mv /home/downloads{,only}  =  /home/downloadsonly
 	mv /home/downloads{,_only} = /home/downloads_only
