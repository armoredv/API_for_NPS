# API_for_NPS
A repo containing code for calculating NPS(net promoter score) for client
Steps to run the api
1. Download the api.py file from the repository.
2. Run the file by using the following command in windows cmd or linux terminal
    python api.py
3. Type following query for getting the input Json file that is used in the API
   http://localhost:5000/
4. Type following query for getting the various distribution of Promoters, Passives and Detractors of each day in Json file
   http://localhost:5000/getnps?startDate=2020-10-15&endDate=2020-10-17
5. Type following query for getting the nps score for each day in Json file
   http://localhost:5000/get_nps_score?startDate=2020-10-15&endDate=2020-10-17

Remember : The above api contains a very small set of input data i.e from 15-10-2020 to 18-10-2020 and thus startDate and endDate in the query should lie between this range only  
   
