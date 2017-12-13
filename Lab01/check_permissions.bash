#! /bin/bash

#---------------------------------------
# $Author: ee364d27 $
# $Date: 2017-08-30 09:59:33 -0400 (Wed, 30 Aug 2017) $
#---------------------------------------

# Do not modify above this line.


output=($(ls -ld $1))
output2=${output[0]}

if [[ $(echo $output2 | cut -c 1) = '-' ]]
then
	echo "$1 is an ordinary file"
else
	echo "$1 is a directory"
fi

echo
echo "Owner Permissions:"
echo

if [[ $(echo $output2 | cut -c 2) = 'r' ]]
then
	echo "$1 is readable"
else
	echo "$1 is not readable"
fi

if [[ $(echo $output2 | cut -c 3) = 'w' ]]
then
	echo "$1 is writable"
else
	echo "$1 is not writable"
fi

if [[ $(echo $output2 | cut -c 4) = 'x' ]]
then
	echo "$1 is executable"
else
	echo "$1 is not executable"
fi

echo
echo "Group Permissions:"
echo

if [[ $(echo $output2 | cut -c 5) = 'r' ]]
then
	echo "$1 is readable"
else
	echo "$1 is not readable"
fi

if [[ $(echo $output2 | cut -c 6) = 'w' ]]
then
	echo "$1 is writable"
else
	echo "$1 is not writable"
fi

if [[ $(echo $output2 | cut -c 7) = 'x' ]]
then
	echo "$1 is executable"
else
	echo "$1 is not executable"
fi

echo
echo "Others Permissions:"
echo

if [[ $(echo $output2 | cut -c 8) = 'r' ]]
then
	echo "$1 is readable"
else
	echo "$1 is not readable"
fi

if [[ $(echo $output2 | cut -c 9) = 'w' ]]
then
	echo "$1 is writable"
else
	echo "$1 is not writable"
fi

if [[ $(echo $output2 | cut -c 10) = 'x' ]]
then
	echo "$1 is executable"
else
	echo "$1 is not executable"
fi

echo

exit 0
