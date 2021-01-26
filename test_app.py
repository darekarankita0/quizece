from app import *
import unittest
from flask import Flask, session


"""I tried running some automated tests. Below is as far as I got, I could only test the login page validation,
 the rendering of the first page of the quiz and the leaderboard page. After this I could not find a way to correctly test the "/submit_answer"
route. I have tested alot of the individual functions I wrote for the routes in test_quiz_functions.py."""

class FlaskTestCase(unittest.TestCase):
    # Test getting the login page and checking the content is correct.
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'Riddle Quiz' in response.data)
    
    # Test The login page with valid username and it is correctly redirected.    
    def test_login_valid_username(self):
        tester = app.test_client(self)
        response = tester.post('/', data=dict(username="tester"), follow_redirects = True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'tester, your score is 0 / 0' in response.data)
        self.assertTrue(b'This thing all things devours: Birds, beasts, trees, flowers; Gnaws iron, bites steel; Grinds hard stones to meal; Slays king, ruins town, And beats high mountain down' in response.data)
    
    # Test The login page with invalid username and check the response message. 
    def test_login_invalid_username(self):
        tester = app.test_client(self)
        response = tester.post('/', data=dict(username="testecdfsfv2348nn8e"), follow_redirects = True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'Username must contain between 3 and 10 characters and cannot contain any spaces' in response.data)
    
    # Test the leaderboard page loads correctly.   
    def test_leaderboard_not_logged_in(self):
        tester = app.test_client(self)
        response = tester.get('/leaderboard_no_login', follow_redirects = True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'Leaderboard' in response.data)
    # Test the skip_question route    
    def test_skip_question(self):
        tester = app.test_client(self)
        tester.post('/', data=dict(username="tester"), follow_redirects = True)
        response = tester.post('/skip_question', follow_redirects = True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'tester, your score is 0 / 1' in response.data)
    # test the response when a correct answer is given    
    def test_correct_answer(self):
        tester = app.test_client(self)
        tester.post('/', data=dict(username="tester"), follow_redirects = True)
        response = tester.post('/submit_answer',data=dict(answer="time", solution="Time"), follow_redirects = True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'tester, your score is 1 / 1' in response.data)
    # test the response when an incorrect answer is given   
    def test_incorrect_answer(self):
        tester = app.test_client(self)
        tester.post('/', data=dict(username="tester"), follow_redirects = True)
        response = tester.post('/submit_answer',data=dict(answer="dark", solution="Time"), follow_redirects = True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'tester, your score is 0 / 0' in response.data)
        self.assertTrue(b'is incorrect. Please try again.' in response.data)
    # test the whole quiz whilst imputting correct answers and checking leaderboard message    
    def test_all_questions_correct_leaderboard(self):
        tester = app.test_client(self)
        tester.post('/', data=dict(username="tester"), follow_redirects = True)
        tester.post('/submit_answer',data=dict(answer="time", solution="Time"), follow_redirects = True)
        tester.post('/submit_answer',data=dict(answer="mountain", solution="Mountain"), follow_redirects = True)
        tester.post('/submit_answer',data=dict(answer="river", solution="River"), follow_redirects = True)
        tester.post('/submit_answer',data=dict(answer="shoe", solution="Shoe"), follow_redirects = True)
        tester.post('/submit_answer',data=dict(answer="Fish", solution="Fish"), follow_redirects = True)
        tester.post('/submit_answer',data=dict(answer="dark", solution="Dark"), follow_redirects = True)
        tester.post('/submit_answer',data=dict(answer="teeth", solution="Teeth"), follow_redirects = True)
        tester.post('/submit_answer',data=dict(answer="egg", solution="Egg"), follow_redirects = True)
        tester.post('/submit_answer',data=dict(answer="Wind", solution="Wind"), follow_redirects = True)
        response = tester.post('/submit_answer',data=dict(answer="talent", solution="Talent"), follow_redirects = True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'You scored 10/10. You have mad Google skills' in response.data)
        
    # test the whole quiz whilst imputting correct answers and 2 skips and then checking leaderboard message     
    def test_complete_quiz_with_two_skips(self):
        tester = app.test_client(self)
        tester.post('/', data=dict(username="tester"), follow_redirects = True)
        tester.post('/submit_answer',data=dict(answer="time", solution="Time"), follow_redirects = True)
        tester.post('/skip_question', follow_redirects = True)
        tester.post('/submit_answer',data=dict(answer="river", solution="River"), follow_redirects = True)
        tester.post('/submit_answer',data=dict(answer="shoe", solution="Shoe"), follow_redirects = True)
        tester.post('/submit_answer',data=dict(answer="Fish", solution="Fish"), follow_redirects = True)
        tester.post('/skip_question', follow_redirects = True)
        tester.post('/submit_answer',data=dict(answer="teeth", solution="Teeth"), follow_redirects = True)
        tester.post('/submit_answer',data=dict(answer="egg", solution="Egg"), follow_redirects = True)
        tester.post('/submit_answer',data=dict(answer="Wind", solution="Wind"), follow_redirects = True)
        response = tester.post('/submit_answer',data=dict(answer="talent", solution="Talent"), follow_redirects = True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b"8/10. Close... but no cigar" in response.data)
    
    # test the quiz by inputting correct answers, incorrect answers and skips, then checking leaderboard message   
    def test_complete_quiz_with_wrong_answers_and_skips(self):
        tester = app.test_client(self)
        tester.post('/', data=dict(username="tester"), follow_redirects = True)
        tester.post('/submit_answer',data=dict(answer="time", solution="Time"), follow_redirects = True)
        tester.post('/submit_answer',data=dict(answer="tree", solution="Mountain"), follow_redirects = True)
        tester.post('/skip_question', follow_redirects = True)
        tester.post('/submit_answer',data=dict(answer="river", solution="River"), follow_redirects = True)
        tester.post('/submit_answer',data=dict(answer="boot", solution="Shoe"), follow_redirects = True)
        tester.post('/skip_question', follow_redirects = True)
        tester.post('/submit_answer',data=dict(answer="Fish", solution="Fish"), follow_redirects = True)
        tester.post('/skip_question', follow_redirects = True)
        tester.post('/submit_answer',data=dict(answer="teeth", solution="Teeth"), follow_redirects = True)
        tester.post('/submit_answer',data=dict(answer="egg", solution="Egg"), follow_redirects = True)
        tester.post('/submit_answer',data=dict(answer="Wind", solution="Wind"), follow_redirects = True)
        response = tester.post('/submit_answer',data=dict(answer="talent", solution="Talent"), follow_redirects = True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'7/10. Above average' in response.data)
        
    
        
    def test_complete_quiz_with_less_than_6_correct_answers(self):
        tester = app.test_client(self)
        tester.post('/', data=dict(username="tester"), follow_redirects = True)
        tester.post('/skip_question', follow_redirects = True)
        tester.post('/skip_question', follow_redirects = True)
        tester.post('/skip_question', follow_redirects = True)
        tester.post('/skip_question', follow_redirects = True)
        tester.post('/submit_answer',data=dict(answer="Fish", solution="Fish"), follow_redirects = True)
        tester.post('/skip_question', follow_redirects = True)
        tester.post('/submit_answer',data=dict(answer="teeth", solution="Teeth"), follow_redirects = True)
        tester.post('/submit_answer',data=dict(answer="egg", solution="Egg"), follow_redirects = True)
        tester.post('/submit_answer',data=dict(answer="Wind", solution="Wind"), follow_redirects = True)
        response = tester.post('/submit_answer',data=dict(answer="talent", solution="Talent"), follow_redirects = True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'5/10. Mediocre' in response.data)
        
    def test_complete_quiz_with_less_than_3_correct_answers(self):
        tester = app.test_client(self)
        tester.post('/', data=dict(username="tester"), follow_redirects = True)
        tester.post('/skip_question', follow_redirects = True)
        tester.post('/skip_question', follow_redirects = True)
        tester.post('/skip_question', follow_redirects = True)
        tester.post('/skip_question', follow_redirects = True)
        tester.post('/skip_question', follow_redirects = True)
        tester.post('/skip_question', follow_redirects = True)
        tester.post('/skip_question', follow_redirects = True)
        tester.post('/skip_question', follow_redirects = True)
        tester.post('/submit_answer',data=dict(answer="Wind", solution="Wind"), follow_redirects = True)
        response = tester.post('/submit_answer',data=dict(answer="talent", solution="Talent"), follow_redirects = True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'2/10. Terrible' in response.data)   
    
    """These are the automated tests for the javascript routes that should perform the same as the previous
    routes although they send new html which will be swapped in rather than a full page reload."""    
    
    def test_js_login_valid_username(self):
        tester = app.test_client(self)
        response = tester.post('/js_login', data=dict(username="tester"), follow_redirects = True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'tester, your score is 0 / 0' in response.data)
        self.assertTrue(b'This thing all things devours: Birds, beasts, trees, flowers; Gnaws iron, bites steel; Grinds hard stones to meal; Slays king, ruins town, And beats high mountain down' in response.data)
       
    def test_js_login_invalid_username(self):
        tester = app.test_client(self)
        response = tester.post('/js_login', data=dict(username="testecdfsfv2348nn8e"), follow_redirects = True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'Username must contain between 3 and 10 characters and cannot contain any spaces' in response.data)   

    def test_js_leaderboard_not_logged_in(self):
        tester = app.test_client(self)
        response = tester.get('/js_leaderboard_no_login', follow_redirects = True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'Leaderboard' in response.data)
    
    def test_js_skip_question(self):
        tester = app.test_client(self)
        tester.post('/js_login', data=dict(username="tester"), follow_redirects = True)
        response = tester.post('/js_skip_question', follow_redirects = True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'tester, your score is 0 / 1' in response.data)
        self.assertTrue(b'What has roots as nobody sees' in response.data)
        
    # test the response when a correct answer is given    
    def test_js_correct_answer(self):
        tester = app.test_client(self)
        tester.post('/js_login', data=dict(username="tester"), follow_redirects = True)
        response = tester.post('/js_submit_answer',data=dict(answer="time", solution="Time"), follow_redirects = True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'tester, your score is 1 / 1' in response.data)
        self.assertTrue(b'What has roots as nobody sees' in response.data)
        
    # test the response when an incorrect answer is given   
    def test_js_incorrect_answer(self):
        tester = app.test_client(self)
        tester.post('/js_login', data=dict(username="tester"), follow_redirects = True)
        response = tester.post('/js_submit_answer',data=dict(answer="dark", solution="Time"), follow_redirects = True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'tester, your score is 0 / 0' in response.data)
        self.assertTrue(b'is incorrect. Please try again.' in response.data)
    
    # Some of the answers submitted are lower case, some have extra whitespace to check they are being stripped properly    
    def test_js_all_questions_correct_leaderboard(self):
        tester = app.test_client(self)
        tester.post('/js_login', data=dict(username="tester"), follow_redirects = True)
        tester.post('/js_submit_answer',data=dict(answer="time", solution="Time"), follow_redirects = True)
        tester.post('/js_submit_answer',data=dict(answer="mountain", solution="Mountain"), follow_redirects = True)
        tester.post('/js_submit_answer',data=dict(answer="river ", solution="River"), follow_redirects = True)
        tester.post('/js_submit_answer',data=dict(answer="shoe", solution="Shoe"), follow_redirects = True)
        tester.post('/js_submit_answer',data=dict(answer="Fish", solution="Fish"), follow_redirects = True)
        tester.post('/js_submit_answer',data=dict(answer=" dark ", solution="Dark"), follow_redirects = True)
        tester.post('/js_submit_answer',data=dict(answer="teeth", solution="Teeth"), follow_redirects = True)
        tester.post('/js_submit_answer',data=dict(answer="egg", solution="Egg"), follow_redirects = True)
        tester.post('/js_submit_answer',data=dict(answer="Wind", solution="Wind"), follow_redirects = True)
        response = tester.post('/submit_answer',data=dict(answer="talent", solution="Talent"), follow_redirects = True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'You scored 10/10. You have mad Google skills' in response.data)
        
    def test_js_complete_quiz_with_two_skips(self):
        tester = app.test_client(self)
        tester.post('/js_login', data=dict(username="tester"), follow_redirects = True)
        tester.post('/js_submit_answer',data=dict(answer="time", solution="Time"), follow_redirects = True)
        tester.post('/js_skip_question', follow_redirects = True)
        tester.post('/js_submit_answer',data=dict(answer="river", solution="River"), follow_redirects = True)
        tester.post('/js_submit_answer',data=dict(answer="shoe", solution="Shoe"), follow_redirects = True)
        tester.post('/js_submit_answer',data=dict(answer="Fish", solution="Fish"), follow_redirects = True)
        tester.post('/js_skip_question', follow_redirects = True)
        tester.post('/js_submit_answer',data=dict(answer="teeth", solution="Teeth"), follow_redirects = True)
        tester.post('/js_submit_answer',data=dict(answer="egg", solution="Egg"), follow_redirects = True)
        tester.post('/js_submit_answer',data=dict(answer="Wind", solution="Wind"), follow_redirects = True)
        response = tester.post('/submit_answer',data=dict(answer="talent", solution="Talent"), follow_redirects = True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b"8/10. Close... but no cigar" in response.data)
        
    def test_js_complete_quiz_with_wrong_answers_and_skips(self):
        tester = app.test_client(self)
        tester.post('/js_login', data=dict(username="tester"), follow_redirects = True)
        tester.post('/js_submit_answer',data=dict(answer="time", solution="Time"), follow_redirects = True)
        tester.post('/js_submit_answer',data=dict(answer="tree", solution="Mountain"), follow_redirects = True)
        tester.post('/js_skip_question', follow_redirects = True)
        tester.post('/js_submit_answer',data=dict(answer="river", solution="River"), follow_redirects = True)
        tester.post('/js_submit_answer',data=dict(answer="boot", solution="Shoe"), follow_redirects = True)
        tester.post('/js_skip_question', follow_redirects = True)
        tester.post('/js_submit_answer',data=dict(answer="Fish", solution="Fish"), follow_redirects = True)
        tester.post('/js_skip_question', follow_redirects = True)
        tester.post('/js_submit_answer',data=dict(answer="teeth", solution="Teeth"), follow_redirects = True)
        tester.post('/js_submit_answer',data=dict(answer="egg", solution="Egg"), follow_redirects = True)
        tester.post('/js_submit_answer',data=dict(answer="Wind", solution="Wind"), follow_redirects = True)
        response = tester.post('/js_submit_answer',data=dict(answer="talent", solution="Talent"), follow_redirects = True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'7/10. Above average' in response.data)
        
    def test_js_complete_quiz_with_less_than_6_correct_answers(self):
        tester = app.test_client(self)
        tester.post('/js_login', data=dict(username="tester"), follow_redirects = True)
        tester.post('/js_skip_question', follow_redirects = True)
        tester.post('/js_skip_question', follow_redirects = True)
        tester.post('/js_skip_question', follow_redirects = True)
        tester.post('/js_skip_question', follow_redirects = True)
        tester.post('/js_submit_answer',data=dict(answer="Fish", solution="Fish"), follow_redirects = True)
        tester.post('/js_skip_question', follow_redirects = True)
        tester.post('/js_submit_answer',data=dict(answer="teeth", solution="Teeth"), follow_redirects = True)
        tester.post('/js_submit_answer',data=dict(answer="egg", solution="Egg"), follow_redirects = True)
        tester.post('/js_submit_answer',data=dict(answer="Wind", solution="Wind"), follow_redirects = True)
        response = tester.post('/js_submit_answer',data=dict(answer="talent", solution="Talent"), follow_redirects = True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'5/10. Mediocre' in response.data)
        
    def test_js_complete_quiz_with_less_than_3_correct_answers(self):
        tester = app.test_client(self)
        tester.post('/js_login', data=dict(username="tester"), follow_redirects = True)
        tester.post('/js_skip_question', follow_redirects = True)
        tester.post('/js_skip_question', follow_redirects = True)
        tester.post('/js_skip_question', follow_redirects = True)
        tester.post('/js_skip_question', follow_redirects = True)
        tester.post('/js_skip_question', follow_redirects = True)
        tester.post('/js_skip_question', follow_redirects = True)
        tester.post('/js_skip_question', follow_redirects = True)
        tester.post('/js_skip_question', follow_redirects = True)
        tester.post('/js_submit_answer',data=dict(answer="Wind", solution="Wind"), follow_redirects = True)
        response = tester.post('/js_submit_answer',data=dict(answer="talent", solution="Talent"), follow_redirects = True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'2/10. Terrible' in response.data)
        
if __name__ == '__main__':
    unittest.main()