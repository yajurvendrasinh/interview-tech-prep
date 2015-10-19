### Problem #1

Find top words using Pinterest APIs and Python.

####Objective

Given a board id and a number N, find the top N words that a board has in its Pins’ descriptions. Return a set consisting of tuples of the word in lowercase and its count.

####Details

Every Pinner on Pinterest has their own style and set of interests. One way to get a feel for a Pinner’s personality is to look at the descriptions of their Pins!

A word is defined as any string that:

- is a minimum of 2 letters.
- starts and ends with an alphabetic ASCII letter.
- only contains ASCII characters that are the alphabet, ', or -.
- is not in nltk's stopwords (provided for your convenience as NLTK_STOPWORDS in the source).

####Requirements

Be sure your answers are returned in a set().

If there’s a tie that causes you to exceed N, return all words within the tie.

You should ignore all URLs, and words within URLs. A URL can start with http://, https://, or www.
Words containing dashes (—), curly apostrophes (’), and other characters similar in appearance to the straight apostrophe (') and hyphen (-) are invalid words and should be ignored.

####Examples

https://www.pinterest.com/flobeanz/womenengpinterest/

```
top_n_words(515310451052222064, 4)
{
   (u"diversity", 8),
   (u"tech", 7),
   (u"industry", 4),
   (u"make", 3),
   (u"need", 3),
   (u"example", 3),
   (u"work", 3),
   (u"woman", 3),
   (u"black", 3),
   (u"data", 3),
   (u"sexism", 3),
   (u"sexist", 3)
}
```

https://www.pinterest.com/ouidad/empowering-women/

```
top_n_words(266627309128262271, 6)
{
   (u"women", 69),
   (u"quotes", 63),
   (u"feminist", 20),
   (u"woman", 19),
   (u"quote", 17),
   (u"best", 14),
   (u"empowering", 14)
}
```

####Take Note

- If you do not have a Pinterest API access token, please go to the following URL to generate one: https://developers.pinterest.com/tools/access_token/.
- By default, our API only returns up to 25 pins. Take a look at https://developers.pinterest.com/docs/api/overview/ to learn how to get paginated responses.
- To see what a board’s ID is, view the source of the page and search for board_id.
Save your code in ~/Lytmus/question_2/answer.py.

###Problem #2

Find the closest Place Pin.

####Objective

Given a board id, a latitude and longitude coordinates, find the closest Place Pin on the board to the coordinates.

####Details

You’re at Grace Hopper, looking at the Pinterest board for all the cool places near the conference center. You want to find the closest place to you, using the Pinterest API.

A "Place Pin" is a Pin that has geolocation data such as latitude and longitude.

####Requirements

- This extra Pin information can be obtained by explicitly requesting the metadata field (&fields=metadata), and then obtaining the latitude and longitude from the place data section.
- If Pin exists, return just the pin id.
- If no Pin exists, return None.

####Examples

Board: https://www.pinterest.com/ivmi15/brunch-in-san-francisco/

```
> get_closest_place_pin(526991662585809763, 37.786673888041925, -122.40033388137817)
"526991593875023832"
```

Board: https://www.pinterest.com/Pinclusion/negotiation-speak-up/

```
> get_closest_place_pin(476255798033512034, 100, -100)
None
```

GET /v1/boards/[board_spec:board]/

```
E.g. https://api.pinterest.com/v1/boards/ivmi15/brunch-in-san-francisco/?access_token=$ACCESS_TOKEN
{
    data:
    {
        "url": "https://www.pinterest.com/ivmi15/brunch-in-san-francisco/",
        "id": "526991662585809763",
        "name": "Brunch in San Francisco"
    }
}
```

####Take Note

- If you do not have a Pinterest API access token, please go to the following URL to generate one: https://developers.pinterest.com/tools/access_token/
- By default, our API only returns up to 25 pins. Take a look at https://developers.pinterest.com/docs/api/overview/ to learn how to get paginated responses.
- To obtain a board's id, use the following developer API endpoint with a valid access token, and retrieve the id from the response: GET /v1/boards/[board_spec:board]/
- Alternatively, you can use the API explorer: https://developers.pinterest.com/tools/api-explorer/
- Save your code in ~/Lytmus/question_1/answer.py.