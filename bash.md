# Stream
## for
```bash
for i in ((i=0; i<=100; i++)) # C-like
for i in {1..100}
for i in `seq 1 100`
```
# General
## find
`find [-path] -option`
```bash
# options
-name 
-mtime # modified time, e.g.
    $ find . -mtime 7 # mdfd 7 days ago
    $ find . -mtime +7 # mdfd more than 7 days ago
    $ find . -mtime -7 # mdfd no more than 7 days ago
-size
-exec # e.g.
    $ find . -name "*chk" -exec rm {} \; # rm files found
-ok # like -exec, but confirm required
-print
```
## grep
```bash
grep "^-" # file
grep "^d" # dir
```
## ls
```bash
ls -l
ls -lR # recursively
```
count # of files (w/out dir) `ls -l | grep "^-" | wc -l`. See **grep**, **wc**.
## wc
```bash
wc -l # count lines
```
#Shortcuts
```
Ctrl+L # clear
Ctrl+A # jump to head of current line
Ctrl+E # ... end ...
Ctrl+W # clear current line
Ctrl+Y # paste
Ctrl+C # kill current program
Ctrl+D # exit
Ctrl+R # search history command
```
