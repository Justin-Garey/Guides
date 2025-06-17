#!/bin/bash

# Name: cmd_line_args.sh
# Description: This is an example script for how to 
#   use command line arguments in a shell script. 
#   This script is based on this answer 
#   (https://unix.stackexchange.com/a/505342)
#   to a question on Unix Stack Exchange.
# Example: ./cmd_line_args.sh -a arg1 -b arg2 -c arg3

helpFunction()
{
   echo ""
   echo "Usage: $0 -a <parameterA> -b <parameterB> [OPTIONS]"
   echo -e "\t-a Description of what is parameterA"
   echo -e "\t-b Description of what is parameterB"
   echo -e "\t-c Description of what is parameterC"
   echo -e "\t-h View this help message"
   echo ""
   exit 1
}

while getopts "a:b:c:" opt
do
   case "$opt" in
      a ) parameterA="$OPTARG" ;;
      b ) parameterB="$OPTARG" ;;
      c ) parameterC="$OPTARG" ;;
      h ) helpFunction ;;
      ? ) helpFunction ;;
   esac
done

# parameterA and parameterB are required
if [ -z "$parameterA" ] || [ -z "$parameterB" ]
then
   echo "parameterA and/or parameterB are missing";
   helpFunction
fi

echo "$parameterA"
echo "$parameterB"
echo "$parameterC"