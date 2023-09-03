import pyclip


def generate_apa_citation():

    '''
    Given user input, generate the apa 7th style citation in Markdown version.
    Note that the title of the book should be italic in apa. And in Markdown italic text is represented with "*[text]*".
    So the title will be: "*title*".

    E.g.,
    Bernard Kolman, Robert C. Busby & Sharon Cutler Ros. (2014). Relations and Digraph. *Discrete Mathematical Structures* (6th ed., pp. 139-204). Pearson.
    :return:
    '''
    author_names = input("Enter the author names (comma-separated): ").strip()
    title = input("Enter the title of the work: ").strip()
    subTitle = input("Enter the sub-title of the work: ").strip()
    chapter = input("Enter the chapter name of the work: ").strip()

    publication_year = input("Enter the publication year: ").strip()
    edition = input("Enter the edition number: ").strip()
    pageNum = input("Enter the pageNumber(E.g., 139-204): ").strip()
    publisher = input("Enter the publisher's name: ").strip()

    authors = author_names.split(', ')
    if len(authors) == 1:
        formatted_authors = authors[0]
    else:
        formatted_authors = ', '.join(authors[:-1]) + ' & ' + authors[-1] # A [-1] provides the last element of the list.

    if not subTitle == "":
        subTitle = ": " + subTitle # XXX: AAAA

    if not edition == "":
        ed = int(edition)
        if ed == 1:
            edition = "1st" # 1st ed.
        elif ed == 2:
            edition = "2nd" # 2nd ed.
        else:
            edition = f"{ed}th"
        edition += " ed." # 6th ed.

    if not pageNum == "":
        pageNum = "pp. " + pageNum # pp. 139-204

    edition_and_pageNum_part = ""
    if (not edition == "") and (not pageNum == ""):
        edition_and_pageNum_part = "(" + edition + ", " + pageNum + ")" # (6th ed., pp. 139-204)
    elif not edition == "":
        edition_and_pageNum_part = "(" + edition + ")" # (6th ed.)
    elif not pageNum == "":
        edition_and_pageNum_part = "(" + pageNum + ")"# (pp. 139-204)
    else:
        pass

    if chapter is not "":
        chapter = " " + chapter + ". "
    else:
        chapter = " "

    citation = f"{formatted_authors}. ({publication_year}).{chapter}*{title}{subTitle}* {edition_and_pageNum_part}. {publisher}."

    return citation

def main():
    print("APA Style Citation Generator")
    print("Skip the question if there's no answer for that part.")

    print("============================")
    citation = generate_apa_citation()
    print("\nGenerated APA Style Citation:")
    print(citation)
    print("The text has been copied to your clipboard")
    pyclip.copy(citation)

if __name__ == "__main__":
    main()
