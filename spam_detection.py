import os
from collections import Counter
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split as tts
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

def make_dict():
    direc = "email/"
    files = os.listdir(direc)    
    emails = [direc + email for email in files]   
    words = []
    c = len(emails)

    for email in emails:
        f = open(email, encoding="utf8", errors='ignore')
#         print(email)
        blob = f.read()
        words += blob.split(" ")
        print(c)
        c -= 1
        
    for i in range(len(words)):
        if not words[i].isalpha():
            words[i] = ""
        
    dictionary = Counter(words)
    del dictionary[""]
    return(dictionary) ##this will we returned if we make a def

def make_dataset(dictionary):
    direc = "email/"
    files = os.listdir(direc)
    
    emails = [direc + email for email in files]
    
    words = []
    c = len(emails)
    feature_set = []
    labels = []
    for email in emails:
        data = []
        f = open(email, encoding="utf8", errors='ignore')
        words = f.read().split(' ')
#         print( words.count(0))
        for entry in dictionary:
            data.append(words.count(entry[0]))
        feature_set.append(data)
        if "ham" in email:
            labels.append(0)
        if "spam" in email:
            labels.append(1)
        print(c)
        c -= 1
    return(feature_set, labels)



x_train, x_test, y_train, y_test = tts(features, labels, test_size = 0.2)

clf = MultinomialNB()
clf.fit(x_train, y_train)
preds = clf.predict(x_test)
print(classification_report(preds, y_test))
print(confusion_matrix(preds, y_test))
print(accuracy_score(preds, y_test))

# d = make_dict()
while True:
    inp = input(">")
    if inp == 'exit':
        break
    features = []
    for word in d :
        features.append(inp.count(word[0]))
    res = clf.predict([features])
    print(res)
    print(['Not spam', 'spam'][res[0]])



