import txt_analyser

def main():
    """
    This code utilizes the class txt_analyser to read a .txt file and to
    Display every word present in the file, in order of occurrence. From
    The most used word to the least used word.
    """
    txt = txt_analyser.TxtAnalyser("theTXT.txt")
    my_dict = txt.count_words()
    print(my_dict)
    txt.txtClose()


if __name__ == "__main__":
    main()