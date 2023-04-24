
def remove_similar_sentences(sentences):
    new_sentences = []
    for i in range(len(sentences)):
        is_duplicate = False
        for j in range(i + 1, len(sentences)):
            # Convert sentences to lower case and tokenize into words
            sent1 = set(sentences[i].lower().split())
            sent2 = set(sentences[j].lower().split())
            # Compute the Jaccard similarity between the two sets of words
            similarity = len(sent1.intersection(sent2)) / float(len(sent1.union(sent2)))
            if similarity > 0.8:
                is_duplicate = True
                break
        if not is_duplicate:
            new_sentences.append(sentences[i])
    return new_sentences


def find_and_remove_duplications():
    puns = []
    with open("./pun_repository.txt", "r") as f:
        puns = f.readlines()
        puns = [
            pun.strip().replace("’", "'") 
            for pun in puns
        ]
        puns = list(set(puns))
        puns = remove_similar_sentences(puns)
        
    
    with open("./pun_repository.txt", "w") as f:
        f.write("\n".join(puns))

find_and_remove_duplications()
