''' Author:Polina Soshnin
    Date: Oct 14, 2015

    Problem 1: Given a board id, a latitude and longitude coordinates, 
    find the closest Place Pin on the board to the coordinates

    Problem 2: Given a board id and a number N, find the top N words that a 
    board has in its Pins’ descriptions. Return a set consisting of tuples of the word in lowercase 
    and its count.
'''

import requests
import json
from geopy.distance import vincenty

BASE_URL = "https://api.pinterest.com/v1/boards/"
access_token = 'ATZFq-Di1KDXCqrTWFS65KrAbG3RFA05CqF-HyBCjrj4nIABaQAAAAA'
board_id = '526991662585809763'

#if pin exists, return pin id
#if no pin exists, return none
def get_closest_place_pin(board_id, latitude, longitude):
	url = BASE_URL + str(board_id) + '/pins/?access_token='+ ACCESS_TOKEN + '&fields=metadata'
	response = requests.get(url)

	if response.status_code != 200:
		return None

	json_data = response.json()

	results = {}
	location1 = (latitude, longitude)

	for pin in json_data['data']:

		if 'place' in pin['metadata']:
			location2 = (pin['metadata']['place']['latitude'], pin['metadata']['place']['longitude'])
			distance = vincenty(location1, location2).feet
			results[pin['id']] = distance

	if not results:
		return None
	else:
		return min(results, key=results.get)	

NLTK_STOPWORDS = ['all', 'just', 'being', 'over', 'both', 'through', 'yourselves', 'its', 'before', 'herself', 'had', 'should', 'to', 'only', 'under', 'ours', 'has', 'do', 'them', 'his', 'very', 'they', 'not', 'during', 'now', 'him', 'nor', 'did', 'this', 'she', 'each', 'further', 'where', 'few', 'because', 'doing', 'some', 'are', 'our', 'ourselves', 'out', 'what', 'for', 'while', 'does', 'above', 'between', 't', 'be', 'we', 'who', 'were', 'here', 'hers', 'by', 'on', 'about', 'of', 'against', 's', 'or', 'own', 'into', 'yourself', 'down', 'your', 'from', 'her', 'their', 'there', 'been', 'whom', 'too', 'themselves', 'was', 'until', 'more', 'himself', 'that', 'but', 'don', 'with', 'than', 'those', 'he', 'me', 'myself', 'these', 'up', 'will', 'below', 'can', 'theirs', 'my', 'and', 'then', 'is', 'am', 'it', 'an', 'as', 'itself', 'at', 'have', 'in', 'any', 'if', 'again', 'no', 'when', 'same', 'how', 'other', 'which', 'you', 'after', 'most', 'such', 'why', 'a', 'off', 'i', 'yours', 'so', 'the', 'having', 'once']

def top_n_words(board_id, top_N):

    #^[a-zA-Z]+[a-zA-Z'-]{2,}[a-zA-Z]+$

    return None

def main():

	#print get_closest_place_pin(526991662585809763, 37.786673888041925, -122.40033388137817)
	#print get_closest_place_pin(476255798033512034, 100, -100)

if __name__ == '__main__':
	main()



