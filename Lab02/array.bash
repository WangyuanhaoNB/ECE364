#! /bin/bash

# $Author: ee364d27 $
# $Date: 2017-09-06 11:01:27 -0400 (Wed, 06 Sep 2017) $

function array 
{
    	# Fill out your answer here.
    	Arr=(a.txt b.txt c.txt d.txt e.txt)
	((sel=$RANDOM%5))
	count=1
	while read -r line 
	do
	if ((count == 7 || count == 8 || count == 9))
	then

		echo $line
	fi
	((count=count+1))
	done < ${Arr[sel]}
	

    	return

}


#
# To test your function, you can call it below like this:
#
#array
#

array
