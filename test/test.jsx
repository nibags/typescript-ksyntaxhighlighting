// JavaScript React

/** @author Willy <willy@wmail.com>
  * @url https://reactjs.org/ **/

import React from 'react';
import { PhotoStory, VideoStory } from './stories';

function Story(props) {
  const SpecificStory = components[props.storyType];
  return <SpecificStory story={ props.story } attr2="&ref;" attr3="Hello\n" />;
} 

function 
<Tag attr1={ <tag/> function <noTag/> return class var 0x123 { } &noRef; hello() React.Component() } attr2="&ref;">
	/* no comment*/ function <tag/> return class var 0x123 &ref; hello() React.Component()
	.<tag/> anyWord <tag/>
	{ function <tag> return class var 0x123 hello() React.Component() } 
</Tag>

<tag1> </tag1>
<tag1> </Tag$>
<Tag$> </tag>

<tag/*comment*/attr1/*comment*/= /*comment*/"value"/*comment*/attr2 /*comment*/attr3='a' key/*comment*/key2 />

// Detect Valid tags

/* comment */ <tag></tag>
{ /* comment 
	*/ <Tag /> 
	word <noTag/> . <noTag/> } <noTag/>
return /* comment
	multiline */ <tag/> /* comment */ <Tag/>
&& /*comment*/ <Tag/>
& /*comment*/ <noTag/>

  <tag/>
{ <hello>Hello</hello> }
?<Tag />;
[ <tag />  ( <tag />
,<Tag/>    =<Tag/>
&&<tag/>   ||<tag/>
return <tag/> ;
default<tag/> ;
<Tag> <tag> <tag$/> </tag> return </Tag>

anyWord<noTag>
anyWord/*comment*/ <noTag/>
.<noTag>
&<notag> | <noTag/>
% /* comment*/ <noTag/>

<C<number>/>
<C<number>> </C>
<C
<error />

// Non-ASCII tag name & attribute
<日本語></日本語>;
<Component 本本:本-本 aa本:本 aa:aa />

<Namespace.DeepNamespace.Component />;
<Component { ... x } y
={2 } z />;

let k1 = <div> <h2> Hello </h2> <h1> world </h1></div>;
let k2 = <Button> <h2> Hello </h2> </Button>;

// Empty tags
<></>; // no whitespace
<    ></   >; // lots of whitespace
< /*starting wrap*/ ></ /*ending wrap*/>; // comments in the tags
<>hi</>; // text inside
<><span>hi</span><div>bye</div></>; // children
<><span>1</span><><span>2.1</span><span>2.2</span></><span>3</span></>; // nested fragments
<>#</>; // # would cause scanning error if not in jsxtext
