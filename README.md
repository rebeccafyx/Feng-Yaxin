# Feng-Yaxin

Question (1):
1.input "top"
2.input "getconf -a | grep CACHE" to get the L1-L3 cache size
3.input "lshw -C memory" to get the memory size
4.input "df -h" to get the disk size

Question (2):
step1: input"touch createfolders.sh" to create a shell script, input "vim createfolders.sh" to edit the bash

step2: the code of my bash is like this:
#!/bin/sh
For I in `seq 1 100`;do
	mkdir DDM$i
	cd ./DDM$i
	dcho “nanoseconds since 1970-01-01 00:00:00 UTC:
<$(date +%s%N)>”>time_till_now.txt
	cd ../
done

step3: input"ESC+:wq!" to exit

step4: input "ls" of "tree" to check the folders and documents

step5: input "cd DDM1" to change the location, and input "cat tim_till_now.txt" to cheak the content in the .txt document.

Question (3):
import the .xml files to python, and use regular expression to deal with the strings.
