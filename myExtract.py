#script to extract desired data from simulation output/log file

import sys

BZIP2 =	'bzip2/'
EQUAKE ='equake/'
MILC =	'milc/'
HMMER =	'hmmer/'
SJENG  = 'sjeng/'
MCF = 'mcf/'

def parse(fileName, outputName):
	



	for x in range (0,6):
	
    		
		if x==0:
			path = BZIP2 + fileName
			benchmark = 'bzip2'
    		elif x==1:
			path = EQUAKE + fileName
			benchmark = 'equake'
    		elif x==2: 
			path = MILC + fileName
			benchmark = 'milc'
    		elif x==3: 
			path = HMMER + fileName
			benchmark = 'hmmer'
    		elif x==4:
			path = SJENG + fileName
			benchmark = 'sjeng'
    		elif x==5:
			path = MCF + fileName
			benchmark = 'mcf'

    		log = open(path, 'r')


		

    		output = open(outputName + '_' + benchmark + '_results.log', 'w')

    		for line in log:
		        if line.find('sim_num_insn') == 0:  #if the first word on this line is sim_num_insn
		            output.write("sim_num_insn: %d \n" % (int(line.split()[1])))  #get the int value for sim_num_insn
			elif line.find('sim_CPI') == 0:     #if the first word on this line is sim_CPI
		            output.write("sim_CPI: %f \n" % (float(line.split()[1])))  #get the int value for sim_CPI			


    		log.close()
    		output.close()

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print "Not enough arguments\n"
        print "Usage: python extract.py <log file> <benchmark>\n"
    else:
        parse(sys.argv[1], sys.argv[2])             
