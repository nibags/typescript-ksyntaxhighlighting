#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ====================================================================
#
#   Copyright 2018 Nibaldo González S. (nibgonz@gmail.com)
#
#   This Source Code Form is subject to the terms of the MIT License.
#   If a copy of the license was not distributed with this file,
#   You can obtain one at: https://opensource.org/licenses/MIT
#
# ====================================================================

#  Simple script that generates the JavaScript React Syntax
#  Highlighting file (javascript-react.xml) and the TypeScript React
#  Syntax Highlighting file (typescript-react.xml).
#  Basically, replaces this data from 'react.xml.tpl':
#    {{{NAME}}}, {{{NAME_LOWERCASE}}}, {{{KATEVERSION}}}
#    {{{EXTENSIONS}}}, {{{MIMETYPES}}}, {{{EXTRA_RULES}}}

# USAGE:
#   $ python3 generate-react-syntax.py
# OR
#   $ python3 generate-react-syntax.py /dir/output/files/

# EXAMPLE:
#   $ python3 generate-react-syntax.py ../syntax/

import sys
import os

templateFile = "react.xml.tpl"

def main():
    # Reminder: increase version of 'react.xml.tpl' if any of these data is modified
    javascript = LanguageBase(name = "JavaScript",
                              kateversion = "5.0",
                              extensions = "*.jsx",
                              mimetypes = "text/jsx;text/x-jsx;application/jsx;application/x-jsx;")

    typescript = LanguageBase(name = "TypeScript",
                              kateversion = "5.53",
                              extensions = "*.tsx",
                              mimetypes = "text/tsx;text/x-tsx;application/tsx;application/x-tsx;")

    # Extra rules
    javascript.addRule(r'<DetectChar context="#stay" attribute="Symbol" char="?" />')

    javascript.generateXMLFile()
    typescript.generateXMLFile()
    return

class LanguageBase:
    def __init__(self, name, kateversion, extensions, mimetypes):
        self.name = name
        self.kateversion = kateversion
        self.extensions = extensions
        self.mimetypes = mimetypes
        self.code = ""

    def generateXMLFile(self):
        with open(templateFile, 'U') as f:
            newFile = f.read()

            while r"{{{NAME}}}" in newFile:
                newFile = newFile.replace(r"{{{NAME}}}", self.name)
            while r"{{{NAME_LOWERCASE}}}" in newFile:
                newFile = newFile.replace(r"{{{NAME_LOWERCASE}}}", self.name.lower())
            while r"{{{KATEVERSION}}}" in newFile:
                newFile = newFile.replace(r"{{{KATEVERSION}}}", self.kateversion)
            while r"{{{EXTENSIONS}}}" in newFile:
                newFile = newFile.replace(r"{{{EXTENSIONS}}}", self.extensions)
            while r"{{{MIMETYPES}}}" in newFile:
                newFile = newFile.replace(r"{{{MIMETYPES}}}", self.mimetypes)
            while r"{{{EXTRA_RULES}}}" in newFile:
                newFile = newFile.replace(r"{{{EXTRA_RULES}}}", self.code)
        
        newFileName = self.name.lower() + "-react.xml"
        
        try:
            if os.path.isdir(sys.argv[1]):
                dirFile = sys.argv[1]
                if dirFile[-1:] != '/':
                    dirFile += '/'
                dirFile += newFileName
                absDir = os.path.abspath(sys.argv[1])
            else:
                dirFile = newFileName
                absDir = os.path.dirname(os.path.abspath(__file__))
                print("Invalid directory: {0}".format(sys.argv[1]))
        except:
            dirFile = newFileName
            absDir = os.path.dirname(os.path.abspath(__file__))
        
        with open(dirFile, "w") as f:
            f.write(newFile)
        
        print("{0} : File generated in {1}".format(newFileName, absDir))
        return

    def addRule(self, text):
        if not self.code:
            self.code = text
        else:
            self.code += "\n\t\t\t" + text


if __name__ == "__main__":
    main()
