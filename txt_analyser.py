class TxtAnalyser:
    """
    Class TxtAnalyser is used to read .txt files and count how many
    times each word occurs in the file. It also organizes them
    """
    
    
    def __init__(self, file_path):
        """
        Args:
            file_path(str): full path to the .txt file including its
            name. Example: "C:\Users\Username\Downloads\my_txt.txt"
        """
        self.file_path = file_path
        self.file = open(file_path, "r+")
        self.sorted_words = dict()

    def get_file_path(self):
        """
        Returns: 
            file_path(str): path of the .txt file.
        """
        return self.file_path
    
    def count_words(self):
        """
        Reads the .txt file, saves each word in a dictionary,
        and how many times each occurred in the .txt file. And organizes
        the words in decreasing order of amount of occurrence
        Returns:
            sorted_words(dictionary): dictionary in which keys are the
            words present in the .txt file, and the values are each word
            occurrence.
        """
        for line in self.file:
           
            for word in line.split():
                
                if word in self.sorted_words.keys():
                    self.sorted_words[word] += 1
                else:
                    self.sorted_words[word] = 1

        self.sorted_words = dict(
            sorted(
                self.sorted_words.items(), key=lambda item: item[1], 
                reverse = True
            )
        )         
        
        return self.sorted_words

    def txt_close(self):
        """
        closes the opened .txt
        """
        self.file.close()