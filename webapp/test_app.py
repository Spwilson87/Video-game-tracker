from app import app
import unittest


class FlaskTestCase(unittest.TestCase):

    #check for html response 200
    def test_home(self):
        tester = app.test_client(self)
        response = tester.get("/home")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_add_game(self):
        tester = app.test_client(self)
        response = tester.get("/add_games")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
        


    # check if content is html
    def test_home_content(self):
        tester = app.test_client(self)
        response = tester.get("/home")
        self.assertRegex(response.content_type, "html")

    # check returned data
    def test_home_data(self):
        tester = app.test_client(self)
        response = tester.get("/home")
        self.assertTrue(b'Use the hamburger in top left to navigate' in response.data)

    def test_add_games(self):
        tester = app.test_client(self)
        response = tester.get("/add_games")
        self.assertTrue(b'Enter Game Name' in response.data)
        self.assertTrue(b'Enter Release Year' in response.data)
        self.assertTrue(b'Enter Genre' in response.data)
        self.assertTrue(b'Enter Developer' in response.data)
        self.assertTrue(b'Enter Publisher' in response.data)
        self.assertTrue(b'Enter Platform' in response.data)
            

if __name__ == "__main__":
    unittest.main()