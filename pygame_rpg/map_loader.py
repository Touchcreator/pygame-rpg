# converts the text files into lists

class MapLoader():

    @staticmethod
    def load(map_path):
        with open(map_path, "r") as m:
            
            map_file_raw = m.read()

            lines = map_file_raw.splitlines()

            lines = [l.strip() for l in lines]

            lines = [l.split(" ") for l in lines]

            return lines