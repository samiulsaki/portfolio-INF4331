#!/bin/bash

## Calculator with operation and arguments ##

clear
function calculator {
	
	printf "\nWrong format!! You must provide all the arguments \n"
	printf "Use format: $(tput setaf 1)./calc.sh $(tput setaf 3)S(Summation) | P(Product) | M(Maximum) | m(Minimum) $(tput setaf 5)num num num ... ... \n\n"
	exit
}

[ $# -lt 2 ] && calculator

# Take Variables:
operation=$1;
shift 
sum=$1;
pro=$1;
max=$1;
min=$1; 
shift

# Main Calculation:
for args in $@; do
	sum=$((${sum} + ${args}))
	pro=$((${pro} * ${args}))
	[ ${args} -gt ${max} ] && max=${args}
	[ ${args} -lt ${min} ] && min=${args}
done;

# Cases
case "${operation}" in
	
        S ) 
		echo "Summation = ${sum}";;
        
	P ) 
		echo "Product = ${pro}";;
        
	M ) 
		echo "Maximum = ${max}";;
        
	m ) 
		echo "Minimum = ${min}";;
        
	* ) 
		calculator;;
esac
