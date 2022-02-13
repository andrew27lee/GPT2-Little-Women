from flask import Flask, request, render_template
import gpt_2_simple as gpt2

app = Flask(__name__)
sess = gpt2.start_tf_sess()
print('Downloading trained GPT-2 model...')
gpt2.load_gpt2(sess)
print('Download complete')


@app.route('/gpt2', methods=['POST'])
def main():
    data = dict(request.form) # Improve the service later to accept additional parameters (ex. length)

    if 'prefix' in data and data['prefix']:
        prefix = data['prefix']

        print("Generating text")
        generated_text = gpt2.generate(sess, prefix=prefix, length=400, return_as_list=True)[0]
        print("Text generation complete")
        
        # Organizing generated text
        word_list = generated_text.split()
        formatted_text = ""
        for word in word_list:
            formatted_text += word + " "
        formatted_text = formatted_text[:-1]

        data = {'generated_text': formatted_text}
        return render_template('index.html', result=data)
    else:
        return render_template('index.html', result=None)


@app.route('/')
def default():
    return render_template('index.html', result=None)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
