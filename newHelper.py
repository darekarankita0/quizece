class Quiz(object):
    def __init__(self, username):
        self.username = username
        self.score = 0
        self.url = 1
    
        
    def get_score(self):
        return self.score
        
    def get_url(self):
        return self.url
        
    def get_questions_asked(self):
        return str(self.url - 1)
        
    def correct_answer(self):
        self.score += 1
        self.url += 1
    
    def pass_question(self):
        self.url += 1
        

def get_final_score_message(score, url):
    message = ""
    if url > 10:
        if score < 3:
            message = "You scored " + str(score) + "/10. Terrible"
        elif score < 6:
            message = "You scored " + str(score) + "/10. Mediocre"
        elif score < 8:
            message = "You scored " + str(score) + "/10. Above average"
        elif score < 10:
            message = "You scored " + str(score) + "/10. Close... but no cigar"
        else:
            message = "You scored " + str(score) + "/10. You have mad Google skills"

    return message
        
        