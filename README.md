# Anomaly-Detection-in-Bitcoin

## ABSTRACT
This project focuses on anomaly detection of the bitcoin transactions using unsupervised machine learning method [1]. In order to detect which users and transactions are the most suspicious, an anomaly detection model is developed with the help of isolation forest algorithm to prevent future illegal actions. The developed model initially extracts all bitcoin transaction data and various features of the same. The incorporated isolation forest algorithm isolates observations by arbitrarily choosing a
feature and afterward split the value amongst most extreme and least ones of the selected features. The anomalies are detected by running developed the isolation forest model and the most suspicious transactions are determined for corrective action.

## INTRODUCTION
Network structures have appeared for a long time, and along with them are those who behave abnormally within the system. We refer to these people or their illegal activities as anomalies. In financial networks, thieves and their illegal activities are called as anomalies. Members of a network want to detect anomalies as soon as possible to prevent them from creating problems in the network’s community and integrity.
Bitcoins are digital currencies that works on technology called blockchain, which is a public electronic ledger that is openly shared among the nodes in the network and creates an unchangeable record of the transactions.

## OBJECTIVE
The objective is to detect which users and transactions are the most suspicious by creating a web application that help in the anomaly detection in Bitcoin network based upon Machine Learning model.

The **sub objectives** incidental to the main objective are: 
• Collect Bitcoin transactional data and preprocessing the data.
• Developing the Machine Learning model using Isolation Forest based on the
above problem statement.
• Build a web application: To create two parts
Front-end (designed using HTML, CSS)
Back-end (designed using Flask Framework)
• Integrating Machine Learning model into Flask.


