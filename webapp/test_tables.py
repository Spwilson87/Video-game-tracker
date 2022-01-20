from app import app
import unittest


class FlaskTestCase(unittest.TestCase):

    #check for html response 200
    def test_owned_table(self):
        tester = app.test_client(self)
        response = tester.get("/owned_table")
        # self.assertTrue(b'game_id' in response.data)
        # self.assertTrue(b'game_name' in response.data)
        # self.assertTrue(b'release_year' in response.data)
        # self.assertTrue(b'genre' in response.data)
        # self.assertTrue(b'developer' in response.data)
        # self.assertTrue(b'publisher' in response.data)
        # self.assertTrue(b'platform' in response.data)
        self.assertTrue(b'Enter Game ID to Add to Playing Games' in response.data)

            

if __name__ == "__main__":
    unittest.main()