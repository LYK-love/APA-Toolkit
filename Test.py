from unittest import TestCase

from main import generate_book_citation, generate_ebook_citation, generate_website_citation

import difflib


class Test(TestCase):
    def test_generate_ebook_citation(self):
        expected = "Bernard Kolman, Robert C. Busby & Sharon Cutler Ros. (2014). *Relations and Digraph. Discrete Mathematical Structures: A Modern Approach* (6th ed., pp. 139-204). Pearson."
        author_names = "Bernard Kolman, Robert C. Busby, Sharon Cutler Ros"
        title = "Discrete Mathematical Structures"
        sub_title = "A Modern Approach"
        chapter = "Relations and Digraph"
        publication_year = "2014"
        edition = "6"
        page_num = "139-204"
        publisher = "Pearson"
        citation = generate_book_citation(author_names, title, sub_title, chapter, publication_year, edition, page_num,
                                          publisher)
        assert citation == expected

    def test_generate_book_citation(self):
        expected = "Aston Zhang, Zachary C. Lipton, Mu Li & Alex J. Smola. *[Chapter 1. Introduction. Dive into Deep Learning: A Modern Approach](http://d2l.ai/index.html)*."

        author_names = "Aston Zhang, Zachary C. Lipton, Mu Li, Alex J. Smola"
        title = "Dive into Deep Learning"
        sub_title = "A Modern Approach"
        chapter = "Chapter 1. Introduction"
        url = "http://d2l.ai/index.html"

        citation = generate_ebook_citation(author_names, title, sub_title, chapter, url)
        assert citation == expected

    def test_generate_website_citation(self):
        expected = "Aston Zhang, Zachary C. Lipton, Mu Li & Alex J. Smola. *[Dive into Deep Learning](http://d2l.ai/index.html#)*."

        author_names = "Aston Zhang, Zachary C. Lipton, Mu Li, Alex J. Smola"
        title = "Dive into Deep Learning"
        url = "http://d2l.ai/index.html#"

        citation = generate_website_citation(author_names, title, url)
        assert citation == expected

        # No author
        expected2 = "*[Dive into Deep Learning](http://d2l.ai/index.html#)*."
        citation2 = generate_website_citation("", title, url)
        assert citation2 == expected2

