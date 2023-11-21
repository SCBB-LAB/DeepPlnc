# DeepPlnc

<h2>Introduction</h2>

Long non-coding RNAs (lncRNAs), characterized as RNA transcripts longer than 200 nucleotides without functional open reading frames, play critical regulatory roles in various biological and developmental processes in both animals and plants. Despite their recent discovery and intriguing potential functions, lncRNA characterization remains a significant challenge, particularly in plants due to limited information, distinct transcriptional patterns, low sequence conservation, and scarce resources for credible annotation in plant genomes and transcriptomes. This highlights the need for novel tools to effectively identify and characterize plant lncRNAs.

We introduce DeepPlnc, a deep learning-based software for accurately identifying plant lncRNAs across various plant genomes. Unlike most existing tools, DeepPlnc can even annotate incomplete length transcripts. It employs a bi-modal architecture of Convolutional Neural Networks (CNNs) to extract information from both the nucleotide sequence and secondary structure of plant lncRNAs, enabling accurate lncRNA identification.

<h2>1. Data information</h2>
The user needs to provide RNA-seq data or any nucleotide sequence data in a fasta format as an input. This data undergoes analysis via trained bi-modal Convolutional Neural Networks (CNNs), resulting in the generation of scores allocated to each provided sequence. These scores serve as an output, offering insights or assessments derived from the analysis conducted by the CNNs.

<h2>2. Web server</h2>
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
8. python module multiprocessing, Bio, bayesian-optimization 

==================
*File description*
==================

1. DeepPlnc.sh = Complete execution script.
2. DeepPlnc.py = Python script for detecting lncRNAs from sequences provided.
3. Model_A.h5 = Trained model have traditionally considered negative dataset of just mRNAs.
4. Model_B.h5: Trained model has one-third of the negative dataset having plant rRNAs and tRNAs, along with two-third of it having mRNAs.
5. test = fasta sequence. (Minimum 200 bases in length)
6. make-plot.py = Python script for box and violin plot generation for a single sequence.
7. batch-plot.py = Python script for violin plot generation for a batch (10 sequence).
8. predict_GPU.py = Python script for detecting lncRNAs utilizing GPU.
9. file_format_GPU = file format of input for script predict_GPU.py. file containing seq_id, sequence (sequence length of >= 200 bases but not > 400 bases), and secondary structure(dot bracket). All in one line separated by tab for a single instance.
10. model_hyper.py = Python script build model implementing hyperparameter tuning

==================
*Running script*
==================
To predict the lncRNAs, In parent directory execute following command:

sh DeepPlnc.sh test /usr/local/bin/ A

1. test = test file.
2. /usr/local/bin/ = Path of RNAfold in your local system
3. A = Model to be selected for classification (Options : A|B)

python3 predict_GPU.py file_format_GPU # to detect lncRNA utilizing GPU

NOTICE: When you run DeepPlnc, please make sure there are no folder named "plot" in parent directory, otherwise it will give unnecessary warning:

mkdir: cannot create directory ‘plot’: File exists 

To plot box and violin plot for a single sequence, switch to directory name "plot" and execute following command:

python3 ../make-plot.py seq1 (sequences file name without ".csv")

To plot violin plot for a batch (10 sequence), switch to directory name "plot" and execute following command:

python3 ../batch-plot.py batch_1 (batch file name without ".csv")

To build model implementing hyperparameter tuning

python3 model_hyper.py file_for_tuning

file_for_tuning: file containing label, sequence (sequence length of >= 200 bases but not > 400 bases), and secondary structure(dot bracket). All in one line separated by tab for a single instance. 

==================
*Output description*
==================

lncRNA detection module (DeepPlnc) gives output in following format 

1. test.txt = Chunks wise probability score of the sequence provided.
2. test_results.tsv = Classification result of the sequence provided.
3. plot = folder containing "csv" files to construct violin and line plot.
4. seq.txt = Hyparameters for sequence side of bi-modal
5. struc.txt = Hyparameters for structure side of bi-modal

==================
*Citation*
==================

Citation: Ritu, Gupta S, Sharma NK, Shankar R (2022) DeepPlnc: Discovering plant lncRNAs through multimodal deep learning on sequential data. Genomics, 2022. https://www.sciencedirect.com/science/article/pii/S0888754322001884
