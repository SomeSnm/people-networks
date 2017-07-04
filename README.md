# people-networks

# Parsing wikipedia

Politician Map in English Wikipedia
[Parsing Wikipedia] 


Parsing Wikipedia articles was a part of a Research Project of creation a Politician Map in English Wikipedia. List of articles was delivered by Marcel (who parsed DBpedia).

The main goal of the project is to create a web platform that illustrates a map (graph) of politicians and interconnections between them with applied filters as sex, nationality, etc. 

The main goal of parsing Wikipedia team is to retrieve internal links between articles about politicians from 2001 to 2016 with a month as a step. And then create a set of edge lists with the information of connected politicians (“connection” here is an outgoing link=link from one politician’s article to another’s).

Constraints and issues during the parsing Wikipedia

Memory leakage - after first attempt of running our script we realized that there is some memory leak and our script eats up 2gb of ram after parsing ~3500 articles. We did some code profiling and determined that the problem was in one of the external libraries. To work around this problem we rewrote our code to parse our article list in chunks of 1000 articles and called it from bash script in a loop.
Python libraries – some of the libraries were responsible for the memory leakage described above (but we didn’t find out which one)
Time – all parsing took 4 days via virtual servers


Process

We created 

“Politician_data_tracker.csv”- for a list of politicians (wiki address and ID) same as a list from DBpedia

“parsed_data.csv” - for a list of politicians after it’s parsed. So the code won’t parse parsed data again. 

“profile-data” folder – to store final deliverables


Except standard python libraries we used such libraries as mwclient, wikitextparser and pickle.

1. With mwclient we started retrieving of revisions of articles metadata (Revision ID and Timestamp).
2. Then we filtered retrieved data to leave one Revision per month. And retrieved wikitext of given revisions.
3. Then with wikitextparser we parsed wikitext and extracted internal Wikipedia links.
4. With python internal library called pickle we stored extracted links with info about month and year as python dictionaries in the “profile-data” folder and added new entries into files “Politician_data_tracker.csv” and “parsed_data.csv”. Note: files “Politician_data_tracker.csv” and “parsed_data.csv” were dynamically updating during the parsing.
5. Separate script was used to create edge lists

----------------------------------------------------------------------------------------------------------------------------
