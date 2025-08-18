Mental Health Prediction Using LLM
# 🧠 Mental Health Prediction LLM
[![Python](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/16Ryhn8WmFloFnQJLlF4Gv1wPdBB5dryY)

## Project Overview
This project is a mental health prediction system built using BERT/DistilBERT for text classification. The model classifies user messages into three categories:
- Normal
- Depression
- Anxiety
The project demonstrates a full workflow: data preprocessing, tokenization, model fine-tuning with class weights, evaluation, and deployment with Gradio for interactive predictions.

## Motivation
Mental health is critical, and early detection of symptoms can help individuals seek timely support. This project provides a lightweight LLM-based system to classify user messages and flag potential risks, helping professionals or apps deliver better mental health insights.

## Dataset
- Text data consisting of user messages (`Context`) and responses (`Response`)  
- Target classes: `normal`, `depression`, `anxiety`  

Class distribution:
- Normal: 2241
- Depression: 702
- Anxiety: 565
Note: The dataset is preprocessed by combining relevant features and encoding labels for model training.

## Features

- Text-based input (Context + Response)
- Tokenization using BERT tokenizer
- Weighted loss to handle class imbalance
- Fine-tuning using Hugging Face Trainer
- Prediction API using Gradio interface

## Installation
```bash
git clone https://github.com/zaralrubaie/LLM-mental-health-classification.git
cd mental-health-LLM

# Install dependencies
pip install torch transformers gradio scikit-learn
```
## Usage 
1. Fine-tune the model
```python
trainer.train()
```
2. Evaluate the model
```python

val_results = trainer.evaluate(val_dataset)
print(val_results)
test_results = trainer.evaluate(test_dataset)
print(test_results)
```
3. Predict with Gradio
 ```python
 import gradio as gr
iface.launch()
```
Enter one or more messages (one per line)
Outputs: Predicted label + Class probabilities
Example inputs:
- I feel happy and relaxed today.
- I can’t stop worrying about work.
- I feel hopeless and tired of trying.

## Model & Training
- Model: BERT-base / DistilBERT (lighter & faster)
- Loss: Weighted Cross-Entropy
- Epochs: 3 (can reduce for quick testing)
- Validation Accuracy: ~82%
- Test Accuracy: ~81%

## License
MIT License © 2025 Zahraa Rubaie

