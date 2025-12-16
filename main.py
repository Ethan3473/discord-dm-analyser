import data_processing
import json

def main():
    data = data_processing.load_json("finn_dms.json")
    processed_data = data_processing.extract_processing_info(data)
    print("Processing complete.")

    word_counts = data_processing.count_words(processed_data)
    json.dump(word_counts, open('dms.json', 'w'), indent=4)

    
if __name__ == "__main__":
    main()

