import sys
import re
from pprint import pprint as pp

def read_file(filename):
    with open(filename, mode='rt', encoding='utf-8') as f:
        line = f.readline()
    return line

def output_result(result):
    print('Paragraph Analysis')
    print('-' * 25)
    print(f'Approximate Word Count: {result["word_count"]}')
    print(f'Approximate Sentence Count: {result["sentence_count"]}')
    print(f'Average Letter Count: {result["average_letter_count"]}')
    print(f'Average Sentence Length: {result["average_sentence_length"]}')

def calculate_metrics(paragraph):
    columns = ["word_count", "sentence_count", "average_letter_count", "average_sentence_length"]
    row = []

    sentences = re.split("(?<=[.!?]) +", paragraph)
    # print(sentences[0])
    #Approximate word count
    words = paragraph.split(" ")
    word_count = len(words)
    row.append(len(words))
    #Approximate sentence count
    sentence_count = len(sentences)
    row.append(sentence_count)
    #Approximate letter count (per word)
    total_count_of_letters = sum([len(word) for word in words])
    row.append(round(total_count_of_letters/word_count, 2))
    #Average sentence length (in words)
    row.append(word_count/sentence_count)
    return {x[0]: x[1] for x in zip(columns, row)}

def main(filename):
    paragraph = read_file(filename)
    result = calculate_metrics(paragraph)
    output_result(result)

if __name__ == '__main__':
    main(sys.argv[1])
