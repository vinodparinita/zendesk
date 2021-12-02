import json
import os

class jsonOps(object):
    def __init__(self, config_json_file):
        try:
            self.__dict__ = self.load_json(config_json_file)
        except os.error as oe:
            raise oe

    def load_json(self, config_json_file):
        with open(config_json_file, 'r') as jsonfile:
            config_json = json.load(jsonfile)
            #print("✅ Config JSON Read successful ✅")
        jsonfile.close()
        return config_json

    def print_json(self):
        print(self.__dict__)

    def __getvalue__(self, key):
        return self.__dict__.get(key)

# top-level function
if __name__ == "__main__":
    sys.exit(main())
