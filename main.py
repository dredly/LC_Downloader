import os
from dotenv import load_dotenv
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

def main():
	load_dotenv()
	browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
	starting_url = "https://learningcentral.cf.ac.uk/ultra/courses/_406224_1/cl/outline"
	browser.get(starting_url)

if __name__=="__main__":
	main()