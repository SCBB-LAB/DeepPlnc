#!/bin/bash
awk '/^>/ {printf("\n%s\n",$0);next; } { printf("%s",$0);}  END {printf("\n");}' <$1 |sed '1d'|sed 's+\r++g'  >$1.fa
grep '>' $1.fa | sed 's+>++g' |sed 's+\r++g' >$1\_header.txt
cat $1.fa | tr 'AUGCaugcN' 'ATGCATGCA' | paste - - |awk '{print $1"\n"$NF}' >$1.fasta
python3 DeepPlnc.py $1.fasta $2 >$1\_python_res.txt
printf "Sequence\tChunk\tScore\n" >$1.txt
cat $1\_python_res.txt |sed 's+\[++g' |sed 's+]++g' |sed 's+>++g' |awk '{if($2>=1) {print $1"\t1.0000"}else {print $0}}' |sed 's+_+\t+g'  >>$1.txt
sed 's+>++' $1\_header.txt  | while read i ;do printf "Position,Score\n" >$i.csv ; grep -P "^$i\t" $1.txt |sed 's+\_+\t+1g'|awk '{print NR","$3}' >>$i.csv ;done
printf "Sequence\tClassification\n" >$1\_results.tsv
ls *csv|sed 's+.csv++g' | while read i ;do printf "$i\t" ; awk -F',' '{if($2>=0.5) print $0}'  $i.csv |wc -l |tr "\n" "\t" ; awk -F',' '{if($2<0.5) print $0}' $i.csv |wc -l ; done  >>sequence_results_pre.tsv
awk '{if($2>$3) {print $1"\tlncRNA"} else {print $1"\tNon-lncRNA"}}'  sequence_results_pre.tsv >>$1\_results.tsv
mkdir plot ;
naya_var=1; mv *.csv plot/
sed 's+>++' $1\_header.txt |while read a ; do read b ; read c ; read d ; read e; read f ; read g; read h;read i ;read j ; printf "<b>Sequence</b>,<b>Score</b>\n" > plot/batch\_$naya_var.csv; sed '1d' plot/$a.csv |awk -v var="$a" -F"," '{print  "<b>"var","$2}' >> plot/batch\_$naya_var.csv ; sed '1d' plot/$b.csv |awk -v var="$b" -F"," '{print  "<b>"var","$2}'>> plot/batch\_$naya_var.csv ; sed '1d' plot/$c.csv |awk -v var="$c" -F"," '{print  "<b>"var","$2}' >> plot/batch\_$naya_var.csv ; sed '1d' plot/$d.csv |awk -v var="$d" -F"," '{print  "<b>"var","$2}'>> plot/batch\_$naya_var.csv ; sed '1d' plot/$e.csv |awk -v var="$e" -F"," '{print  "<b>"var","$2}'>> plot/batch\_$naya_var.csv ; sed '1d' plot/$f.csv|awk -v var="$f" -F"," '{print  "<b>"var","$2}' >> plot/batch\_$naya_var.csv ; sed '1d' plot/$g.csv |awk -v var="$g" -F"," '{print  "<b>"var","$2}'>> plot/batch\_$naya_var.csv ; sed '1d' plot/$h.csv |awk -v var="$h" -F"," '{print  "<b>"var","$2}'>> plot/batch\_$naya_var.csv ; sed '1d' plot/$i.csv|awk -v var="$i" -F"," '{print  "<b>"var","$2}' >> plot/batch\_$naya_var.csv ; sed '1d' plot/$j.csv |awk -v var="$j" -F"," '{print  "<b>"var","$2}'>> plot/batch\_$naya_var.csv ; echo "batch_$naya_ "<b>"var" >>plot/$1\_new1.txt; naya_var=$((naya_var+1)) ; done

rm $1\_header.txt sequence_results_pre.tsv $1.fasta_coding.fa $1.fasta_RNA_coding $1.fasta $1.fa temp $1\_python_res.txt
