sh and dash are pre-installed in Kali
alt+printscreen to capture the active window
Screenshot is saved in Pictures

xdg-open to double click screenshot (anything) and to view
ls -lahtr
l long listing
a all dot files
h hidden files
t as per modification time
r reverse so recently modified appears at the top

date #Current date time and timezone

ls --hide=Desktop #Hides Desktop in the list

uname #current OS
uname -a #full details of current OS
who -uH # Who is using computer how long, u is about idle time H is header line

#73 done

history # cmd to look history of commands entered

type bash #IMPORTANT TO CHECK WHERE THE COMMAND IS TAKEN FROM, IN OTHER DISTROS IT MIGHT BE FROM USER/BIN/BASH OR BIN/BASH

locate chage #To locate or find the path of the chage command

export PS1="[\t \w]\$ " to see a prompt that looks like this: [20:26:32 /var/spool]$ #pg 90

WHATEVER—You can create your own environment variables to provide shortcuts in your work. Choose any name that is not being used and assign a useful value to it. For example, if you do lots of work with ﬁ les in the /work/time/files/info/ memos directory, you could set the following variable: M=/work/time/files/info/memos ; export M
You could make that your current directory by typing cd $M. You could run a program from that directory called hotdog by typing $M/hotdog. You could edit a ﬁ le from there called bun by typing vi $M/bun
