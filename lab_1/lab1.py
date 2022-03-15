def get_file_text(file_name):
    try:
        file = open("text.txt", "r")
        try:
            file_text = file.read()
        except Exception as e:
            print(e)
        finally:
            file.close()
            return file_text
    except Exception as ex:
        print(ex)


def get_average_word_count(text):
    text = text.lower()
    punctuation_marks = list("()-:;\",")
    end_of_sentence_signs = list("?!.")

    for char in punctuation_marks:
        text = text.replace(char, "")

    word_count = len(text.split())

    sentence_count = 0
    for char in text:
        if char in end_of_sentence_signs:
            sentence_count += 1

    average_word_count = word_count / sentence_count

    return average_word_count


def get_words_dict(text):
    text = text.lower()
    punctuation_marks = list("()-:;\",?!.")

    for char in punctuation_marks:
        text = text.replace(char, "")

    words_list = text.split()

    words_dict = dict()
    for word in words_list:
        if word in words_dict:
            words_dict[word] += 1
        else:
            words_dict[word] = 1

    return words_dict


def get_median_word_count(text):
    end_of_sentence_signs = list("?!.")
    for char in end_of_sentence_signs:
        text = text.replace(char + " ", ".")

    sentence_list = text.split(".")
    sentence_list.remove("")

    words_count_list = list()
    sentence_dict = dict()
    for sentence in sentence_list:
        sentence_dict[sentence] = 1
        for char in sentence:
            if char == " ":
                sentence_dict[sentence] += 1
        words_count_list.append(sentence_dict[sentence])

    words_count_list.sort()
    pointer = len(words_count_list) / 2
    if len(words_count_list) % 2 == 0:
        pointer = int(pointer)
        return (words_count_list[pointer - 1] + words_count_list[pointer]) / 2
    else:
        return words_count_list[int(pointer)]


def get_top_ngrams(text, n, k):
    words_dict = get_words_dict(text)
    filtered_dict = dict()
    for word in words_dict:
        if len(word) == n:
            filtered_dict[word] = words_dict[word]

    quantities_list = list(filtered_dict.values())
    quantities_list.sort()
    quantities_list.reverse()
    top_list = quantities_list[:k]
    top_dict = dict()

    for times in top_list:
        for word in filtered_dict:
            if filtered_dict[word] == times and word not in top_dict.keys():
                top_dict[word] = times
                break

    return top_dict


def print_words_dict(words_dict):
    for word in words_dict:
        print(f"{word}: {words_dict[word]} times")


def main():
    text = get_file_text("text.txt")

    if text is None:
        print("File not found or file is empty")
        return
    n = 10
    k = 4
    print("Choose an option:\n1) Show top-4 10-grams\n2) Enter your values")
    choice = input(">> ")
    if int(choice) == 2:
        n = int(input("n = "))
        k = int(input("k = "))

    print(f"\nTop-{k} {n}-grams:")
    print_words_dict(get_top_ngrams(text, n, k))
    print("\nWords dictionary:")
    print_words_dict(get_words_dict(text))
    print(f"\nAverage word count: {get_average_word_count(text)}")
    print(f"Median word count: {get_median_word_count(text)}")


if __name__ == "__main__":
    main()
