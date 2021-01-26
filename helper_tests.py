import json
from helper import (username_validator, match_page_info_with_url, questions_asked)

"""In this file I have tested some of my helper functions I have created to work with the routes.
They helped me design the functions in a TDD way. The majority of autmated testing for this project can
be found in test.py"""


riddle_json = 'data/riddle_data.json'
score_data = 'data/test_scoreboard.txt'

def test_are_equal(actual, expected):
    assert actual == expected, "Expected {0}, got {1}".format(expected, actual)

# Testing username validator to see if it gives the correct response when a username is entered.
test_are_equal(username_validator(""), False) 
test_are_equal(username_validator("po"), False)
test_are_equal(username_validator("pop"), None)
test_are_equal(username_validator("pop3"), None)
test_are_equal(username_validator("pop3 1"), False)
test_are_equal(username_validator("pop3 10"), False)
test_are_equal(username_validator("123456789012"), False)
test_are_equal(username_validator("1234567890123"), False)
                
# testing that the correct riddle is loaded depending on what the session['url'] currently is.
test_are_equal(match_page_info_with_url(riddle_json, 0), {})
test_are_equal(match_page_info_with_url(riddle_json, 1), {
        "riddle"       : "This thing all things devours: Birds, beasts, trees, flowers; Gnaws iron, bites steel; Grinds hard stones to meal; Slays king, ruins town, And beats high mountain down",
        "answer"       : "Time",
        "url"          : "1",
        "image_source" : "static/img/riddle-1.png",
        "original_source": "http://img.playbuzz.com/image/upload/f_auto,fl_lossy,q_auto/cdn/79003510-1e28-4caa-8067-0f850a1b30bb/20b6a5af-2be2-4592-81b1-0b27045fa05c.jpg"
        
    })
test_are_equal(match_page_info_with_url(riddle_json, 7), {
        "riddle"       : "Thirty white horses on a red hill, First they champ, Then they stamp, Then they stand still. ",
        "answer"       : "Teeth",
        "url"          : "7",
        "image_source" : "static/img/riddle-7.png",
        "original_source": "http://images.mocpages.com/user_images/47094/1369141220m_SPLASH.jpg"
    })        


#This test checks to see if the total (the amount of questions asked) is correct depending upon session["url"].)
test_are_equal(questions_asked(1), "0")
test_are_equal(questions_asked(2), "1")
test_are_equal(questions_asked("2"), "1")
test_are_equal(questions_asked(11), "10")

# Testing the function that will delver the correct message at the end dependant upon the user's score.
def get_message(score):
    message = ""
    if score < 3:
        message = "A terrible score"
    elif score < 6:
        message = "A mediocre score"
    elif score < 8: 
        message = "Very average"
    elif score < 10:
        message = "Close... but no cigar"
    else:
        message = "You have mad Google skills"
        
    return message
        
test_are_equal(get_message(0), "A terrible score") 
test_are_equal(get_message(5), "A mediocre score")
test_are_equal(get_message(6), "Very average")
test_are_equal(get_message(8), "Close... but no cigar")
test_are_equal(get_message(10), "You have mad Google skills")


print("all tests passed")       
        
       
    