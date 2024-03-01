import requests
import json 
from utils.utils import Utils
from logger import logging
from xml.etree import ElementTree as ET

class Data_ingestion:
    def __init__(self) -> None:
        self.utils= Utils()

    def get_data(self, format:str, offset:int, limit:int):
        
        api_key = self.utils.get_property("api_key")
        url= self.utils.get_property("url")

        api_url = f"{url}?api-key={api_key}&format={format}&limit={limit}"

        response = requests.get(api_url)
        
        return response
    
    def initiate_data_ingestion(self):
        # Reading properties from yaml file
        try:
            logging.info("Data Ingestion Started")
            # format1= self.utils.get_property("format1")
            # offset1= self.utils.get_property("offset1")
            # limit1= self.utils.get_property("limit1")

            # response= self.get_data(format1, offset1, limit1)
            # # Check if the request was successful (status code 200)
            # if response.status_code == 200:
            #     logging.info("JSON format data collection started")
            #     data = response.json() 
            #     with open('artifacts/json_response.json', 'w') as response_file:
            #         json.dump(data, response_file, indent=2)
            #     print("got response json")
            # else:
            #     # Handle errors
            #     print(f"Error: {response.status_code} - {response.text}")

            # format2= self.utils.get_property("format2")
            # offset2= self.utils.get_property("offset2")
            # limit2= self.utils.get_property("limit2")

            # response= self.get_data(format2, offset2, limit2)
            # # Check if the request was successful (status code 200)
            # if response.status_code == 200:
            #     logging.info("CSV format data collection started")
            #     data = response.text 
            #     with open('artifacts/csv_response.csv', 'w') as response_file:
            #         response_file.write(data)
            #     print("got response csv")
            # else:
            #     # Handle errors
            #     print(f"Error: {response.status_code} - {response.text}")
                
            format3= self.utils.get_property("format3")
            offset3= self.utils.get_property("offset3")
            limit3= self.utils.get_property("limit3")

            response= self.get_data(format3, offset3, limit3)
            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                logging.info("XML format data collection started")
                data = ET.fromstring(response.text)
                data_tree= ET.ElementTree(data)
                data_tree.write('artifacts/xml_response.xml')
                # with open('artifacts/xml_response.xml', 'w') as response_file:
                #     response_file.write(data_tree)
                print("got response xml")
            else:
                # Handle errors
                print(f"Error: {response.status_code} - {response.text}")
            logging.info("Data Ingestion Completed")
            
        except Exception as e:
            raise e
            

if __name__=="__main__":
    obj= Data_ingestion()
    obj.initiate_data_ingestion()