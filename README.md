Simplescalar-Scripts
====================

This repository contains a couple scripts that I used in my CMPEN 431 ( Computer Architechture ) class. Simplescalar is a 
program that lets you run any program in a simulated CPU. This simulated CPU has dozens of settings and that can be changed
using a .cfg file. These settings include cache sizes, issue and decode width, branch prediction, memory latency, and 
many more.

The Simplescalar.script takes in a variable number of arguments. Each for each argument simplescalar is run a single time using a .cfg file according to the arguemnt. The script uses a runall.script bash routine which actually calls the execution of simplescalar. Then a myExtract.py python script is run to gather the useful information from the output of the simple scalar program. Finally after some file manipulation, another python script, tableFormat.py, is called which pulls the information from each run into one file.
