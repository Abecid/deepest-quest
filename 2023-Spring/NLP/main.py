import csv

import gpt
import data

def main():
    # open the file in the write mode
    f = open('./dataset/results/result.csv', 'w')

    # create the csv writer
    writer = csv.writer(f)
    
    header = ['Id', 'Type']
    writer.writerow(header)
    
    train_data, test_data = data.get_data()
    test_data = test_data.Tweet.values.tolist()
    train_data_tweets = train_data.Tweet.values.tolist()
    train_data_labels = train_data.Type.values.tolist()
    
    chat_history = []
    i = 0
    step = 30
    while i < len(test_data):
        j = i + step if i + step < len(test_data) else len(test_data)
        print(i, j)
        train_batch = train_data.sample(n = 30)
        # train_tweets_batch = train_data_tweets[i:j]
        # train_labels_batch = train_data_labels[i:j]
        train_tweets_batch = train_batch.Tweet.values.tolist()
        train_labels_batch = train_batch.Type.values.tolist()
        test_batch = test_data[i:j]
        examples, classification_examples = get_examples(train_tweets_batch, train_labels_batch, test_batch)
        instruction = """
        Classify the likelihood of the following tweets as spam (100) or not spam(0) in the range of 0 to 100. :
        """
        # Only return the numbers don't repeat the tweets
        prompt = f"Examples:\n----------\n{examples}\n----------\n\n{instruction}\n\n{classification_examples}"
        print(prompt)
        # chat_history.append({"role": "user", "content": prompt})
        chat_history = [{"role": "user", "content": prompt}]
        results = gpt.chatGPT(chat_history)
        print(results)
        results = results.split('\n')
        results = [result.split(' ')[-1] if ' ' in result else result for result in results]
        save_to_csv(writer, results, i)
        i += step
        
    f.close()
    

def get_examples(train_data_tweets, train_data_labels, test_data):
    examples = """
    
    """
    classification_examples = """
    
    """
    
    for i in range(len(train_data_tweets)):
        examples += f"[{i}.] {train_data_tweets[i]}: {train_data_labels[i]}\n"
    
    for i in range(len(test_data)):
        classification_examples += f"[{i}.] {test_data[i]}\n"
    return examples, classification_examples

def save_to_csv(writer, results, i):
    j = 0
    for result in results:
        if len(result) > 0 and result[0].isnumeric():
            result = float(result)
            result = "Quality" if result < 50 else "Spam"
            writer.writerow([i+j, result])
            j += 1

if __name__ == "__main__":
    main()