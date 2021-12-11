===============
*Description*
===============
DeepPlnc: A tool for discovering plant lncRNAs through multimodal deep learning on sequential data

Long noncoding RNAs (lncRNAs) can be characterized as RNA transcripts with minimum length of 200 bases, and with short ORFs which are not translated into functional proteins. These lncRNAs plays pivotal role on the regulation in a wide range of biological and developmental processes in animals and plants. Among them the lncRNAs are very recent and most intriguing for their possible functions. Due to limited information about lncRNAs, their characterization remains a big challenge, especially in plants. Plant lncRNAs differ a lot from animal’s even in the mode of transcription as well as display poor sequence conservation. Scarce resources exist to annotate plant genomes and transcriptomes for lncRNAs with good credibility.
Here, we present a deep learning approach-based software, DeepPlnc, to accurately identify plant lncRNAs across the plant genomes. DeepPlnc, unlike most of the existing software, can even accurately annotate the incomplete length transcripts also. It has incorporated a bi-modal architecture of Convolution Neural Nets (CNNs) while extracting information from the sequence of nucleotides and sequence of secondary structures of plant lncRNAs.

The user needs to provide the RNA-seq or any other sequence data in fasta format. This data is run through the trained bi-modal CNN which generates a scores for each sequence provided. 

The lncRNA detection system has been implemented as a webserver at https://scbb.ihbt.res.in/DeepPlnc/. 

===============
*Requirements*
===============
1. Python3.6 or higher
2. Numpy
3. keras
4. tensorflow
5. plotly
6. pandas
7. RNAfold (ViennaRNA package download it from here: "https://www.tbi.univie.ac.at/RNA/")

==================
*File description*
==================

1. DeepPlnc.sh = Complete execution script.
2. DeepPlnc.py = Python script for detecting lncRNAs from sequences provided.
3. DeepPlnc_model.h5 = Trained model.
4. test = fasta sequence. (Minimum 200 bases in length)
5. make-plot.py = Python script for box and violin plot generation for a single sequence.
6. batch-plot.py = Python script for violin plot generation for a batch (10 sequence).

==================
*Running script*
==================
To predict the lncRNAs, In parent directory execute following command:

DeepPlnc.sh test /usr/local/bin/ (Path of RNAfold in your local system)

NOTICE: When you run DeepPlnc, please make sure there are no folder named "plot" in parent directory, otherwise it will give unnecessary warning:

mkdir: cannot create directory ‘plot’: File exists 

To plot box and violin plot for a single sequence, switch to directory name "plot" and execute following command:

python3 ../make-plot.py seq1 (sequences file name without ".csv")

To plot violin plot for a batch (10 sequence), switch to directory name "plot" and execute following command:

python3 ../batch-plot.py batch_1 (batch file name without ".csv")

==================
*Output description*
==================

lncRNA detection module (DeepPlnc) gives output in following format 

test.txt = Chunks wise probability score of the sequence provided.
test_results.tsv = CLassification result of the sequence provided.
plot = folder containing "csv" files to construct violin and line plot.



==================
*Citation*
==================

Citation: Ritu, Gupta S, Sharma NK, Shankar R (2021) DeepPlnc: Discovering plant lncRNAs through multimodal deep learning on sequential data. bioRxiv 2021. https://www.biorxiv.org/content/10.1101/2021.12.10.472074v1
