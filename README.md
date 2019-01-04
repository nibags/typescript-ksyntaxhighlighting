# TypeScript Syntax Highlighting Definition for Kate

**Author:** Nibaldo González (<nibgonz@gmail.com>)

**Last Change:** December 2018

**Requirements:** KDE Frameworks 5.53.0 or higher

```
This file is part of the KDE's KSyntaxHighlighting Framework.
```
**Last version:** Version 2 included in KDE Frameworks 5.54.0+.

## Description:

Add syntax highlighting to KDE text editors (as Kate, KWrite, KDevelop 
or any application that uses the KSyntaxHighlighting or KTextEditor Framework) 
for **TypeScript**, **TypeScript React** & **JavaScript React**.

These files are an extension of the JavaScript highlighter (`javascript.xml`, Version 10) of the KSyntaxHighlighting Framework.

The latest version of these files are included in KDE Frameworks 5.53.0 and require that version to work.


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

Copy the `*.xml` files to `$HOME/.local/share/org.kde.syntax-highlighting/syntax/` (for local user) or `/usr/share/org.kde.syntax-highlighting/syntax/` (for all users).

Ex.: 
For local user:
```bash
mkdir -p $HOME/.local/share/org.kde.syntax-highlighting/syntax/
cp ./{typescript,typescript-react,javascript-react}.xml $HOME/.local/share/org.kde.syntax-highlighting/syntax/
```
For all users:
```bash
sudo mkdir -p /usr/share/org.kde.syntax-highlighting/syntax/
sudo cp ./{typescript,typescript-react,javascript-react}.xml /usr/share/org.kde.syntax-highlighting/syntax/
```
