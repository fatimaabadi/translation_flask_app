# translation_flask_app
<img width="1197" height="522" alt="image" src="https://github.com/user-attachments/assets/a1fed6a0-b6c3-45cc-8ca6-5380bcc76b12" />

git clone <repo_url>
cd <repo_folder>
docker build -t translation-app .
docker run -p 10000:10000 translation-app
Live Demo: https://translation-flask-app-iqn4.onrender.com

The model will likely perform decently on simple, frequent phrases.

Errors or strange outputs may appear on more complex sentences.

To improve:

Use attention mechanisms (Bahdanau or Luong).

Train on a larger dataset.

Use beam search decoding instead of greedy argmax.

Use pretrained embeddings.

Perform more advanced data cleaning, including punctuation and casing handling
Now that the model has been trained, it's important to evaluate its performance. Based on the test translations above, we can see some initial results.

Consider the suggestions for improvement outlined previously:

Attention Mechanisms: Implementing attention can help the model focus on relevant parts of the input sequence during translation.
Larger Dataset: Training on a more extensive dataset will expose the model to a wider variety of sentence structures and vocabulary.
Beam Search Decoding: Beam search can produce more accurate translations compared to greedy decoding by exploring multiple possible output sequences.
Pretrained Embeddings: Using pretrained word embeddings can leverage knowledge from large corpora and potentially improve translation quality.
Advanced Data Cleaning: Further data cleaning, including handling punctuation, casing, and potentially rare words, could enhance the model's ability to process and translate sentences accurately.
Depending on the desired level of accuracy and complexity, you can choose to implement one or more of these improvements.
