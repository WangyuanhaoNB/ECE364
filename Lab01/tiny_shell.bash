#! /bin/bash 

#---------------------------------------
# $Author: ee364d27 $
# $Date: 2017-08-27 18:00:23 -0400 (Sun, 27 Aug 2017) $
#---------------------------------------

# Do not modify above this line.
while (( 0 == 0 ))
do

#echo -n 
read -p "Enter a command: " acommand

if [[ $acommand = "hello" ]]
then
	echo "Hello $USER"

elif [[ $acommand = "compile" ]]
then
	for File in *.c
	do
	gcc -Wall -Werror ${File} -o ${File%?}o
	
	if (( $? == 0 )) 
	then
		echo "Compilation succeeded for: ${File}"
	else
		echo "Compilation failed for: ${File}"
	fi

	done

elif [[ $acommand = "whereami" ]]
then
	echo ${PWD};

elif [[ $acommand = "quit" ]]
then
	echo "Goodbye"
	exit 0
else
	echo "Error: unrecognized input"
fi


echo

done

exit 0
