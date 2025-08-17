from flask import Flask, request, render_template
import tensorflow as tf
import numpy as np
import pickle
import os
# Load tokenizers
with open("models/eng_tokenizer.pkl", "rb") as f:
    eng_tokenizer = pickle.load(f)

with open("models/fre_tokenizer.pkl", "rb") as f:
    fre_tokenizer = pickle.load(f)

# Load max lengths
with open("models/max_lengths.pkl", "rb") as f:
    max_lengths = pickle.load(f)

max_eng_len = max_lengths['max_eng_len']
max_fre_len = max_lengths['max_fre_len']

# Load models
encoder_model = tf.keras.models.load_model("models/encoder_model.keras")
decoder_model = tf.keras.models.load_model("models/decoder_model.keras")

# Reverse token dict
reverse_fre = {i: w for w, i in fre_tokenizer.word_index.items()}

app = Flask(__name__)

def decode_sequence(input_seq):
    states_value = encoder_model.predict(input_seq)
    target_seq = np.array([[fre_tokenizer.word_index['<start>']]])
    decoded_sentence = ''
    for _ in range(max_fre_len):
        output_tokens, h, c = decoder_model.predict([target_seq] + states_value)
        sampled_token_index = np.argmax(output_tokens[0, -1, :])
        sampled_word = reverse_fre.get(sampled_token_index, '')
        if sampled_word == '<end>' or sampled_word == '':
            break
        decoded_sentence += ' ' + sampled_word
        target_seq = np.array([[sampled_token_index]])
        states_value = [h, c]
    return decoded_sentence.strip()

@app.route('/', methods=['GET', 'POST'])
def index():
    translation = ''
    if request.method == 'POST':
        text = request.form['text']
        seq = eng_tokenizer.texts_to_sequences([text])
        seq = tf.keras.preprocessing.sequence.pad_sequences(seq, maxlen=max_eng_len, padding='post')
        translation = decode_sequence(seq)
    return render_template('index.html', translation=translation)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
