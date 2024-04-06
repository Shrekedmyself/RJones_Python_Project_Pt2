{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b9958314-93f3-4ce9-98d9-3ec8de09e691",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Biopython Exercise 2: FASTA fun with protein!!! Yay...\n",
    "\n",
    "## 1) Download fasta files for NCBI protein accessions AGI40145.1, AGJ87295.1, WVV45440.1, and WVS05366.1\n",
    "\n",
    "## 2) Write a python script called genbank_parse.py that is executable on the command line that is called fasta_parse.py\n",
    "\n",
    "## 3) Fasta_parse.py should output a csv table called protein_info.csv that has the fasta IDs as row names, and as columns, the first 10 amino acids in the protein, the length of the protein, the number of cysteines in the protein. You should use biopython’s parsing of seq and seqrecord objects and seq methods to accomplish this\n",
    "\n",
    "### This assumes all files are in your current directory "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "783951c0-946f-425e-bd24-5d76d2694a44",
   "metadata": {},
   "outputs": [],
   "source": [
    "from Bio import SeqIO \n",
    "import csv\n",
    "\n",
    "def parse_fasta_files(fasta_files): #Defining our function\n",
    "    protein_info = [] #Setting our empty list\n",
    "    for fasta_file in fasta_files: #Creating a for loop to iterate through\n",
    "        with open(fasta_file, \"r\") as file: #Using `with()` so we do not have to use `f.in` or `f.out`\n",
    "            record = SeqIO.read(file, \"fasta\") #Creating the variable 'record' and assigning it to read a file in fasta format with `SeqIO`'s `read()` function\n",
    "            first_10_aa = str(record.seq[:10]) #Getting the first 10 aa's with using `str()` to get our record's seq(uence)\n",
    "            length = len(record.seq) #Setting our length variable to be the length of the amino acid sequence\n",
    "            num_cysteines = record.seq.count(\"C\") #Creating a variable to count for the number of cysteines in the record's sequence\n",
    "            protein_info.append({\"ID\": record.id, \"First10AminoAcids\": first_10_aa, \"Length\": length, \"NumCysteines\": num_cysteines}) \n",
    "            #Appending all of this to our 'protein_info' empty list\n",
    "    return protein_info\n",
    "\n",
    "def write_csv(protein_info, output_filename): #Creating our next function!!! Yay\n",
    "    with open(output_filename, \"w\", newline=\"\") as csvfile: #Using `with` and `open` to write our output csv file\n",
    "        fieldnames = [\"ID\", \"First10AminoAcids\", \"Length\", \"NumCysteines\"] #Creating our column headers\n",
    "        writing = csv.DictWriter(csvfile, fieldnames=fieldnames) #Creating a `writing` function that will use the `DictWriter()` function \n",
    "        writing.writeheader() #Writing our header\n",
    "        writing.writerows(protein_info) #Writing our rows using our previously created 'protein_info' variable\n",
    "\n",
    "if __name__ == \"__main__\": #Conditional which will allow code to run but not as a module\n",
    "    fasta_files = [\"AGI40145_1.fasta\", \"AGJ87295_1.fasta\", \"WVV45440_1.fasta\", \"WVS05366_1.fasta\"] #Once again, assumes these are in your cwd\n",
    "    protein_info = parse_fasta_files(fasta_files) #Creating a variable which is the output of our function with our given fasta files\n",
    "    write_csv(protein_info, \"protein_info.csv\") #Writing our .csv file!!!"
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
