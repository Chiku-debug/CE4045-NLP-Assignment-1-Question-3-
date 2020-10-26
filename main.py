import string

from nltk.sentiment.vader import SentimentIntensityAnalyzer
from xlwt import Workbook
import matplotlib.pyplot as plot
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

positive_counter = 0
neutral_counter = 0
negative_counter = 0


def converting_list_to_string(s):
    # initialize an empty string
    new_string = " "
    return (new_string.join(s))

# function to remove punctuation characters from a sentence


def punctuation_removal(txt):
    non_punctuated_text = "".join([c for c in txt if c not in string.punctuation])
    return non_punctuated_text


def sentiment_detector(sentence):
    detection = SentimentIntensityAnalyzer().polarity_scores(sentence)
    global positive_counter
    global neutral_counter
    global negative_counter
    print(detection)
    if detection['compound'] >= 0.05:
        print("Positive Review")
        positive_counter += 1
        return 0
    elif detection['compound'] <= - 0.05:
        print("Negative Review")
        negative_counter += 1
        return 2
    else:
        print("Neutral Review")
        neutral_counter += 1
        return 1


f = open('review.txt', encoding='utf-8')
count = 0
wb = Workbook()
sheet1 = wb.add_sheet('Sentiment Categorisation')
sheet1.write(0, 0, 'Positive Sentiment')
sheet1.write(0, 1, 'Neutral Sentiment')
sheet1.write(0, 2, 'Negative Sentiment')
sheet1.write(0, 3, 'Processed Reviews')


count = 1
while True:
    line = f.readline()
    if not line:
        break
    # convert all characters to lower-case
    lower_case = line.lower()
    # remove punctuation character
    preprocessed_text = punctuation_removal(lower_case)
    # split sentence into words
    token_words = word_tokenize(preprocessed_text, "english")
    # removing stopwords from tokenized words
    remove_stopwords = []
    for word in token_words:
        if word not in stopwords.words('english'):
            remove_stopwords.append(word)
    # removing punctuations from stopwords
    final_string = converting_list_to_string(remove_stopwords)
    # write to excel sheet
    sheet1.write(count, 3, final_string)
    print(final_string)
    old_positive_counter = positive_counter
    old_neutral_counter = neutral_counter
    old_negative_counter = negative_counter
    sentiment_detector(final_string)
    if positive_counter > old_positive_counter:
        sheet1.write(positive_counter, 0, line)
    elif neutral_counter > old_neutral_counter:
        sheet1.write(neutral_counter, 1, line)
    else:
        sheet1.write(negative_counter, 2, line)
    count = count+1


print("Overall Performance")
print("Positive Reviews:" + " " + str(positive_counter))
print("Negative Reviews:" + " " + str(negative_counter))
print("Neutral Reviews:" + " " + str(neutral_counter))


plot.style.use('ggplot')
x_axis = ['Positive Reviews', 'Neutral Reviews', 'Negative Reviews']
y_axis = [positive_counter, neutral_counter, negative_counter]
plot.xlabel('Sentiment type')
plot.ylabel('Count')
plot.title('Overall Sentimental Analysis of Dining at Yomenya Goemon')
plot.bar(x_axis, y_axis)
plot.savefig('sentiment_analysis.jpg')
plot.show()

wb.save('sentiment_Categorisation1.xls')
f.close()
