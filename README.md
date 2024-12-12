### Workflow: Applying artificial neural networks to build models to analyze customer emotions based on comments and evaluation serves for determination business-related trends

![workflow](https://github.com/ZeusCoderBE/NLP-clustering-word--Vietnamese-Sentiment-Analysis/assets/117000361/07f725cc-ff77-4909-a9bd-62265e478cb9)

### I.Data Information:

- **Train Data:** 7,786 samples
- **Dev**: 1,112 samples
- **Test Data:** 2,224 samples
- **Link:** [Dataset Repository](https://github.com/LuongPhan/UIT-ViSFD?tab=readme-ov-file)

### II.Attribute Information:
1. **id** : the id of comment
2. **comment:** Commentary content
3. **n_star:** User rating for the smartphone (stars)
4. **data_time:** Date and time the comment was posted
5. **label:** Sentiment label of the comment


### III.Inferential analysis and exploratory analysis

##### 1.The chart shows customers' ratings of products over time

<img width="750" alt="image" src="https://github.com/user-attachments/assets/05fad310-6f22-4692-ab33-047dfb1157a9">




###### Based on the chart above, in the years from early 2017 to early 2019, customer reviews for products were quite high, averaging about 4.5. But between mid-2019 and the end of 2020, average reviews dropped alarmingly, demonstrating that customers are very dissatisfied with the quality of our products or services. It is necessary to urgently re-check product or service quality management steps to improve the situation

##### 2.The chart shows the number of labels evaluated over time

<<img width="767" alt="image" src="https://github.com/user-attachments/assets/a3dfc50c-53da-44fa-ab6e-04c7c74cf440">

###### We can see that the number of Positive Reviews is always more than other categories. Another notable point is that from early 2019 to mid-2020, the number of classified ad reviews increased rapidly, meaning the number of customers skyrocketed during that time.

##### 3.The line graph shows the number of reviews for each status by word count

![image](https://github.com/user-attachments/assets/1b365a85-5edf-4b21-ac52-6d372ef71e08)

###### It is observed that users tend to use less than 40 words to rate. The number of Positive reviews is always higher than Negative, this is a good sign for the product business.

##### 4.The heatmap chart represents the correlation matrix for the columns positive count, negative count, neutral_count, n_star

![image](https://github.com/user-attachments/assets/7042acaf-7c98-4e6f-8171-3eb79e22d149)

##### The chart shows that the positive_count value is positively correlated with n_star (correlation index 0.65), meaning that in user reviews, the higher the number of positive_count words, the higher the likelihood that that user will give a high rating. On the contrary, the negative_count value is negatively correlated with n_star (correlation index -0.69), meaning that in user reviews, the more negative_count words there are, the lower the rating will be.

### IV.Visualize word context and semantic correlation

### 5.1.Ploting learning curves BERT-fine-tuned for sentiment analysis:
![image](https://github.com/user-attachments/assets/7fbb5e93-e7e5-418d-aedc-ded96990e06e)

### 5.2.Ploting learning curves LSTM for sentiment analysis:
![image](https://github.com/ZeusCoderBE/NLP-clustering-word--Vietnamese-Sentiment-Analysis/assets/117000361/14d6044e-8480-412d-b057-ba0d9b6acced)


### 5.3.Ploting learning curves Hybrid CNN with LSTM for sentiment analysis:
![image](https://github.com/ZeusCoderBE/NLP-clustering-word--Vietnamese-Sentiment-Analysis/assets/117000361/cffe57cd-0338-4207-bb12-a213c706f330)


