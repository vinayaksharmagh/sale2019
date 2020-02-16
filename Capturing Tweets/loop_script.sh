#program live_capture.py was run inside loop with the help of shell script. This was done so that any unexpected termination of program due to 
#api and server issues can be dealt with.
i=1
while true
do
	echo $i process relaunched
	python3 live_capture.py $i
	i=$(($i+1))
done
