#!/bin/bash
## The Bookmark script
# ============================================================================================#
# The script takes arguments from user to do the corresponding tasks:
# 1) source bookmark.sh: exports all the bookmarks (if there is any) and print out with the available bookmarks
# (if there is any). Recommend to always run this command first. If not you might loose the previous bookmarks.
#
# 2) source bookmark.sh -a directory_name: creates a bookmark along with the current path of the directory.
# Then it exports it to the variable which is same as the given directory_name. Running cd $directory_name
# will direct to corresponding directory.
#
# 3) source bookmark.sh -r directory_name: will remove the bookmark of the given directory from the bookmark
# list. It will also remove the variable name created for that bookmark.
#
# 4) source bookmark.sh -h: will open the script usage help menu.
# Inserting any wrong flag rather than -a | -A | -r | -R | -h will print out the help menu automatically.
#
# Disclaimer:
# The script is not completely bug free. It does not run on Unix system as declare -A is defined in Unix.
# Upon sourcing the script for first time might throw out bookmark exporting error. If do please ignore the
# message and run it again.
#==============================================================================================#

clear
declare -A bookmark

# Take Arguments
operation=$1;
dir=$2;
path=$(pwd);

# Usage/Help 
function bookmark_usage {
        echo -en "\nYou must provide all the arguments \n"
        echo -en "Use format: $(tput setaf 1)source bookmark.sh $(tput setaf 5)-a(adding bookmark) | -r(removing bookmark) $(tput setaf 3)directory_name\n"
	echo -en "$(tput sgr0)For sourcing all the bookmarks: $(tput setaf 1) source bookmark.sh $(tput sgr0)\n"
	echo -en "For help and check all the bookmarks: $(tput setaf 1)source bookmark.sh -h$(tput sgr0)\n\n"
        return
}

# Bookmark Export
function bookmark_export {
	touch ~/.bookmark
	echo -en "\nShowing all the bookmarks (if any):\n";
	while IFS="|" read dir path
        	do
                	export $dir=$path
			echo "Directory= $(tput setaf 3)$dir$(tput sgr0)  :  Path= $(tput setaf 3)$path$(tput sgr0)";
			bookmark[$dir]=$path
	        done < ~/.bookmark
}

# Error
function bookmark_error {
		echo "Opps!! You forgot to insert a directory name" && bookmark_usage
}

# Cases
function bookmark_import {
	case "${operation}" in
		[-][aA] )
			if [ ! -z "$dir" ]; then
				bookmark[$dir]=$path; rm ~/.bookmark; for i in "${!bookmark[@]}"; do echo "$i|${bookmark[$i]}" >> ~/.bookmark; done; bookmark_export;
			else
				bookmark_error
			fi;;

		[-][rR] )
			if [ ! -z "$dir" ]; then
				unset bookmark[$dir]; rm ~/.bookmark; for i in "${!bookmark[@]}"; do echo "$i|${bookmark[$i]}" >> ~/.bookmark; done; eval "unset "$dir""; bookmark_export;
			else
				bookmark_error
			fi;;

		[-][h] )
			bookmark_usage;;

	        * )
			bookmark_usage;;
	esac
}

# Select Functions
if [ $# == "0" ]; then
	bookmark_export
elif [ $# == 1 ]; then
	bookmark_import
elif [ $# == 2 ]; then
	bookmark_import
fi
