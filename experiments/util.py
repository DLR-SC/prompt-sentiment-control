import pandas as pd
import os

def load_file (query_path):
    """
    Loads entries from a file line by line into a list.
    
    Args:
        query_path (str): Path to the query file to be loaded.
        
    Returns:
        list: List containing each line from the file as an element.
    """
    
    entries = []
    counter = 0

    try:
        with open (query_path, "r") as file:
            for line in file:
                entries.append (line.rstrip("\n")) # remove enters before adding entry to list
                counter += 1
        return entries
    except IOError as e:
        print(F"Error loading file entries: {e}")



def save_file (text_list, output_path):
    """
    Saves model responses to a specified output file.
    
    Args:
        text_list (list): List of model responses to be saved.
        output_path (str): Path where the output file should be saved, without file extension.
            The function will handle adding the appropriate file extension.
    
    Returns:
        None: The function saves data to disk but doesn't return a value.
    
    Note:
        This function is specifically designed for saving responses generated from
        Vanilla Prompts (prompts without emotional content).
    """
    
    counter = 0
    file_path = F"{output_path}.txt"

    try:
        with open (file_path, "w") as file:
            for entry in text_list:
                full_entry = F"{entry}\n"
                file.write(str(full_entry))
                counter += 1
        print(F"{counter} list entries are saved to {file_path} successfully.")  # double check if all expected responses are saved to the file
    except IOError as e:
        print(F"Error saving list entries to {file_path}: {e}")



def save_dataframe_files (text_list, emotion_list, queries, output_path):
    """
    Saves model responses with their corresponding emotions in multiple file formats.
    
    Args:
        text_list (list): List of model responses/texts to be saved.
        emotion_list (list): List of emotions corresponding to each text in text_list.
            Must be the same length as text_list.
        output_path (str): Base path for output files without extension.
            The function will save files with .csv and .json extensions.
    
    Returns:
        None: The function saves data to disk but doesn't return a value.
    """
    
    emotion_mapping = {
        "anger": 0,
	    "disgust": 1,
	    "fear": 2,
	    "joy": 3,
	    "sadness": 4,
	    "surprise": 5,
        "neutral": 6
    }

    mapped_labels = [emotion_mapping[label] for label in emotion_list]

    df = pd.DataFrame({"query": queries, "text": text_list, "label": mapped_labels, "label_name": emotion_list})

    df.to_pickle(output_path, protocol=4)



def save_file_with_emotion (df, output_path):
    """
    Saves responses with their corresponding emotions to a text file.
    
    Args:
        df (pandas.DataFrame): DataFrame containing 'text' and 'emotion' columns.
            Expected to be the output from save_dataframe_files function.
        output_path (str): Path where the output file should be saved.
            The function will append .txt extension if not provided.
    
    Returns:
        None: The function does not return a value.
    """
    counter = 0
    file_path = F"{output_path}-with-emotions.txt"

    try:
        with open (file_path, "w") as f:
            for _, row in df.iterrows():
                counter += 1
                text = row["text"]
                label = row["label"]
                label_name = row["label_name"]

                entry = F'{text}, {label}, {label_name}\n'
                f.write(str(entry))
        print(F"{counter} list entries are saved to {file_path} successfully.")
    except IOError as e:
        print(F"Error saving DataFrame to {file_path}: {e}")

def load_dataframe (dataframe_path):
    if os.path.exists(dataframe_path): # if dataframe already exists, just load the dataframe from the path
        df = pd.read_pickle(dataframe_path)
        print(F"Loaded dataframe from {dataframe_path} successfully!")
        return df
    else:
        print(F"ERROR: no dataframe available. Please recheck the given path {dataframe_path} and try again.")