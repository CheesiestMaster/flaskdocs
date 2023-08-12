# Markdown
Markdown is a lightweight markup language with plain text formatting syntax. It is designed so that it can be converted to HTML and many other formats using a tool by the same name. Markdown is often used to format readme files, for writing messages in online discussion forums, and to create rich text using a plain text editor.
## Headers
# H1
## H2
### H3
#### H4
##### H5
###### H6
## Emphasis
*This text will be italic*
_This will also be italic_
**This text will be bold**
__This will also be bold__
_You **can** combine them_
## Lists
### Unordered
* Item 1
* Item 2
  * Item 2a
  * Item 2b
### Ordered
1. Item 1
1. Item 2
1. Item 3
   1. Item 3a
   1. Item 3b
## Links
http://github.com - automatic!
[GitHub](http://github.com)
## Blockquotes
```
This is a blockquote with two paragraphs. Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aliquam hendrerit mi posuere lectus.
```
## Inline code
`$ npm install marked`
## Syntax highlighting
```javascript
function fancyAlert(arg) {
  if(arg) {
    $.facebox({div:'#foo'})
  }
}
```
## Tables
| First Header | Second Header |
| ------------ | ------------- |
| Content cell 1 | Content cell 2 |
| Content column 1 | Content column 2 |

## Task Lists
- [x] [links](), **formatting**, and <del>tags</del> supported
- [x] list syntax required (any unordered or ordered list supported)
- [x] this is a complete item
- [ ] this is an incomplete item
# Markdown