text and finding text strings, grepping, sed and awk
------------------------------------------------------

https://unix.stackexchange.com/questions/138398/how-to-get-lines-10-to-100-from-a-200-line-file-into-a-new-file

#### To find files by case-insensitive extension (ex: .jpg, .JPG, .jpG):

```bash
find . -iname "*.jpg"
```

#### To find directories:

```bash
find . -type d
```

#### To find files:

```bash
find . -type f
```

#### To find files by octal permission:

```bash
find . -type f -perm 777
```

#### To find files with setuid bit set:

```bash
find . -xdev \( -perm -4000 \) -type f -print0 | xargs -0 ls -l
```

#### To find files with extension '.txt' and remove them:

```bash
find ./path/ -name '*.txt' -exec rm '{}' \;
```

#### To find files with extension '.txt' and look for a string into them:

```bash
find ./path/ -name '*.txt' | xargs grep 'string'
```

#### To find files with size bigger than 5 Mebibyte and sort them by size:

```bash
find . -size +5M -type f -print0 | xargs -0 ls -Ssh | sort -z
```

#### To find files bigger than 2 Megabyte and list them:

```bash
find . -type f -size +200000000c -exec ls -lh {} \; | awk '{ print $9 ": " $5 }'
```

#### To find files modified more than 7 days ago and list file information

```bash
find . -type f -mtime +7d -ls
```

#### To find symlinks owned by a user and list file information

```bash
find . -type l --user=username -ls
```

#### To search for and delete empty directories

```bash
find . -type d -empty -exec rmdir {} \;
```

#### To search for directories named build at a max depth of 2 directories

```bash
find . -maxdepth 2 -name build -type d
```

#### To search all files who are not in .git directory

```bash
find . ! -iwholename '*.git*' -type f
```

#### To find all files that have the same node (hard link) as MY_FILE_HERE

```bash
find . -type f -samefile MY_FILE_HERE 2>/dev/null
```

#### To find all files in the current directory and modify their permissions

```bash
find . -type f -exec chmod 644 {} \;
```


