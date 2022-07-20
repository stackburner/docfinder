import os
import platform
import PyPDF2
import webbrowser
import subprocess


def find_file_by_pattern(pattern, directory, openfile=False):
    """
    Returns the path to the pdf-file that contains the given search string.
    Searches in files, directories and subdirectories.

            Parameters:
                    pattern (str): The pattern to search for
                    directory (str): The directory to search in
                    openfile (bool): Whether found file should ne opened or not

            Returns:
                    res (str): Path to the pdf-file that contains the pattern
    """
    for root, dirs, files in os.walk(directory):
        for fname in files:
            if fname.endswith('.pdf'):
                f = open(os.path.join(root, fname), 'rb')
                # Try/catch because corrupted pdf files with missing CMaps cannot be read
                try:
                    filereader = PyPDF2.PdfFileReader(f)
                except Exception as e:
                    print(f'Found non extractable pdf {os.path.join(root, fname)} due to: {str(e)}')
                    f.close()
                    continue

                text = ''
                for i in range(filereader.numPages):
                    page = filereader.pages[i]
                    text = text + page.extract_text()
                if pattern in text:
                    res = os.path.join(root, fname)
                    f.close()
                    if openfile:
                        if platform.system() == 'Windows':
                            webbrowser.open_new(res)
                        elif platform.system() == 'Darwin':
                            subprocess.call(['open', '-a', 'Preview', res])
                        else:
                            print('Opening file not supported on this platform!')
                    return res

                else:
                    f.close()

    print('No file found for the given pattern.')
    return None
