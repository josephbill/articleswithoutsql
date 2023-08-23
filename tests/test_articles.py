import sys
import os
# Adjust the path to the parent directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from articlesapp.articles import Article

class TestArticle(unittest.TestCase):
    def setUp(self):
        # Create a mock Author and Magazine for testing
        class MockAuthor:
            def __init__(self, name):
                self.name = name
                self._articles = []
            
            def articles(self):
                return self._articles

        class MockMagazine:
            def __init__(self, name):
                self.name = name
                self._articles = []
            
            def add_contributor(self, author):
                pass

        self.mock_author = MockAuthor("John Doe")
        self.mock_magazine = MockMagazine("Tech Magazine")

    def test_article_initialization(self):
        article = Article(self.mock_author, self.mock_magazine, "Sample Article")
        
        self.assertEqual(article.title(), "Sample Article")
        self.assertEqual(article.author(), self.mock_author)
        self.assertEqual(article.magazine(), self.mock_magazine)
        
        self.assertIn(article, Article.all())

        self.assertIn(article, self.mock_author.articles())
        self.assertIn(article, self.mock_magazine._articles)

    def test_all_articles(self):
        initial_count = len(Article.all())
        article1 = Article(self.mock_author, self.mock_magazine, "Article 1")
        article2 = Article(self.mock_author, self.mock_magazine, "Article 2")

        self.assertEqual(len(Article.all()), initial_count + 2)
        self.assertIn(article1, Article.all())
        self.assertIn(article2, Article.all())

if __name__ == '__main__':
    unittest.main()
