{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "73f54445-2960-47df-a3d0-ad1535ee4072",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Biopython Exercise 3: Analyze a genome!!!! Whooooooooo\n",
    "\n",
    "## 1) Download the fasta file for NCBI accession GCA_000287275.1. This is the bacteria with the smallest known genome. It is 166.2 kilobases.\n",
    "\n",
    "## 2) Write a python script called genbank_parse.py that is executable on the command line that is called ruddi_analysis.py. \n",
    "## This script should output a csv called ruddi.csv that has the length of the genome, the GC content of the genome, the number of times that the sequence ‘ATG’ appears in the sequence (the forward strand), and the number of times that ‘ATG’ appears in the reverse strand (the reverse complement). \n",
    "## You should use biopython’s parsing of seq and seqrecord objects and seq methods to accomplish this.\n",
    "\n",
    "### Assumes all files are in your current working directory"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ba3c9ecc-6a1a-437d-9b1d-d0a10d055670",
   "metadata": {},
   "outputs": [],
   "source": [
    "from Bio import SeqIO\n",
    "import pandas as pd\n",
    "from Bio.Seq import Seq\n",
    "\n",
    "def analyze_genome(genbank_file): #Defining our function\n",
    "    records = SeqIO.parse(genbank_file, \"fasta\") #Using `SeqIO`'s `parse()` function on our genbank file in fasta format\n",
    "    for record in records: #Create a for loop\n",
    "        genome_length = len(record.seq) #Getting the length of our record's sequence\n",
    "        gc_content = (record.seq.count(\"G\") + record.seq.count(\"C\")) / genome_length * 100 #Setting up a simple GC percentage\n",
    "        #Wasn't sure if I should do the above or the below so I included both:\n",
    "        #gc_content = record.seq.count(\"GC\") / genome_length * 100\n",
    "        ATG_forward = record.seq.count(\"ATG\") #Counting the number of times that 'ATG' appears in our sequence\n",
    "        reverse_complement = record.seq.reverse_complement() #Creating the reverse complement\n",
    "        ATG_reverse = reverse_complement.count(\"ATG\") #Counting the number of times that our reverse complement has ATG\n",
    "        return genome_length, gc_content, forward_atg_count, reverse_atg_count #Return all these useful values\n",
    "\n",
    "def super_function(genbank_file, output_csv): #Defining our 'super' function\n",
    "    genome_length, gc_content, forward_atg_count, reverse_atg_count = analyze_genome(genbank_file)\n",
    "    #Calling the `analyze_genome()` fx to output our four variables\n",
    "    data = { #Creating a python dictionary\n",
    "        \"Metric\": [\"Genome Length\", \"GC Content\", \"Forward ATG Count\", \"Reverse ATG Count\"],\n",
    "        #Using our key 'Metric' to be these four strings\n",
    "        \"Value\": [genome_length, gc_content, forward_atg_count, reverse_atg_count]\n",
    "        #Using our key 'Value\" to be these four variables\n",
    "    }\n",
    "    df = pd.DataFrame(data) #Saving our 'data' variable as a pandas DataFrame\n",
    "    df.to_csv(genome_csv, index=False) #Saving it to a .csv called genome_csv\n",
    "\n",
    "if __name__ == \"__main__\": #Specifying with a logical that we cannot call it with a module\n",
    "    fna_file = \"GCA_000287275.1_ASM28727v1_genomic.fna\"  # Assumes files are in your cwd\n",
    "    output_csv = \"ruddi.csv\" #Creating our actual output .csv\n",
    "    main(fna_file, genome_csv) #Finishing touch"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.18"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
