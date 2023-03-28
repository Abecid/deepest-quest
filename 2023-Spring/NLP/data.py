import pandas as pd

def get_data():    
    train_data_path = 'https://raw.githubusercontent.com/Abecid/deepest-quest/main/2023-Spring/NLP/data/utkmls-twitter-spam-detection-competition/train.csv'
    test_data_path = 'https://raw.githubusercontent.com/Abecid/deepest-quest/main/2023-Spring/NLP/data/utkmls-twitter-spam-detection-competition/test.csv'

    
    train_data_path = '/Users/abecid/Downloads/Projects/deepest-quest/2023-Spring/NLP/dataset/utkmls-twitter-spam-detection-competition/train.csv'
    test_data_path = '/Users/abecid/Downloads/Projects/deepest-quest/2023-Spring/NLP/dataset/utkmls-twitter-spam-detection-competition/test.csv'
    
    train_data = pd.read_csv(train_data_path)[["Tweet", "Type"]]
    test_data = pd.read_csv(test_data_path)[["Tweet"]]

    # 0: Quality, 1: Spam
    train_data['Type'] = train_data['Type'].map({'Quality': 0, 'Spam': 100})
    return train_data, test_data