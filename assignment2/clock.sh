#!/bin/bash
# Clock with operations

clear
function clock {
	echo -e "\nWrong argument!! Enter: $(tput setaf 1)./clock.sh $(tput setaf 3)no(Norway) | us(eastern US) | sk(South Korea)\n"
	exit
}

# Take Argument
operation=$1

# Cases
case "${operation}" in

	[uU][sS] ) 
		tz="America/New_York";;
	[nN][oO] ) 
		tz="Europe/Oslo";;
	[sS][kK] ) 
		tz="Asia/Seoul";;
	* ) 
		clock;;
esac

# Print Timezone and Time
echo -e "\n$(tput setaf 1)TimeZone: ${tz}"
while true; do	
	echo -en "\r$(tput setaf 3)$(TZ="${tz}" date +"%A %B %d %Y %T %Z")"
done
