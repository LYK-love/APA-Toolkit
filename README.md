# APA-Toolkit
A python toolkit for creating and checking citations of [APA style (7th)](https://apastyle.apa.org/style-grammar-guidelines/references/examples/edited-book-chapter-references) for scientific writing.

The output is in Markdown version. E.g., The italic part `text` is represented as `*text*`

Note: I use [pyclip](https://pypi.org/project/pyclip/) to copy the generated citation to your clipboard.
```shell
python main.py
```
# Usage
```text
APA Style Citation Generator
Skip the question if there's no answer for that part.
============================
Enter the author names (comma-separated): Bernard Kolman, Robert C. Busby, Sharon Cutler Ros
Enter the title of the work: Discrete Mathematical Structures
Enter the sub-title of the work: 
Enter the chapter name of the work: Relations and Digraph
Enter the publication year: 2014
Enter the edition number: 6
Enter the pageNumber(e.g. 139-204): 139-204
Enter the publisher's name: Pearson

Generated APA Style Citation:
Bernard Kolman, Robert C. Busby & Sharon Cutler Ros. (2014). Relations and Digraph. *Discrete Mathematical Structures* (6th ed., pp. 139-204). Pearson.
The text has been copied to your clipboard

```
The result is:

Bernard Kolman, Robert C. Busby & Sharon Cutler Ros. (2014). Relations and Digraph. *Discrete Mathematical Structures* (6th ed., pp. 139-204). Pearson.