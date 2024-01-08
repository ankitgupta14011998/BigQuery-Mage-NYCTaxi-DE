# BigQuery-Mage-NYCTaxi-DE

### Data Model Diagram
![image](https://github.com/ankitgupta14011998/BigQuery-Mage-NYCTaxi-DE/assets/32798626/0ce0616a-a134-40a0-b244-aaa697f33f76)

### Project architecture

![image](https://github.com/ankitgupta14011998/BigQuery-Mage-NYCTaxi-DE/assets/32798626/b01971d2-a86f-42f0-912c-cc0baf058f7a)

### Snapshot from Mage UI

![image](https://github.com/ankitgupta14011998/BigQuery-Mage-NYCTaxi-DE/assets/32798626/cdf66eef-fa4a-43d7-b891-78891ce7c858)


#### Steps

1. Data set from NYC taxi https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page
2. Create date model on draw.io. Create Facts and Dimension tables and define relationship between them.
3. Filter the data using jupyter notebook. Implement the data model diagram using the python code and test it in notebook.
4. Upload the dataset to 'Google Cloud Storage'. Create new VM and SSH into it.
   Run following command in linux terminal
   a. sudo apt-get update -y
   b. sudo apt-get install python3-distutils
   c. sudo apt-get install wget
   d. wget https://bootstrap.pypa.io/get-pip.py
   e. sudo python2 get-pip.py
   f. pip3 install mage-ai
   g. pip3 install google-cloud
   h. pip3 install google-cloud-bigquery
   i. pip3 install pandas
5. run command mage start [project-name] to start mage project.
6. Create Data_loader,Data transformer and Data_Exporter objects and create a pipeline. The pipeline will load any new dataset available from Google Cloud Storage, apply transformation and create required tools in Google BigQuery Analytics Engine.
7. We can perform various analytical operations on these datasets.
8. We can visualize the dataset using interactive dashboard on Google LookerStudio.


