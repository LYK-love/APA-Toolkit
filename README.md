# APA-Toolkit
A python toolkit for creating and checking citations of [APA style (7th)](https://apastyle.apa.org/style-grammar-guidelines/references/examples/edited-book-chapter-references) for scientific writing.

The output is in Markdown version. E.g., The italic part `text` is represented as `*text*`

Note: I use [pyclip](https://pypi.org/project/pyclip/) to copy the generated citation to your clipboard.
```shell
python main.py
```
# Usage
## For Books
```text
APA Style Citation Generator
Generating the markdown version of [apa 7th](https://apastyle.apa.org/products/publication-manual-7th-edition) citations.
Skip the question if there's no answer for that part.
Note:
        1. Due to the capability to markdown, some details are different from original apa 7th style.
        2. If the number of authors is too much, You can simply input `author names` as "<First author> et al"
        
============================

    Operations:
        * generate_book_citation
        * generate_ebook_citation
        * generate_website_citation
        
Please select operation: generate_book_citation
Enter the author names (comma-separated): Bernard Kolman, Robert C. Busby, Sharon Cutler Ros
Enter the title of the work: Discrete Mathematical Structures
Enter the sub-title of the work: Any subtitle you want
Enter the chapter name of the work: Relations and Digraph
Enter the publication year: 2014
Enter the edition number: 6
Enter the pageNumber(E.g., 139-204): 139-204
Enter the publisher's name: Pearson
Bernard Kolman, Robert C. Busby & Sharon Cutler Ros. (2014). *Relations and Digraph. Discrete Mathematical Structures: Any subtitle you want* (6th ed., pp. 139-204). Pearson.
The text has been copied to your clipboard
```
The result is:

Bernard Kolman, Robert C. Busby & Sharon Cutler Ros. (2014). *Relations and Digraph. Discrete Mathematical Structures: Any subtitle you want* (6th ed., pp. 139-204). Pearson.
## For Ebooks
If the book has too many authors. You can simply input "[first author]" et al.

```text
<...>
Please select operation: generate_ebook_citation
Enter the author names (comma-separated): Mu Li et al
Enter the title of the work: Dive into Deep Learning
Enter the sub-title of the work: 
Enter the chapter name of the work: 1. Introduction        
Enter the URL: http://d2l.ai/index.html#
Mu Li et al. *[1. Introduction. Dive into Deep Learning](http://d2l.ai/index.html#)*.
The text has been copied to your clipboard
```

The result is:
Mu Li et al. *[1. Introduction. Dive into Deep Learning](http://d2l.ai/index.html#)*.

## For websites

```text
<...>
Please select operation: generate_website_citation
Enter the author names (comma-separated): 
Enter the title of the work: Dive into Deep Learning
Enter the URL: http://d2l.ai/index.html#
*[Dive into Deep Learning](http://d2l.ai/index.html#)*.
The text has been copied to your clipboard
```

The result is
*[Dive into Deep Learning](http://d2l.ai/index.html#)*.