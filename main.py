import json
import os.path


def main():
    fileList = []
    path = 'metadata'
    for filenames in os.walk(path):
        fileList.append(filenames)

    data_list = []

    for i in range(len(filenames[2])):
        try:
            data = json.load(open('metadata/' + filenames[2][i], encoding='utf-8'))
            data_final = dict((k, data[k]) for k in ('name', 'description', 'image', 'dna', 'edition', 'date', 'attributes', 'compiler'))
            data_list.append(data_final)
        except Exception:
            pass

    out_file = open("_metadata.json", "w")
    json.dump(data_list, out_file, indent=2)
    print(data_list)
    out_file.close()


if __name__ == '__main__':
    main()

