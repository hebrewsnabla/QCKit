# Math
## expr
```bash
val=`expr ...`
echo $val
```
expressions:
```bash
val=`expr $a + $b`
val=`expr $a - $b`
val=`expr \( $a + $c \) \* $b`
val=`expr $b / $a`
val=`expr $b % $a`
```

# Stream
## for
```bash
for i in ((i=0; i<=100; i++)) # C-like
for i in {1..100}
for i in `seq 1 100`
```
# General
## df
check disk use
```bash
df -h
df -h /user/
```
## du
```bash
du -h # recursively!
du --max-depth=1 -h [-path]
du -sh [-path] # itself
```
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
## tar
```bash
tar -xvf foo.tar     # extract, verbosely
tar -cvf foo.tar foo # create, ...
tar -zxvf foo.tar.gz
tar -jxvf foo.tar.bz2
#options
-d # difference
-r, --append
-u, --update
-t, --list
```
# I/O
## input
```bash
# this is a bash file
echo "the bash file is $0"
echo "the first input is $1"
echo "the first input is $2"
# ...
echo "the number of input params is $#"
echo "all input params are $*" # i.e. "$1 $2 ..."
echo "all input params are $@" # i.e. "$1" "$2" ...
```
# Shortcuts
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
