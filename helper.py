import os
import json
from flask import Flask, render_template, request, redirect, flash, url_for, session, jsonify
from datetime import datetime

# Function will load correct riddle and picture for each page 
def match_page_info_with_url(json_file, number):
    riddle = {}
    with open(json_file, "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == str(number):
                riddle = obj
    return riddle
    
#Username validator to ensure all usernames are between 3 and 10 characters and contain no spaces
def username_validator(username):
    if len(username) < 3 or len(username) > 10:
        return False
    else:
        for char in username:
            if char == ' ':
                return False
 
             
def write_to_file(filename, data):
    with open(filename, "a") as file:
        file.writelines(data)
        
#Add to scoreboard.txt  
def add_to_scoreboard(username, score, scoreboard):
    write_to_file(scoreboard, "{0} {1} {2}\n".format(
            score,
            username,
            datetime.now().strftime("%d/%m/%y")))

#Order the scoreboard based on score
def ordered_scoreboard(scoreboard):
    ordered = []
    ordered = sorted(scoreboard, key= (lambda line: int(line.lstrip().split(' ')[0])))
    return ordered

#Split each entry into score, username and date to be fill the table in leaderboard.html
def score_username_date(scores):
    details=[]
    for score in scores[::-1]:
        details.append(score.split())
        
    return details

#Display scoreboard in ordered fashion and split scores into list for indexing into tables            
def get_scoreboard_data(scoreboard):
    parse_data = []
    with open(scoreboard, 'r') as scoreboard_data:
        ordered_data = ordered_scoreboard(scoreboard_data.readlines())
        parse_data = score_username_date(ordered_data)
        return parse_data

#Set the session dictionary as new login is created
def initiate_session(user):
    session['username'] = user
    session['url'] = 1
    session['score'] = 0

#Increment the score and or current url
def correct():
    session['url'] += 1
    session['score'] += 1
    
def pass_question():
    session['url'] += 1

#Calculate number of questions asked to be displayed on page
def questions_asked():
    return session['url'] - 1