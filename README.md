# Protein-protein interaction classification with LSTM-RNN in Keras
Biology-related word embeddings can be downloaded from https://github.com/cambridgeltl/BioNLP-2016, and put in bio_nlp_vec/PubMed-shuffle-win-2.txt

## Create vocab

```bash
python vocab_creator.py -datadir AIMED -outputfile AIMED/AIMed_tokenized.vocab
```


## Run 
How to run
```bash
python train_keras.py  -data  AIMED/AIMed_tokenized -embeddings_file bio_nlp_vec/PubMed-shuffle-win-2.txt

```
