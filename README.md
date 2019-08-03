# TypeScript Syntax Highlighting Definition for Kate

**Author:** Nibaldo González (<nibgonz@gmail.com>)

**Last Change:** July 2019

**Requirements:** KDE Frameworks 5.53.0 or higher

**Last versions:** Included in KDE Frameworks 5.61.0+.

```
This file is part of the KDE's KSyntaxHighlighting Framework.
```

## Description:

Add syntax highlighting to KDE text editors (as Kate, KWrite, KDevelop 
or any application that uses the KSyntaxHighlighting or KTextEditor Framework) 
for **TypeScript**, **TypeScript React** & **JavaScript React**.

These files are an extension of the JavaScript highlighter (`javascript.xml`, Version 11).

The TypeScript and TypeScript React highlighters require **KDE Frameworks 5.53.0** to work.

**NOTE:** `typescript-react.xml` depends on `typescript.xml`; 
`typescript.xml` and `javascript-react.xml` depend on the JavaScript highlighter.

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

## List of Versions

<table>
    <tr>
        <th>typescript.xml<br>Version</th>
        <th>Date</th>
        <th>KDE Frameworks</th>
        <th>Relevant Changes</th>
    </tr>
    <tr>
        <td>4</td>
        <td>Jul. 16, 2019</td>
        <td>5.61.0</td>
        <td>Fixed highlighting of keywords before ":" in conditional expressions.</td>
    </tr>
    <tr>
        <td>3</td>
        <td>Feb. 18, 2019</td>
        <td>5.56.0</td>
        <td>Add support to bigint, add the "is" keyword and multiple fixes and improvements.</li>
        </ul></td>
    </tr>
    <tr>
        <td>2</td>
        <td>Dec. 29, 2018</td>
        <td>5.54.0</td>
        <td>Fix float-points and improve types detection.</td>
    </tr>
    <tr>
        <td>1</td>
        <td>Nov. 18, 2018</td>
        <td>5.53.0</td>
        <td></td>
    </tr>
</table>

<table>
    <tr>
        <th>javascript-react.xml<br>Version</th>
        <th>typescript-react.xml<br>Version</th>
        <th>Date</th>
        <th>KDE Frameworks</th>
        <th>Relevant Changes</th>
    </tr>
    <tr>
        <td>-</td>
        <td>4</td>
        <td>Jul. 16, 2019</td>
        <td>5.61.0</td>
        <td>Adapt to the TypeScript highlighter.</td>
    </tr>
    <tr>
        <td>5</td>
        <td>3</td>
        <td>Feb. 20, 2019</td>
        <td>5.56.0</td>
        <td><ul>
            <li>Don't highlight tags within declarations of types, variables, classes and interfaces.</li>
            <li>Fixes tags after substitutions in templates.</li>
        </ul></td>
    </tr>
    <tr>
        <td>4</td>
        <td>2</td>
        <td>Dec. 30, 2018</td>
        <td>5.54.0</td>
        <td><ul>
            <li>Allow type assertion in the tag name.</li>
            <li>Allow tags after the keywords "await" & "yield".</li>
            <li>Allow empty tags and non-ASCII tag name & attributes.</li>
        </ul></td>
    </tr>
    <tr>
        <td>3</td>
        <td>1</td>
        <td>Nov. 18, 2018</td>
        <td>5.53.0</td>
        <td></td>
    </tr>
</table>
