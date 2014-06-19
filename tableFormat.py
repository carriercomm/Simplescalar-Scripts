#script to extract desired data from simulation output/log file

import sys

BZIP2 =	'./bzip2/'
EQUAKE ='./equake/'
MILC =	'./milc/'
HMMER =	'./hmmer/'
SJENG  = './sjeng/'
MCF = './mcf/'

args = sys.argv
def parse(args):

	outputName = args[len(sys.argv)-1]

	output = open(outputName + '_' + 'tableFormat.log', 'w')

	output.write(" sim_insn_num sim_CPI\n" );    	

	for x in range (0,6):
	
    		
		if x==0:
			path = BZIP2
			benchmark = 'bzip2'
			endOfFile = 'bzip2_results.log'
    		elif x==1:
			path = EQUAKE 
			benchmark = 'equake'
			endOfFile = 'equake_results.log'
    		elif x==2: 
			path = MILC 
			benchmark = 'milc'
			endOfFile = 'milc_results.log'
    		elif x==3: 
			path = HMMER 
			benchmark = 'hmmer'
			endOfFile = 'hmmer_results.log'
    		elif x==4:
			path = SJENG 
			benchmark = 'sjeng'
			endOfFile = 'sjeng_results.log'
    		elif x==5:
			path = MCF 
			benchmark = 'mcf'
			endOfFile = 'mcf_results.log'


			
		output.write(benchmark + "\n\n")
		
		for x in range ( 1, len(sys.argv)-1 ):
			fullPath = path + sys.argv[x] + '_' + endOfFile
			output.write( sys.argv[x] + ' ' )
			

			log = open(fullPath, 'r')

				    		

    			for line in log:
				if line.find('sim_num_insn') == 0:  #if the first word on this line is sim_num_insn
		            		output.write("%d " % (int(line.split()[1])))  #get the int value for sim_num_insn
				elif line.find('sim_CPI') == 0:     #if the first word on this line is sim_CPI
		            		output.write("%f " % (float(line.split()[1])))  #get the int value for sim_CPI
			
			output.write("\n")
    			log.close()
		
		output.write("\n")
    	output.close()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "Not enough arguments\n"
        print "Usage: python extract.py <log file> <benchmark>\n"
    else:
        parse(args)             
