from articlesapp.articles import Article
from articlesapp.author import Author
from articlesapp.magazine import Magazine

# Creating instances
author1 = Author("John Doe")
author2 = Author("Jane Smith")
magazine1 = Magazine("Tech Magazine", "Technology")
magazine2 = Magazine("Science Journal", "Science")

author1.add_article(magazine1, "Python Programming")
author1.add_article(magazine2, "Exploring the Cosmos")
author2.add_article(magazine1, "Web Development Trends")

print("Author:", author1.name())
print("Author's Articles:", [article.title() for article in author1.articles()])
print("Author's Magazines:", [magazine.name() for magazine in author1.magazines()])
print("All Magazines:", [magazine.name() for magazine in Magazine._all_magazines])
print("Magazine Contributors:", [contributor.name() for contributor in magazine1.contributors()])
print("Article Titles:", Magazine.article_titles())