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

<img width="780" alt="image" src="https://github.com/user-attachments/assets/a32a875d-098e-46d7-a9fa-80cf10df64f4">


###### Based on the chart above, in the years from early 2017 to early 2019, customer reviews for products were quite high, averaging about 4.5. But between mid-2019 and the end of 2020, average reviews dropped alarmingly, demonstrating that customers are very dissatisfied with the quality of our products or services. It is necessary to urgently re-check product or service quality management steps to improve the situation

##### 2.The chart shows the number of labels evaluated over time

<img width="867" alt="image" src="https://github.com/user-attachments/assets/14c48267-2905-4ddb-9ff0-6217c11d7c6b">

###### We can see that the number of Positive Reviews is always more than other categories. Another notable point is that from early 2019 to mid-2020, the number of classified ad reviews increased rapidly, meaning the number of customers skyrocketed during that time.

### IV.Visualize word context and semantic correlation

### V.Ploting learning curves LSTM for sentiment analysis:
![image](https://github.com/ZeusCoderBE/NLP-clustering-word--Vietnamese-Sentiment-Analysis/assets/117000361/14d6044e-8480-412d-b057-ba0d9b6acced)


### VI.Ploting learning curves Hybrid CNN with LSTM for sentiment analysis:
![image](https://github.com/ZeusCoderBE/NLP-clustering-word--Vietnamese-Sentiment-Analysis/assets/117000361/cffe57cd-0338-4207-bb12-a213c706f330)


