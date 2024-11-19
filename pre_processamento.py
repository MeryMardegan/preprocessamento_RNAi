#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Pré-processamento


# In[ ]:


#Análisando o sequenciamento utilizando o fastp
fastp -i SRR14578729_1.fastq.gz -I SRR14578729_2.fastq.gz -o output_forward_clean.fq -O output_reverse_clean.fq --detect_adapter_for_pe --trim_front1 10 --trim_front2 10 --length_required 50 --qualified_quality_phred 30 --correction


# In[ ]:


#Baixando o genoma de Drosophila
wget https://ftp.flybase.net/genomes/Drosophila_melanogaster/dmel_r6.60_FB2024_05/fasta/dmel-all-chromosome-r6.60.fasta.gz 


# In[ ]:


#Baixando o gff de Drosophila
wget https://ftp.flybase.net/genomes/Drosophila_melanogaster/dmel_r6.60_FB2024_05/gff/dmel-all-r6.60.gff.gz


# In[ ]:


#Indexando o genoma de referência através do HISAT2
hisat2-build Drosophila_melanogaster_genome.fa Drosophila_melanogaster_genome_index


# In[ ]:


#Alinhando as leituras ao genoma de referência
hisat2 -x Drosophila_melanogaster_genome_index -1 output_forward_clean.fq -2 output_reverse_clean.fq -S aligned_reads.sam


# In[ ]:


#Converter o arquivo SAM para o formato BAM e ordenação e criação de índice
samtools view -bS aligned_reads.sam > aligned_reads.bam
samtools sort aligned_reads.bam -o aligned_reads_sorted.bam
samtools index aligned_reads_sorted.bam


# In[ ]:


#Avaliação da qualidade do alinhamento
samtools flagstat aligned_reads_sorted.bam

