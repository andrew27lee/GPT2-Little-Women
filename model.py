import gpt_2_simple as gpt2
import os
import requests

MODEL_NAME = '124M'  # Specify which GPT-2 model is downloaded (Compatible with 124M and 355M models)
STEP_COUNT = 100  # Specify how many training steps are run (Do not exceed 1000 steps)


def download_text(file_name):
    """
    Download text used for training from URL to local text file
    :param filename: Name of local text file
    :param url: Web URL containing text required for training
    :return: None
    """
    url = 'https://www.gutenberg.org/cache/epub/514/pg514.txt'
    data = requests.get(url)
    
    with open(file_name, 'w') as f:
        f.write(data.text)


if __name__ == '__main__':
    if not os.path.isdir(os.path.join('models', MODEL_NAME)):
        print(f'Downloading {MODEL_NAME} model...')
        gpt2.download_gpt2(model_name = MODEL_NAME)
        print(f'Model {MODEL_NAME} download completed')

    file_name = 'LittleWomen.txt'
    if not os.path.isfile(file_name):
        download_text(file_name)

    sess = gpt2.start_tf_sess()
    print(f'Training GPT-2 model with {file_name}, Steps = {STEP_COUNT}')
    gpt2.finetune(sess, file_name, model_name = MODEL_NAME, steps = STEP_COUNT)
