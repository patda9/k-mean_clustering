from preprocessing import *

def data_map(data):
    mapped_data = data
    
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
    recommendation = []

    mapped_data_t = np.transpose(mapped_data).tolist()
    for i in range(0, len(mapped_data_t)):
        if(i == 0):
            styles = (mapped_data_t[i])
        elif(i == 1):
            prices = (mapped_data_t[i])
        elif(i == 2):
            ratings = (mapped_data_t[i])
        elif(i == 3):
            sizes = (mapped_data_t[i])
        elif(i == 4):
            seasons = (mapped_data_t[i])
        elif(i == 5):
            neck_lines = (mapped_data_t[i])
        elif(i == 6):
            sleeve_lengths = (mapped_data_t[i])
        elif(i == 7):
            waistlines = (mapped_data_t[i])
        elif(i == 8):
            materials = (mapped_data_t[i])
        elif(i == 9):
            pattern_types = (mapped_data_t[i])
        elif(i == 10):
            recommendation = (mapped_data_t[i])
        
    styles_stats = collections.Counter(styles)
    prices_stats = collections.Counter(prices)
    sizes_stats = collections.Counter(sizes)
    seasons_stats = collections.Counter(seasons)
    neck_lines_stats = collections.Counter(neck_lines)
    sleeve_lengths_stats = collections.Counter(sleeve_lengths)
    waistlines_stats = collections.Counter(waistlines)
    materials_stats = collections.Counter(materials)
    pattern_types_stats = collections.Counter(pattern_types)

    i = 0
    for record in data:
        for j in range(0, len(record)):
            if(j == 0):
                if(data[i][j] in styles_stats):
                    mapped_data[i][j] = float(styles_stats[data[i][j]])
            elif(j == 1):
                if(data[i][j] in prices_stats):
                    mapped_data[i][j] = float(prices_stats[data[i][j]])
            elif(j == 2):
                mapped_data[i][j] = float(ratings[i])
            elif(j == 3):
                if(data[i][j] in sizes_stats):
                    mapped_data[i][j] = float(sizes_stats[data[i][j]])
            elif(j == 4):
                if(data[i][j] in seasons_stats):
                    mapped_data[i][j] = float(seasons_stats[data[i][j]])
            elif(j == 5):
                if(data[i][j] in neck_lines_stats):
                    mapped_data[i][j] = float(neck_lines_stats[data[i][j]])
            elif(j == 6):
                if(data[i][j] in sleeve_lengths_stats):
                    mapped_data[i][j] = float(sleeve_lengths_stats[data[i][j]])
            elif(j == 7):
                if(data[i][j] in waistlines_stats):
                    mapped_data[i][j] = float(waistlines_stats[data[i][j]])
            elif(j == 8):
                if(data[i][j] in materials_stats):
                    mapped_data[i][j] = float(materials_stats[data[i][j]])
            elif(j == 9):
                if(data[i][j] in pattern_types_stats):
                    mapped_data[i][j] = float(pattern_types_stats[data[i][j]])
            elif(j == 10):
                mapped_data[i][j] = float(recommendation[i])
        i += 1
    
    recommendation = np.asarray(recommendation, dtype = np.int)
    recommendation = np.reshape(recommendation, (len(recommendation), 1))
    return mapped_data[0:len(mapped_data)]