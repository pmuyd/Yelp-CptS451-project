import json

def cleanStr4SQL(s):
    return s.replace("'", "''").replace("\n", " ")

def parseCheckinData():
    print("Parsing checkins...")
    # reading the JSON file
    with open('.//yelp_checkin.JSON', 'r') as f:  # Assumes that the data files are available in the current directory. If not, you should set the path for the yelp data files.
        outfile = open('yelp_checkin.txt', 'w')
        line = f.readline()
        count_line = 0
        # read each JSON object and extract data
        while line:
            data = json.loads(line)
            for dayofweek, time in data['time'].items():
                checkin_str = f'"{dayofweek}": {{'
                for hour, count in time.items():
                    checkin_str += f'"{hour}": {count}, '
                checkin_str = checkin_str[:-2]  # Remove the extra comma and space at the end
                checkin_str += '}'
                outfile.write(checkin_str + "\n")
            line = f.readline()
            count_line += 1
        print(count_line)
    outfile.close()
    f.close()

parseCheckinData()