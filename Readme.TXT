As I have completed the task in windows operating system so the setup guide is for windows OS.

1- Install Anaconda/miniconda (It is both package manager and environment manager) which is recommended for windows OS to avoid dependencies issues. And open conda prompt

2- Create a virtual environment and install all the packages using requirement.txt file using command 
	conda create --name <env> --file requirements.txt
3- Activate environment(if not already activated) using command (For windows)
	conda activate <env>
4- enter into my_project folder
	cd my_project
5- Enter into imdb_scrape folder
	cd imdb_scrape
6-To crawl the movies from imdb and store them into csv file run the command
	scrapy crawl imdb -o ../imdb_movies.csv
Now after the scrapper has finished running all the movies will be stored in imdb_movies.csv file that will be located in my_project folder.Gross USA or Budget  for movies not having these field will be Zero.

7-Now for data analysis go back to my_project folder using command
	cd ..
8- run the script data_analysis.py 
	python data_analysis.py
It will firstly show the graph illustrating relation between total number of ratings and rating score and after closing the graph it will show the graph illustrating relation between Budget and rating score. Average earning of each genre will also be displayed on conda prompt.