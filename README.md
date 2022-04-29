# CS 221 - Determining Virality of TED Talks

By: Joseph T. Guman, Joseph C. O’Brien, Christopher L.M. Pondoc, Travis R. Senf

## Problem Statement and Task Definition
The real-world problem our system is trying to solve is predicting the virality of a TED talk based on its content. Our system inputs the title and manuscript of a TED talk and outputs its level of virality. In other words, we are solving a multi-class classification problem using word features.

Regarding its real-world applications, the system can be utilized to determine what types of educational content are most effective in inducing learning. While virality is not a perfect metric for measuring such an impact, we can assume that virality implies widespread adoption of concepts, showing that if we can understand what features matter to these TED talks, we can help teachers plan out their lessons.

## Input/Output Behavior and Concrete Examples
We are planning to utilize the TED Talks dataset found on Kaggle. Concrete examples of inputs and outputs are the following:
- Inputs: This dataset includes a variety of different information about the Ted talk videos that give us the leeway to experiment with what inputs we would like to include to generate the best outcome. 
- We currently plan to start with using the text manuscripts and titles of the videos as our main parameters and adding the speaker's occupation, comment information, etc. 
- Outputs: We plan on using the number of views associated with each video to slot the talk into different buckets (for example: low virality, moderate virality, high virality) in a multi-class classification method.

## Evaluation Metrics
We are planning to turn the problem of predicting virality into a multi-class classification problem. To create the classes, we plan to analyze the distribution of the number of views of the TED talks and determine appropriate buckets for relative evaluation. Furthermore, we plan to create a script that will automatically break up our dataset into a parameter training set, hyperparameter set, and test set. The accuracy will be decided by the percent accuracy of successfully guessing the virality bucket. Finally, we will test our model purely by the ability to consistently create a high accuracy in the testing set for each iteration of a given training.

## Related Works
We look at works that determine the virality of various internet phenomena:
- A project by Ming Cheung was designed to predict the timing of virality of internet phenomena, such as tweets, by monitoring social cascades.
- A study of the success of Kickstarter campaigns by Alex Kindler looked to link vitality to said success but found that virality actually played a minor role. It found that success is primarily correlated to appeal to high-pledge backers usually influenced largely by themselves.
- When attempting to predict hashtag virality, Siddharth Bora found that conductance-based features most heavily influenced the virality of a given hashtag, and predicting virality based on the second derivative of the conductance of a given tweet was very effective.
- Liqun Gao developed a virality prediction model for public opinion information, with its features based primarily on emotional polarity ratio, semantic evolution, and dissemination scale.

## Baseline and Oracle
A baseline algorithm for our multi-class virality classifier would be an algorithm that classifies the most common class of viral TED talks. While this may seem trivial at first, note that the virality of TED talks follows a power law: there are a high number of non-popular TED talks, while there are only a small number of extremely popular TED talks.

An oracle for our algorithm would be to have each member of our team read through the manuscripts of 10 TED talks, predict their virality, and measure the agreement rate. While human accuracy will not be 100%, the oracle would provide a relatively good upper bound.

## Methodology
We will be developing a feature extractor using a variety of techniques to be fed into a neural network. We will be focusing mainly on natural language processing to best craft our feature extractor, using the NLTK Python package to accomplish this goal. Furthermore, we will be focusing on multi-class classification – would be rather difficult to determine generally the number of views, but a ballpark.

## Description of the Challenges
One challenge will involve finding the proper details to include for the algorithm to use in classification. Starting with the manuscript and title, we intend to iteratively add different features in the Ted talks to see what features will aid in classification. We fear that immediately adding all features and manually checking the magnitude of parameters will give the possibility of overfitting. This will be good to help us get an intuition for future MLP problems.

It will also be difficult to come up with a descriptive feature extractor. With only 2,500 TED talks, brute-forcing learning may not be feasible, and we may need to develop domain-specific heuristics. This will be a good exercise for developing future strategies in special texts.

