import os, sys
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
import tensorflow as tf, keras, tensorflow
from keras.preprocessing.sequence import pad_sequences 
from keras.models import load_model
import numpy as np

def mono_hot_encode1(seq):
	mapping = dict(zip(['.',')','('], range(3)))  
	text=[seq[i:i+1] for i in range(len(seq)-(1-1))]
	seq1 = [mapping[i] for i in text]
	return np.eye(3)[seq1]


def mono_hot_encode(seq):
	mapping = dict(zip(['A','T','G','C'], range(4)))  
	text=[seq[i:i+1] for i in range(len(seq)-(1-1))]
	seq1 = [mapping[i] for i in text]
	return np.eye(4)[seq1]


def kmers(file1,k):
	seq_id1 = []
	kmer1 = []
	for line in file1:
		if line.startswith(">"):
			seq_id = line.strip()
		else:
			if(len(line) >= 400):
				for i in range(0,len(line)-k+1):
					kmer = line[i:i+k]
					seq = seq_id + "_" + str(i)
					seq_id1.append(seq)
					kmer1.append(kmer)
			elif(len(line) >= 200):
				seq_id1.append(str(seq_id)+'_0')
				kmer1.append(line)
	return(seq_id1,kmer1)



def foo(x):
	texts_mono_fold = []
	texts_mono_fold.append(mono_hot_encode1(x[2]))
	padded_docs3 = pad_sequences(texts_mono_fold, maxlen=400, padding='post') 
	X_test_mono_fold = np.array(padded_docs3).reshape(1,400, 3, 1)
	texts_mono = []
	texts_mono.append(mono_hot_encode(x[1]))
	padded_docs4 = pad_sequences(texts_mono, maxlen=400, padding='post')
	X_test_mono = np.array(padded_docs4).reshape(1,400, 4, 1)
	yhat = model.predict([X_test_mono, X_test_mono_fold])
	print(str(x[0])+'\t'+str(yhat))



filename=str(sys.argv[1])
kmer_coding = []
coding=[x1.strip() for x1 in open(filename).readlines()]
kmer_coding=kmers(coding,400)
label_seq_coding = [m+ '\t' + str(n) for m,n in zip(kmer_coding[0],kmer_coding[1])]
f1= open(filename+"_coding.fa","w+")
for i in label_seq_coding:
	z=i.split()
	f1.write(str(z[0])+'\n'+str(z[1])+'\n')


f1.close()
path = str(sys.argv[2])
os.system(path+"RNAfold -j --noPS  "+filename+"_coding.fa | paste - - - | awk \'{print $3}\' > "+filename+"_RNA_coding")
filename_2 = str("temp")
os.system("cat "+filename+"_coding.fa | paste - - "+filename+"_RNA_coding >"+filename_2)
f1=[x.split() for x in open(filename_2).readlines()]
model = load_model('DeepPlnc_model.h5')
name = [foo(i) for i in f1]
