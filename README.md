# Welcome to docfinder
 
Designed to find a pdf-file given a specific search pattern. The script searches in all files and directories including subdirectories and their files for a given search pattern (i.e. a String). Useful when looking for something in large pdf datasets. Throws an exception when a corrupted pdf file is found. This can happen due to missing or wrong CMaps.
 
## Dependencies
 
    import os
    import PyPDF2
    import webbrowser
 
## Usage
 
    find_file_by_pattern('example', r'C:\ExampleDirectory', True)