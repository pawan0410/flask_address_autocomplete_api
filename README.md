# flask_address_autocomplete_api

Autocomplete Rest api to search addresses:

  1) A flask application which serves a autocomplete JSON REST API

  2) Create the addresses.json file and place it in the static folder (provided)

  3) Application should be provided with an initial list of addresses file

  4) The API should accept one or more characters of input as 'q' parameter for the
     API '/search' and return with autocomplete suggestions for matched address names
     (maximum 10 results).


Assumption:
1. We are dealing with flat files, not with databases.
2. Data is small

Suggestions (when data grows):

1.If the addresses file grow,we must switch to MongoDB or other NoSQL db's
2. If the data is large, we need an optimised data structure for the search query.(Trees)
3. We can prioritise our search when databases are in scene.







