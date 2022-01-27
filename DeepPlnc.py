import os, sys
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
import tensorflow as tf, numpy, keras, tensorflow, numpy as np
from keras.preprocessing.sequence import pad_sequences 
from keras.models import load_model
from multiprocessing import Pool

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
				seq_id1.append(seq_id)
				kmer1.append(line)
	return(seq_id1,kmer1)

def s1(k):
	texts_mono_fold = []
	texts_mono_fold.append(mono_hot_encode1(test12[k]))
	padded_docs3 = pad_sequences(texts_mono_fold, maxlen=400, padding='post') 
	texts_mono = []
	lab = testlab[k]
	texts_mono.append(mono_hot_encode(testseq[k]))
	padded_docs4 = pad_sequences(texts_mono, maxlen=400, padding='post')
	return lab, padded_docs4, padded_docs3


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

model = load_model('DeepPlnc_model.h5')
testseq=[]
testlab=[];test12=[]
for i in open(filename_2):
	z=i.split()
	testlab.append(str(z[0]))
	testseq.append(str(z[1]))
	test12.append(z[2])


name=[]
name = Pool().map(s1, [sent for sent in range(len(testseq))])
input_ids=[]
attention_masks=[]
attention_masks_fold=[]
for i, j in enumerate(name):
	input_ids.append(name[i][0])	
	attention_masks.append(name[i][1])
	attention_masks_fold.append(name[i][2])

train_inp = numpy.array(attention_masks).reshape(len(numpy.array(attention_masks)),400,4,1);attention_masks=[]
train_label = numpy.array(input_ids);input_ids=[]
train_fold = numpy.array(attention_masks_fold).reshape(len(numpy.array(attention_masks_fold)),400,3,1);attention_masks_fold=[]

y_pred = model.predict([train_inp,train_fold])
for j,i in enumerate(y_pred):
	print(train_label[j],i)



