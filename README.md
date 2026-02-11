Submitted by: Anzuman Ara
Student ID: 20241266
# M4 Portfolio Assignment 2 — Green Patent Detection (PatentSBERTa)
Active Learning + LLM → Human HITL

Green Patent Classification using Human-in-the-Loop Learning

This project focuses on building a machine learning pipeline to classify whether a patent is related to green technology. The main goal is to improve classification performance by combining automated labeling with human feedback using a Human-in-the-Loop (HITL) approach.

Project Overview

In this project, I start with automatically generated labels (silver labels) and train a baseline model using frozen PatentSBERTa embeddings. After that, I identify uncertain samples and simulate human annotation to improve data quality. Finally, I fine-tune the PatentSBERTa model and upload both dataset and trained model to Hugging Face.

Workflow

The project is divided into five main parts:

Part A — Baseline Model

First, I used PatentSBERTa embeddings to convert patent text into numerical vectors.
A Logistic Regression model was trained using these embeddings.

Embeddings were generated using a frozen encoder.

The model was trained on silver labeled data.

Performance was evaluated using precision, recall, and F1 score.

Part B — Uncertainty Sampling

After building the baseline model, I identified uncertain predictions.

Prediction probabilities were used to detect samples near the decision boundary.

These uncertain samples were selected for further human review.

This step helps focus human effort on the most difficult cases.

Part C — Human-in-the-Loop Labeling

In this stage, selected uncertain samples were manually labeled.

Human labeled data (gold labels) was merged with existing silver data.

This improves overall label quality and training data reliability.

Part D — Model Fine-tuning

The PatentSBERTa model was fine-tuned using the improved dataset.

Hugging Face Trainer API was used.

The model was trained using updated labeled data.

Evaluation metrics were calculated after training.

Fine-tuning helps the model learn domain-specific patterns more effectively.

Part E — Hugging Face Deployment

Finally, both dataset and trained model were uploaded to Hugging Face Hub.

Dataset:
https://huggingface.co/datasets/id66pj/m4-green-patent-hitl-dataset

Model:
https://huggingface.co/id66pj/m4-green-patent-model

This allows easy sharing and reuse of the model and data.

Technologies Used

Python

Scikit-learn

Sentence Transformers

Hugging Face Transformers

Hugging Face Hub

Pandas

NumPy

Key Learning Outcomes

Through this project, I learned:

How to build an end-to-end NLP classification pipeline

How embeddings improve text representation

How Human-in-the-Loop learning improves label quality

How to fine-tune transformer-based models

How to deploy models using Hugging Face

Conclusion

This project demonstrates how combining automated machine learning methods with human feedback can significantly improve classification performance. The HITL approach ensures better data quality and model reliability, which is especially important in specialized domains like green patent classification.

github link: https://github.com/anzuman-ara389/m4-green-patent-hitl