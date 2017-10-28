import os
import starred_repos
import unittest
import tempfile

class RepoTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, flaskr.app.config['DATABASE'] = tempfile.mkstemp()
        starred_repos.app.testing = True
        self.app = starred_repos.app.test_client()
        with starred_repos.app.app_context():
            starred_repos.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(starred_repos.app.config['DATABASE'])

if __name__ == '__main__':
    unittest.main()
