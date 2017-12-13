#! /bin/bash 

#---------------------------------------
# $Author: ee364d27 $
# $Date: 2017-09-03 21:48:09 -0400 (Sun, 03 Sep 2017) $
#---------------------------------------

# Do not modify above this line.


for File in c-files/*.c
do
	string1=${File#"c-files/"}
	string2=${string1%?}
	echo -n "Compiling file $string1..."
	gcc -Wall -Werror ${File} 2>/dev/null 
	
	if (( $? == 0 )) 
	then
		echo " Compilation succeeded."
		echo "$(./a.out)" > ${string2}out
	else
		echo " Error: Compilation failed."
	fi
	
done
echo
exit 0
