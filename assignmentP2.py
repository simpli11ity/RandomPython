import colorsys
import sys
import itertools

def translate(seq): 
      
    table = { 
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M', 
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T', 
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K', 
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',                  
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L', 
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P', 
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q', 
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R', 
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V', 
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A', 
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E', 
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',  
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S', 
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L', 
        'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_', 
        'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W', 
    }
    print("DNA sequence: ", seq)
    for i in range(len(seq)):
        seq[i]=table[seq[i]]
    print("AMINO ACID LENGTH: ", len(seq)-1)
    print(seq)
"""
got this code form here https://codereview.stackexchange.com/questions/151329/reverse-complement-of-a-dna-string
"""
def reverse_complement(dna):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    return ''.join([complement[base] for base in dna[::-1]])
"""
^end of code i got ^
"""


def Frame(values):
    values.pop(0)
    string = ''.join(values)
    reverse=reverse_complement(string)
    frame1=[]
    frame2=[]
    frame3=[]
    frame4=[]
    frame5=[]
    frame6=[]
    
   
    
    frame1=framez(string,frame1,0)
    frame2=framez(string,frame2,1)
    frame3=framez(string,frame3,2)
    frame4=framez(reverse,frame4,0)
    frame5=framez(reverse,frame5,1)
    frame6=framez(reverse,frame6,2)
    #ORFS(frame1,1,0)
    #ORFS(frame2,2,0)
    #ORFS(frame3,3,0)
    ORFS(frame4,-1,len(string))
    #ORFS(frame5,-2,len(string))
    #ORFS(frame6,-3,len(string))
    
    
    
    
def ORFS(fra,no,lena):
    cur=0
    startposition=0
    dnastring=""
    endpos=0
    codon=[]
    count=0
    falsesecond=False
    for i in range(len(fra)):
        
        if fra[i] == "ATG":
            count=count+1
            cur=True
            
        if count < 1:
            startposition=i+1

        if (fra[i] =="TAG" or fra[i] =="TGA" or  fra[i] =="TAA" or i == len(fra)-1)and cur==True :
            endpos=i+1
            cur=False
            count=0
            # records all potential codons
            codon.append([startposition,endpos])
    
    if len(codon) > 0:
        for i in range(len(codon)):
            if((codon[i][1]*3)-(codon[i][0]*3) > 30):
                print("\n")
                print("FRAME NUMBER: ", no)
                if no >0:
                    print("Nucleotide start and stop position: ",(int(codon[i][0])*3)+no,(int(codon[i][1])*3)+no-1)
                else:
                    print("Nucleotide start and stop position: ",lena-((int(codon[i][0])*3)-no-1),lena-((int(codon[i][1])*3)-no-2))

                print("lenght: ",((int(codon[i][1])-int(codon[i][0]))*3)) 
                print("Amino Acid Stop Start: ", codon[i][0],codon[i][1])        
                dna=fra[int(codon[i][0]):int(codon[i][1])]
                dnastring=dnastring.join(dna)
                translate(dna)


def framez(string,frame1,iter):
    for i in itertools.count(iter,3):
        if i+2>=len(string):
            break
        else:
            frame1.append(string[i:i+3])
    return frame1


def main():
    values = []   # create an empty list (array) of values

   
    # input the name of the file
    #FileName = input("Enter the name of the file: ")

        #open the file in reading text mode using error checking
    try:
        #inp = input("Enter the name of a file in the same directory as this program")
        Fp1 = open("palgene.fasta",'r')
        for line in Fp1:
            # strip line of /n
            line = line.rstrip('\n')
            values += [line]   # add the line to the list: this prints the \n as well 
        Frame(values)
        

    except IOError:
        print("error unable to read file or file does not exist!!!")
        print("Exiting the program")
        stop = input()
        Fp1.close()
        exit(1)
        








     

#****************** execute the program *********************
main()



#**************************TEST PAN **********************
"""
    Reads in a file from user input
    removes first line
    joins the lines in to one string from rest of file
    breaks string into groups of 3
    generates +3 and -3 frames based on string turned into a list  with 3 elements in each item
    search for stop start codons
    display nucleotide, amino acid sequence, length, stop and start of the nucleotide
    Basically a replication of the NCBI APP, just more basic
"""
   
