# avec winsound je peux faire de la musique dans python !
# https://docs.python.org/2.7/library/winsound.html?highlight=winsound#module-winsound
# http://stackoverflow.com/questions/12354586/python-what-are-the-nearest-linux-and-osx-equivalents-of-winsound-beep

# avec sonic-pi c'est plus simple !

from Bio import SeqIO

def main (seq,sleepValue):
    print seq#
    res=str()
    for aa in seq:
        #print aa#
        #parcours des acides amines et restitution en code USA des notes
        if aa=='A': #arginine devient un LA
            res=res.__add__('play :'+aa+'\n')
        elif aa=='C': #cysteine devient un DO
            res=res.__add__('play :'+aa+'\n')
        elif aa=='D': #acide aspartique devient un RE
            res=res.__add__('play :'+aa+'\n')
        elif aa=='E': #acide glutamique devient un MI
            res=res.__add__('play :'+aa+'\n')
        elif aa=='F': #phenylalanine devient un FA
            res=res.__add__('play :'+aa+'\n')
        elif aa=='G': #glutamine devient un SOL
            res=res.__add__('play :'+aa+'\n')
        else:	      #tous les autres deviennent des pauses
            if res[-2:][:1]==str(sleepValue)[-1:]:#pour ne pas multiplier les sleep
                None
            else:
                res=res.__add__('sleep '+str(sleepValue)+'\n')  #mais IDEE : en faire des valeurs de prolongation des notes
    print res#
    return res 			                   
	
def output(fasta,filename,sleepValue):
    	f=SeqIO.read(fasta,'fasta')
    	seq = f.seq
	g=open(filename,'w')
	res=main(seq,sleepValue)
	g.write(str(res))
	g.close()
	
