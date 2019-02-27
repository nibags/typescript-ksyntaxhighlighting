# TypeScript Syntax Highlighting Definition for Kate

**Author:** Nibaldo González (<nibgonz@gmail.com>)

**Last Change:** February 2019

**Requirements:** KDE Frameworks 5.53.0 or higher

```
This file is part of the KDE's KSyntaxHighlighting Framework.
```
**Last versions:** included in KDE Frameworks 5.56.0+.

## Description:

Add syntax highlighting to KDE text editors (as Kate, KWrite, KDevelop 
or any application that uses the KSyntaxHighlighting or KTextEditor Framework) 
for **TypeScript**, **TypeScript React** & **JavaScript React**.

These files are an extension of the JavaScript highlighter (`javascript.xml`, Version 11) of the KSyntaxHighlighting Framework.

The TypeScript and TypeScript React highlighters require **KDE Frameworks 5.53.0** to work.

The TypeScript React highlighter depends on the TypeScript highlighter; 
the syntax highlighting files of TypeScript and JavaScript React depend on the JavaScript highlighting.

## About XML Files of Syntax Highlighting Definition:

The syntax highlighting definition files, of the KSyntaxHighlighting Framework, 
consist of XML files that are compiled in the KDE Frameworks libraries.

However, these XML files can also be stored in:

	$HOME/.local/share/org.kde.syntax-highlighting/syntax/
	/usr/share/org.kde.syntax-highlighting/syntax/

For more details of KSyntaxHighlighting Framework, visit:
* Official Repository: https://phabricator.kde.org/source/syntax-highlighting/
* Documentation: https://docs.kde.org/stable5/en/applications/katepart/highlight.html


## Installation:

If you do not have the latest version of KDE Frameworks, you can manually install the latest XML files. 

**IMPORTANT:** Also install the latest version of `javascript.xml`; 
a copy of this file is included in this repository ("javascript" directory). 
The file `typescript-react.xml` requires the latest version of `typescript.xml`.

Copy the `*.xml` files to `$HOME/.local/share/org.kde.syntax-highlighting/syntax/` (for local user) or `/usr/share/org.kde.syntax-highlighting/syntax/` (for all users).

Ex.: 
For local user:
```bash
mkdir -p $HOME/.local/share/org.kde.syntax-highlighting/syntax/
cp ./{typescript,typescript-react,javascript-react,javascript/javascript}.xml $HOME/.local/share/org.kde.syntax-highlighting/syntax/
```
For all users:
```bash
sudo mkdir -p /usr/share/org.kde.syntax-highlighting/syntax/
sudo cp ./{typescript,typescript-react,javascript-react,javascript/javascript}.xml /usr/share/org.kde.syntax-highlighting/syntax/
```
