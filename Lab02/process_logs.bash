#! /bin/bash 

#---------------------------------------
# $Author: ee364d27 $
# $Date: 2017-09-03 21:30:27 -0400 (Sun, 03 Sep 2017) $
#---------------------------------------

# Do not modify above this line.

if (( $# != 1 ))
then
	echo "Usage: process_logs.bash <input file>"
	echo
	exit 1
fi

filename=$1

if [[ ! -r $filename ]]
then
	echo "Error: ${filename} is not a readable file."
	echo
	exit 2
fi


if [[ -e $filename.out ]]
then
	$(rm -f $filename.out)
fi



read -r firstline<$filename

arr1=$(echo $firstline)




while read -r line 
do
	sum1=0	
	temparr=($(echo $line))	
	((num1=${#temparr[*]}-1))
	for element in ${temparr[@]:1}
	do
		((sum1=$sum1+$element))
	done
	avg=$(bc <<< "scale=2 ; $sum1/$num1")
	time=${temparr[0]}
	printf "Average temperature for time %d was %0.2f C.\n" $time $avg >> ${filename}.out

	sorted=( $( printf "%s\n" "${temparr[@]:1}" | sort -n ) )

	
	

	if (( (($num1%2)) == 0 ))
	then
		((num2=($num1/2)-1))
		((num3=$num2+1))
		(( final = ${sorted[$num2]} + ${sorted[$num3]} ))
		med=$(bc <<< "scale=2 ; $final / 2")
	else
		((num4=$num1+1))
		((num5=($num4/2)-1))
		med=${sorted[$num5]}

	fi 
	printf "Median temperature for time %d was %0.2f C.\n" $time $med >> ${filename}.out
	echo >> ${filename}.out
done < <(tail -n +2 $filename)

test42=2
#echo ${arr1[@]:4}
for element in ${arr1[@]:4}
do
	#echo $element
	arr2=( $(cut -f${test42} $filename) )
	#echo ${arr2[*]}
	sum1=0	
	((num1=${#arr2[*]}-1))
	for element1 in ${arr2[@]:1}
	do
		((sum1=$sum1+$element1))
	done
	avg=$(bc <<< "scale=2 ; $sum1/$num1")
	printf "Average temperature for %s was %0.2f C.\n" $element $avg >> ${filename}.out

	sorted=( $( printf "%s\n" "${arr2[@]:1}" | sort -n ) )

	
	

	if (( (($num1%2)) == 0 ))
	then
		((num2=($num1/2)-1))
		((num3=$num2+1))
		(( final = ${sorted[$num2]} + ${sorted[$num3]} ))
		med=$(bc <<< "scale=2 ; $final / 2")
	else
		((num4=$num1+1))
		((num5=($num4/2)-1))
		med=${sorted[$num5]}

	fi
	printf "Median temperature for %s was %0.2f C.\n" $element $med >> ${filename}.out
	echo >> ${filename}.out
	((test42=$test42+1))
	
done



echo
exit 0
