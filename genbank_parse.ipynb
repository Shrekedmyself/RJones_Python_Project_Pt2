{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "9220b8f1-f635-44c0-bc54-3eac427caea7",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Part 2\n",
    "\n",
    "## Biopython Exercise 1: Parse Genbank Files!!!!\n",
    "\n",
    "### Download the following NCBI genbank files\n",
    "#### Assumes that the files are in your current working directory"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "fe95051b-f581-49aa-a37f-49df4ccf4c98",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: Biopython in /Users/rileyjones/anaconda3/envs/pandas_practice/lib/python3.9/site-packages (1.83)\n",
      "Requirement already satisfied: numpy in /Users/rileyjones/anaconda3/envs/pandas_practice/lib/python3.9/site-packages (from Biopython) (1.26.4)\n"
     ]
    }
   ],
   "source": [
    "!pip install Biopython #Can uncomment this if it's already satisfied\n",
    "from Bio import Entrez\n",
    "from Bio import SeqIO\n",
    "import os\n",
    "import csv"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "c67a3bce-498f-4a77-b5b2-a965358a1e39",
   "metadata": {},
   "outputs": [
    {
     "ename": "AttributeError",
     "evalue": "'SeqRecord' object has no attribute 'family'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[7], line 27\u001b[0m\n\u001b[1;32m     24\u001b[0m genbank_records \u001b[38;5;241m=\u001b[39m parse_genbank(directory_path)\n\u001b[1;32m     26\u001b[0m \u001b[38;5;66;03m# Creating a CSV file from our parsed GenBank records\u001b[39;00m\n\u001b[0;32m---> 27\u001b[0m \u001b[43mcreate_csv_from_records\u001b[49m\u001b[43m(\u001b[49m\u001b[43mgenbank_records\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[38;5;124;43msequences_info.csv\u001b[39;49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[43m)\u001b[49m\n",
      "Cell \u001b[0;32mIn[7], line 17\u001b[0m, in \u001b[0;36mcreate_csv_from_records\u001b[0;34m(records, csv_filename)\u001b[0m\n\u001b[1;32m     15\u001b[0m writer\u001b[38;5;241m.\u001b[39mwriteheader() \u001b[38;5;66;03m#Using the variable we just created to, you'll never believe it, write a header\u001b[39;00m\n\u001b[1;32m     16\u001b[0m \u001b[38;5;28;01mfor\u001b[39;00m record \u001b[38;5;129;01min\u001b[39;00m records: \u001b[38;5;66;03m#Using a for loop to iterate through our records\u001b[39;00m\n\u001b[0;32m---> 17\u001b[0m     writer\u001b[38;5;241m.\u001b[39mwriterow({\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mAccession\u001b[39m\u001b[38;5;124m\"\u001b[39m: record\u001b[38;5;241m.\u001b[39mid, \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mFamily\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[43mrecord\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mfamily\u001b[49m, \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mGenus\u001b[39m\u001b[38;5;124m\"\u001b[39m: record\u001b[38;5;241m.\u001b[39mgenus, \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mSpecies\u001b[39m\u001b[38;5;124m\"\u001b[39m: record\u001b[38;5;241m.\u001b[39mspecies, \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mNum_Features\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;28mlen\u001b[39m(record\u001b[38;5;241m.\u001b[39mfeatures) })\n",
      "\u001b[0;31mAttributeError\u001b[0m: 'SeqRecord' object has no attribute 'family'"
     ]
    }
   ],
   "source": [
    "def parse_genbank(directory): #Creating our function with 'directory' as its argument\n",
    "    genbank_records = [] #Empty list obvi\n",
    "    for filename in os.listdir(directory): #Using the module 'listdir' from os to create a for loop\n",
    "        if filename.endswith(\".gb\"):  # Checking if the file is a GenBank file (ends in \".gb\"\n",
    "            filepath = os.path.join(directory, filename) #Setting the file path using the os module functions \"path\" and \"join\"\n",
    "            #This is accomplished by using the syntax \"module.function1.function2\"\n",
    "            records = SeqIO.parse(filepath, \"genbank\") #Using the \"SeqIO.parse\" function with our previous filepath variable and specifying the \"genbank\" file type\n",
    "            genbank_records.extend(records) #Using the \"extend\" function to add records to the end of genbank_records\n",
    "    return genbank_records\n",
    "\n",
    "def create_csv_from_records(records, csv_filename): #Defining our new function with \"records\" and \"csv_filename\" as our two arguments\n",
    "    with open(csv_filename, \"w\", newline=\"\") as csvfile: #Using with (so we don't have to close our file at the end :)\n",
    "        fieldnames = [\"Accession\", \"Family\", \"Genus\", \"Species\", \"Num_Features\", \"Source\"] #Setting our \"fieldnames\" list variable to a list of these fine headers\n",
    "        writer = csv.DictWriter(csvfile, fieldnames=fieldnames) #Using the \"csv\" module's `DictWriter()` function to create a csv file with our field names being, you guessed it, our previous variable\n",
    "        writer.writeheader() #Using the variable we just created to, you'll never believe it, write a header\n",
    "        for record in records: #Using a for loop to iterate through our records\n",
    "            writer.writerow({\"Accession\": record.id, \"Family\": record.family, \"Genus\": record.genus, \"Species\": record.species, \"Num_Features\": len(record.features) }) \n",
    "            #Defining our rows accordingly using data from our records\n",
    "            #I couldn't figure out how to get this to work, had considered even using the `bio taxon --lineage` method but I couldn't figure it\n",
    "            #Out even when I had downloaded the files and sometimes it would say it wouldn't do the lineage even when I did `bio fetch ____`\n",
    "\n",
    "# Specifying the directory containing GenBank files (should be your current directory!!! I put the files in my current directory so please change if need be)\n",
    "directory_path = os.getcwd()\n",
    "\n",
    "# Specifying our wonderful file names with a list\n",
    "filenames = [\n",
    "    \"NZ_CALPCP010000001_1\",\n",
    "    \"NZ_CALPCY010000130_1\",\n",
    "    \"NZ_BHVZ01000001_1\",\n",
    "    \"NZ_SRYA01000017_1\",\n",
    "    \"NZ_CAJTFZ010000019_1\"\n",
    "]\n",
    "\n",
    "# Parsing our .gb files from the cwd\n",
    "genbank_records = parse_genbank_files(directory_path, filenames)\n",
    "\n",
    "# Creating a .csv file!!!\n",
    "create_csv_from_records(genbank_records, \"sequences_info.csv\")\n"
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
