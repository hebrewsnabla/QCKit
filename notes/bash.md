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
## rename
```bash
rename [-v] [-n] [-f] perlexpr [filenames]
-v # verbosely
-n # simulate
-f # force
# expr:
"s/.xyz/.gjf/"
# filenames can be *.xyz
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
## wc
```bash
wc -l # count lines
```

# I/O
## merge files
```bash
cat 1.log 2.log > merge.log
cat *.log > merge.log
paste file1 file2 > file3 # merge as columns
cat file1 file2 | sort | uniq > file3 # 并集
cat file1 file2 | sort | uniq -d > file3 # 交集
cat file1 file2 | sort | uniq -u > file3 # 差集
```
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
## sed
```bash
# delete
sed -i "Nd" filename # Nth line
sed -i "N,Md" filename # N~Mth line
sed -i "/abc/d" filename
sed -i "/abc/d;/efg/d" filename
```
# Misc
## date, cal
```bash
$ date
Fri Aug 30 01:46:13 CST 2019
$ date -R
Fri, 30 Aug 2019 01:46:59 +0800
$ cal
     August 2019
Su Mo Tu We Th Fr Sa
             1  2  3
 4  5  6  7  8  9 10
11 12 13 14 15 16 17
18 19 20 21 22 23 24
25 26 27 28 29 30 31
$ tzselect # modify time zone
# to modify time or date
$ date -s MM/DD/YYYY
$ date -s hh/mm/ss
# to save the modification
$ hwclock -w
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
