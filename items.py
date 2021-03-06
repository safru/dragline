import csv,json,re
from pprint import pprint

class Item:
    
    def save(self,file_name,data):
        output_mode = ''.join(re.findall("\.(\w+)",file_name))
        if output_mode == "csv":
            self.save_csv(file_name,data)
            return
        if output_mode == "json":
            self.save_json(file_name,data)

        if output_mode == "txt":
            self.save_txt(file_name,data)

    def save_csv(self,file_name,data):
        with open(file_name, 'w') as csvfile:
            fieldnames = data[0].keys()
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for item in data:
                writer.writerow(item)
                pprint(item)
          
    def save_json(self,file_name,data):
        with open(file_name, 'w') as jsonfile:
            json.dump(data,jsonfile,indent=4)
            # json.dumps(store_data(conn, data),)
            pprint(data)


    def save_txt(self,file_name,data):
        with open(file_name, 'a') as txtfile:
            txtfile.write(data)
            pprint(data)
            
            

