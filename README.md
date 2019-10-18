# Protein-protein interaction classification with LSTM-RNN in Keras
Biology-related word embeddings can be downloaded from https://github.com/cambridgeltl/BioNLP-2016, and put in bio_nlp_vec/PubMed-shuffle-win-2.txt

## Pre-requisites

1. Install python 3.5


## Set up

1. Install dependencies, for a Cpu machine


    ```bash
    pip install -r requirments.txt
    pip install -r requirments_cpu.txt
    ```
1. Install dependencies, for a gpu machine


    ```bash
    pip install -r requirments.txt
    pip install -r requirments_gpu.txt
    ```
    
## Create vocab & run

```bash
#specify enter directory
export data_dir=AIMED

python vocab_creator.py -datadir ${data_dir} -outputfile ${data_dir}/AIMed_tokenized.vocab
python train_keras.py  -data  ${data_dir}/AIMed_tokenized -embeddings_file bio_nlp_vec/PubMed-shuffle-win-2.txt

```
