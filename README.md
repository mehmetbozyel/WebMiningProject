We brought together all the vehicle advertisements published on a sample website by web crawling. We have taken the necessary data from the web pages of the vehicle advertisements we have in the parcel. These data are the city, brand, model and price of the vehicles. After passing this data in filtering and analysis processes, a csv file was output where we give the average price of the vehicles in each city according to the brand and model. The project was developed to help vehicle sellers and buyers get an idea of price information.

Technologies used in the project:
- Python3
- beautifulsoup4 
- urllib3
- pandas

We encountered blocking during testing on some websites. These sites detected us as bots and blocked us. That's why the way it works on every website is the same. We developed the project based on the https://www.arabam.com/ website.

How It Works

First, we create the links of the pages with the listings according to the url format. We get the html of these pages by making a get request with urllib. Then we parse the html pages with beautifulsoup4 and add the link of each vehicle advertisement to the list.

With Urllib, we get the html of each post with get. We parse it with Beautifulsoup4 and add the vehicle features to the list according to the class names. We use replace to bring the features to the format we want. Then we turn our list into a dataframe with pandas and print it to the cities.csv file.

With the analyzer.py file, we take the average price of the same city, brand and model vehicles and print it to the output.csv file.

To run;
- pip3 install beautifulsoup4
- pip3 install urllib3
- python3 scraper.py
- python3 analyzer.py



