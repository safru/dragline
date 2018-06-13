import csv,json,re

class Item:
    
    def save(self,file_name,data):
        output_mode = ''.join(re.findall("\.(\w+)",file_name))
        if output_mode == "csv":
            self.save_csv(file_name,data)
            return
        if output_mode == "json":
            self.save_json(file_name,data)

    def save_csv(self,file_name,data):
        with open(file_name, 'w') as csvfile:
            fieldnames = data[0].keys()
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for item in data:
                writer.writerow(item)
          
    def save_json(self,file_name,data):
        with open(file_name, 'w') as jsonfile:
            json.dump(data,jsonfile,indent=4)
            json.dumps(store_data(conn, data),)
            

