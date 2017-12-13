#! /bin/bash

#---------------------------------------
# $Author: ee364d27 $
# $Date: 2017-08-30 10:48:02 -0400 (Wed, 30 Aug 2017) $
#---------------------------------------

# Do not modify above this line.
if (( $# != 1 ))
then
	echo "Usage: kaprekar.bash <non-negative integer>"
	echo
	exit 1
fi

testnum=$1

if (( $testnum >= 1 ))
then
	echo 1, square=1, 1+0=1
fi

for (( I=8; I<= $testnum; I++ ))
do
	length=${#I}
	((square=I*I))
	length2=${#square}
	((length3=length2-length))
	left=$(echo $square | cut -c 1-$length3)
	if (( $length2 < 5 ))
	then
	((test42=$length+1))
	
	else
	((test42=$length))
	fi
	right=$(echo $square | cut -c $test42-$length2)
	#echo $I
	#echo $square
	#echo $left
	#echo $right
	#echo
	rightfinal=$((10#$right))
	leftfinal=$((10#$left))
	((final=$rightfinal+$leftfinal))
	if (( final == $I ))
	then
		
		echo "${I}, square=${square}, ${rightfinal}+${leftfinal}=${final}"
	fi
done

exit 0

