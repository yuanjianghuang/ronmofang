import jieba
import jieba.analyse

def main():
    with open( 'sampletext.txt', 'rb') as f:
        text = f.read()
    print ("jieba segmentation results: ")
    print (' '.join(jieba.cut(text)))
    # extract key words
    print ("jieba extract key words: ")
    # topK returns the topK words with highest TF/IDF
    print (','.join(jieba.analyse.extract_tags(text, topK=10)))

if __name__ == "__main__":
    main()
