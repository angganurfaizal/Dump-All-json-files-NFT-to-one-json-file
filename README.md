# ETL on Large JSON files

Imagine you are dealing with a folder containing JSON files this big:
<div align="center">
<img src="https://drive.google.com/uc?export=view&id=1_5CXEP0_2ghFzIfHPalBkoY8E9DHV7rR">
</div><br />
Keeping the such format and processing those in Python, you will be likely to have this kind of error:
<div align="center">
<img src="https://drive.google.com/uc?export=view&id=19rk23uzdyxSXmkrGQC0uz7VLQuYZMJul">
</div><br />
Meaning you have run out of memory in your RAM for your code to execute.

A way to store json files into a much smaller size is by putting them into a single json file containing multiple dictionaries.
In this project you will see how to wrap many dictionaries from json files into a json file and how much size reduced from this process.

## Extract
Extracting the desired output from JSON folder by using `os.walk`.

## Transform
`genres` and `spoken_languages` field need to be transformed from list of dictionaries into the names.

## Load
Storing cleaned dictionaries into a list then use `json.dump` to load them into a single json file.

## Result
The transformation yielded a 150 MB json file with only 1 file passed due to incorrect format.
This process freed up 67% of your memory without no significant data missing and of course no `Memory Error` when processing data.
In this project I also put sample files for you to try on.


## Running the Program using Sample Folder
1. `git clone` this repository to your desired directory.
    ```
    git clone https://github.com/eka-pramudita/academi-self-learning-1
    ```
2. Change the path into `path = 'sample_movie'`. You can also specify your json file by setting `out_file = open("your_filename.json", "w")`
3. Run the program using this command in cmd.
    ```
    python main.py
    ```
