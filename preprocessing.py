import collections
import csv
import numpy as np
import operator


def preprocess(file_path):
    data = []
    null_data = []
    not_null_data = []

    ### open file, read lines ###
    with open(file_path, 'rt') as data_file:
        reader = csv.reader(data_file)
        for line in reader:
            data.append(line)

    ### separate null and not null records ###
    for record in data:
        j = 0
        for attribute in record:
            if('null' in record):
                null_data.append(record)
                break

            elif(j == len(record) - 1):
                not_null_data.append(record)
                break
            j += 1
    not_null_data.remove(not_null_data[0])

    ### stats section ###
    no = []
    yes = []

    for j in range(0, len(not_null_data)):
        recommend = len(not_null_data[0]) - 1

        if(int(not_null_data[j][recommend]) == 0):
            no.append(not_null_data[j])
        else:
            yes.append(not_null_data[j])

    no_t = np.transpose(no).tolist()
    yes_t = np.transpose(yes).tolist()

    styles = []
    prices = []
    ratings = []
    sizes = []
    seasons = []
    neck_lines = []
    sleeve_lengths = []
    waistlines = []
    materials = []
    pattern_types = []

    for j in range(0, len(no_t)):
        if(j == 0):
            styles.append(no_t[j])
        elif(j == 1):
            prices.append(no_t[j])
        elif(j == 2):
            ratings.append(no_t[j])
        elif(j == 3):
            sizes.append(no_t[j])
        elif(j == 4):
            seasons.append(no_t[j])
        elif(j == 5):
            neck_lines.append(no_t[j])
        elif(j == 6):
            sleeve_lengths.append(no_t[j])
        elif(j == 7):
            waistlines.append(no_t[j])
        elif(j == 8):
            materials.append(no_t[j])
        elif(j == 9):
            pattern_types.append(no_t[j])

    for j in range(0, len(yes_t)):
        if(j == 0):
            styles.append(yes_t[j])
        elif(j == 1):
            prices.append(yes_t[j])
        elif(j == 2):
            ratings.append(yes_t[j])
        elif(j == 3):
            sizes.append(yes_t[j])
        elif(j == 4):
            seasons.append(yes_t[j])
        elif(j == 5):
            neck_lines.append(yes_t[j])
        elif(j == 6):
            sleeve_lengths.append(yes_t[j])
        elif(j == 7):
            waistlines.append(yes_t[j])
        elif(j == 8):
            materials.append(yes_t[j])
        elif(j == 9):
            pattern_types.append(yes_t[j])

    no_stats = []
    no_styles_stats = collections.Counter(styles[0])
    no_prices_stats = collections.Counter(prices[0])
    no_ratings_stats = collections.Counter(ratings[0])
    no_sizes_stats = collections.Counter(sizes[0])
    no_seasons_stats = collections.Counter(seasons[0])
    no_neck_lines_stats = collections.Counter(neck_lines[0])
    no_sleeve_lengths_stats = collections.Counter(sleeve_lengths[0])
    no_waistlines_stats = collections.Counter(waistlines[0])
    no_materials_stats = collections.Counter(materials[0])
    no_pattern_types_stats = collections.Counter(pattern_types[0])
    no_stats = [no_styles_stats, no_prices_stats, no_ratings_stats, no_sizes_stats, no_seasons_stats, no_neck_lines_stats,
                no_sleeve_lengths_stats, no_waistlines_stats, no_materials_stats, no_pattern_types_stats, no_stats]

    yes_stats = []
    yes_styles_stats = collections.Counter(styles[1])
    yes_prices_stats = collections.Counter(prices[1])
    yes_ratings_stats = collections.Counter(ratings[1])
    yes_sizes_stats = collections.Counter(sizes[1])
    yes_seasons_stats = collections.Counter(seasons[1])
    yes_neck_lines_stats = collections.Counter(neck_lines[1])
    yes_sleeve_lengths_stats = collections.Counter(sleeve_lengths[1])
    yes_waistlines_stats = collections.Counter(waistlines[1])
    yes_materials_stats = collections.Counter(materials[1])
    yes_pattern_types_stats = collections.Counter(pattern_types[1])
    yes_stats = [yes_styles_stats, yes_prices_stats, yes_ratings_stats, yes_sizes_stats, yes_seasons_stats, yes_neck_lines_stats,
                 yes_sleeve_lengths_stats, yes_waistlines_stats, yes_materials_stats, yes_pattern_types_stats, yes_stats]

    ### null value correction ###
    for record in null_data:
        i = 0
        recommend = len(null_data[0]) - 1
        for a in record:
            null_index = []
            j = i + 1
            while(j < len(record)):
                if(record[j].lower() == 'null'):
                    null_index.append(j)
                j += 1
                for n in null_index:
                    if(int(null_data[i][recommend]) == 0):
                        temp = list(no_stats[n].keys())
                        
                        try:
                            r = np.random.randint(0, int(len(temp)/5))
                        
                        except(ValueError):
                            r = np.random.randint(0, int(len(temp)/5) + 1)
                        record[n] = temp[r]
                    elif(int(null_data[i][recommend]) == 1):
                        temp = list(yes_stats[n].keys())

                        try:
                            r = np.random.randint(0, int(len(temp)/5))
                        except(ValueError):
                            r = np.random.randint(0, int(len(temp)/5) + 1)
                        
                        record[n] = temp[r]
            i += 1

    merged_data = null_data + not_null_data

    return merged_data