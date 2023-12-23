import pyclip
from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter

def generate_book_citation(author_names, title, sub_title, chapter, publication_year, edition, page_num, publisher):

    '''
    Given user input, generate the apa 7th style citation in Markdown version.
    Note that the title of the book should be italic in apa. And in Markdown italic text is represented with "*[text]*".
    So the title will be: "*title*".

    E.g.,
    Bernard Kolman, Robert C. Busby & Sharon Cutler Ros. (2014). Relations and Digraph. *Discrete Mathematical Structures* (6th ed., pp. 139-204). Pearson.
    :return:
    '''

    author_string = __format_author_names(author_names)
    title_string = __format_title(title, sub_title, chapter)

    def __format_edition_and_page_num(edition, page_num):
        if not edition == "":
            ed = int(edition)
            if ed == 1:
                edition = "1st"  # 1st ed.
            elif ed == 2:
                edition = "2nd"  # 2nd ed.
            else:
                edition = f"{ed}th"

        if not page_num == "":
            page_num = "pp. " + page_num  # pp. 139-204

        edition_and_pageNum_part = ""
        if (not edition == "") and (not page_num == ""):
            edition_and_pageNum_part = edition + " ed." + ", " + page_num  # (6th ed., pp. 139-204)
        elif not edition == "":
            edition_and_pageNum_part = edition + " ed."  # (6th ed.)
        elif not page_num == "":
            edition_and_pageNum_part = page_num  # (pp. 139-204)
        else:
            pass
        return edition_and_pageNum_part

    edition_and_page_num_string = __format_edition_and_page_num(edition, page_num)

    citation = f"{author_string}. ({publication_year}). *{title_string}* ({edition_and_page_num_string}). {publisher}."

    return citation

def generate_ebook_citation(author_names, title, sub_title, chapter, url):
    author_string = __format_author_names(author_names)
    title_string = __format_title(title, sub_title, chapter)


    citation = f"{author_string}. *[{title_string}]({url})*."
    return citation


def generate_website_citation(author_names, title, url):


    if not author_names == "":
        author_string = __format_author_names(author_names)
        citation = f"{author_string}. *[{title}]({url})*."
    else:
        citation = f"*[{title}]({url})*."  # Don't need to write website's author.
    return citation



def __format_author_names(author_names):
    authors = [author_name.strip() for author_name in author_names.split(',')]
    if len(authors) == 1:
        formatted_author_names = authors[0]
    else:
        formatted_author_names = ', '.join(authors[:-1]) + ' & ' + authors[-1]  # A [-1] provides the last element of the list.
    return formatted_author_names

def __format_title(title, sub_title, chapter):
    title_string = title
    if sub_title == "":
        pass
    else:
        title_string = title_string + ": " + sub_title

    if chapter == "":
        pass
    else:
        title_string = chapter + ". " + title_string
    return title_string

if __name__ == "__main__":
    functions = ["generate_book_citation", "generate_ebook_citation", "generate_website_citation"]
    function_completer = WordCompleter(functions)

    # 创建 PromptSession 对象
    session = PromptSession()
    print("APA Style Citation Generator")
    print("Generating the markdown version of [apa 7th](https://apastyle.apa.org/products/publication-manual-7th-edition) citations.")
    print("Skip the question if there's no answer for that part.")
    print('''Note:
        1. Due to the capability to markdown, some details are different from original apa 7th style.
        2. If the number of authors is too much, You can simply input `author names` as "<First author> et al"
        ''')
    print("============================")

    print(f'''
    Operations:
        * generate_book_citation
        * generate_ebook_citation
        * generate_website_citation
        '''
          )

    function = session.prompt("Please select operation: ", completer=function_completer)



    if function not in functions:
        print("Feature not supported.")
    else:

        if function == "generate_book_citation":
            author_names = input("Enter the author names (comma-separated): ").strip()
            title = input("Enter the title of the work: ").strip()
            sub_title = input("Enter the sub-title of the work: ").strip()
            chapter = input("Enter the chapter name of the work: ").strip()
            publication_year = input("Enter the publication year: ").strip()
            edition = input("Enter the edition number: ").strip()
            pageNum = input("Enter the pageNumber(E.g., 139-204): ").strip()
            publisher = input("Enter the publisher's name: ").strip()

            citation = generate_book_citation(author_names, title, sub_title, chapter, publication_year, edition, pageNum, publisher)
            print(citation)
            pyclip.copy(citation)
            print("The text has been copied to your clipboard")
        elif function == "generate_ebook_citation":
            author_names = input("Enter the author names (comma-separated): ").strip()
            title = input("Enter the title of the work: ").strip()
            sub_title = input("Enter the sub-title of the work: ").strip()
            chapter = input("Enter the chapter name of the work: ").strip()
            url = input("Enter the URL: ")
            citation = generate_ebook_citation(author_names, title, sub_title, chapter, url)
            print(citation)
            pyclip.copy(citation)
            print("The text has been copied to your clipboard")
        elif function == "generate_website_citation":
            author_names = input("Enter the author names (comma-separated): ").strip()
            title = input("Enter the title of the work: ").strip()
            url = input("Enter the URL: ")
            citation = generate_website_citation(author_names, title, url)
            print(citation)
            pyclip.copy(citation)
            print("The text has been copied to your clipboard")
        else:
            print("Error")


